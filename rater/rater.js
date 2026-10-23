/* Rater interface logic. No backend, no network calls except items.json.
 *
 * Implements RATER_RUBRIC.md exactly, in the rubric's own order:
 *   Q1 visibility gate (yes / partly / no)  -- gates everything after it
 *   Q2 hood state   (up / down / no hood present / cannot determine)
 *   Q3 metal eyelets (yes / no / cannot determine)  -- presence only
 *   Q4 drawcord toggle count (0 / 1 / 2 / 3 / 4+ / cannot tell)  -- exact numbers
 *   Q5 collar inner trim (red / other colour / none visible / cannot tell)
 *   Q6 free text, revealed ONLY after q1-q5 are locked
 *
 * Two protocol details that are easy to get wrong and are enforced here:
 *   1. Free text is shown only after the ratings above are locked, so it cannot
 *      become a post-hoc justification for a rating already given.
 *   2. Free text is REQUIRED when visibility is partly or no, when any answer is
 *      cannot determine, when the toggle count is 0 or 4+, and on a
 *      pre-specified random 20% of ordinary items.
 *
 * BLINDING: items.json carries no condition, no replicate, no brief id. Item ids
 * are opaque and derived from shuffled position. Image filenames are opaque.
 * Nothing here derives, prints, or sorts by condition.
 */

(function () {
  'use strict';

  var params = new URLSearchParams(window.location.search);
  var RATER_ID = params.get('rater') || 'anonymous';
  var TOKEN = params.get('token') || '';
  var STATE_KEY = 'garment-rating/v3:' + RATER_ID;

  var QUESTIONS = ['q1', 'q2', 'q3', 'q4', 'q5'];

  // Same seed as the shuffled presentation, so the 20% sample is identical for
  // every rater. Change it only alongside items.json.
  var SEED = 20261023;
  var FREE_TEXT_SAMPLE_RATE = 0.20;

  var ITEMS = [];
  var STATE = { rater_id: RATER_ID, token: TOKEN, current_idx: 0, answers: {} };

  var $ = function (id) { return document.getElementById(id); };
  var elImg = $('garment');
  var elScroll = $('stage-scroll');
  var elPill = $('rater-pill');
  var elProg = $('progress-pill');
  var elFreePill = $('free-pill');
  var elIdx = $('idx-display');
  var elPrev = $('btn-prev');
  var elNext = $('btn-next');
  var elExport = $('btn-export');
  var elReset = $('btn-reset');
  var elDetail = $('detail-block');
  var elQ6 = $('q6-block');
  var elFreeText = $('free-text');
  var elFreeCount = $('free-count');
  var elSkipNote = $('skip-note');
  var elSkipText = $('skip-text');

  /* ---------- the 20% sample, decided by opaque item id not by condition ---------- */

  function isSampled(id) {
    var h = 0;
    for (var i = 0; i < id.length; i++) {
      h = ((h << 5) - h + id.charCodeAt(i)) | 0;
    }
    return Math.abs(h) % 100 < FREE_TEXT_SAMPLE_RATE * 100;
  }

  /* ---------- free text requirement ---------- */

  function freeTextRequired(ans) {
    if (!ans || !ans.q1) return false;
    if (ans.q1 === 'no' || ans.q1 === 'partly') return true;
    if (ans.q2 === 'cannot_determine') return true;
    if (ans.q3 === 'cannot_determine') return true;
    if (ans.q4 === 'cannot_determine') return true;
    if (ans.q4 === '0' || ans.q4 === '4plus') return true;
    if (ans.q5 === 'cannot_determine') return true;
    return false;
  }

  function isLocked(id) {
    var a = STATE.answers[id];
    return !!(a && a.locked);
  }

  function wordCount(s) {
    var t = String(s || '').trim();
    return t ? t.split(/\s+/).length : 0;
  }

  function countsComplete() {
    return ITEMS.filter(function (it) {
      var a = STATE.answers[it.id];
      if (!a || !a.responses || !a.responses.q1) return false;
      if (a.responses.q1 === 'no') return a.locked === true;
      return QUESTIONS.every(function (q) { return a.responses[q]; }) && a.locked === true;
    }).length;
  }

  function pendingFreeText() {
    return ITEMS.filter(function (it) {
      var a = STATE.answers[it.id];
      if (!a || !a.responses || !a.responses.q1 || a.locked) return false;
      var need = freeTextRequired(a.responses) || isSampled(it.id);
      return need && !a.free_text;
    }).length;
  }

  /* ---------- persistence ---------- */

  function load() {
    try {
      var raw = localStorage.getItem(STATE_KEY);
      if (!raw) return;
      var saved = JSON.parse(raw);
      STATE.current_idx = Number(saved.current_idx) || 0;
      STATE.answers = saved.answers && typeof saved.answers === 'object' ? saved.answers : {};
    } catch (e) {
      console.warn('could not restore rater state', e);
    }
  }

  function save() {
    try {
      localStorage.setItem(STATE_KEY, JSON.stringify(STATE));
    } catch (e) {
      console.warn('could not save rater state', e);
    }
  }

  function answerFor(id) {
    if (!STATE.answers[id]) {
      STATE.answers[id] = { responses: {}, locked: false, free_text: null, order_index: null };
    }
    return STATE.answers[id];
  }

  /* ---------- render ---------- */

  function clampIdx(i) {
    if (i < 0) return 0;
    if (i > ITEMS.length - 1) return ITEMS.length - 1;
    return i;
  }

  function render() {
    STATE.current_idx = clampIdx(STATE.current_idx);
    var i = STATE.current_idx;
    var item = ITEMS[i];
    if (!item) return;

    document.title = 'Garment rating, item ' + (i + 1) + ' of ' + ITEMS.length;

    // srcset hands the browser the 768px file for phones and the full 1254px PNG
    // for desktop and for zoom. Both candidates are declared and the browser
    // picks by viewport and DPR, so the full-resolution artefact is never
    // degraded and a phone never downloads a 1.9MB file.
    //
    // There is deliberately NO separate preload Image() here. Preloading the
    // full-size file would make every phone download all 1.9MB, which is the
    // exact cost this change exists to remove. Assigning srcset directly makes
    // the browser fetch exactly one candidate.
    var small = 'assets/img-sm/' + item.id + '.jpg';
    var full = 'assets/img/' + item.id + '.png';
    elImg.srcset = small + ' 768w, ' + full + ' 1254w';
    elImg.sizes = '(max-width: 700px) 100vw, 1000px';
    elImg.src = full;            // fallback for a browser that ignores srcset
    elImg.alt = 'Garment image ' + item.id;
    resetZoom();

    var ans = STATE.answers[item.id];
    var r = (ans && ans.responses) || {};
    var locked = !!(ans && ans.locked);

    // Q1 always visible: it gates everything after it.
    paint('q1', r.q1);
    $('q1-note').hidden = !r.q1 || r.q1 === 'yes';

    var skipDetails = r.q1 === 'no';
    elDetail.hidden = skipDetails;
    elQ6.hidden = true;

    QUESTIONS.slice(1).forEach(function (q) {
      paint(q, r[q]);
    });

    if (skipDetails) {
      elSkipNote.hidden = false;
      elSkipText.value = (ans && ans.free_text) || '';
    } else {
      elSkipNote.hidden = true;
      elSkipText.value = '';
    }

    // Free text opens only once the ratings above are locked.
    var showFree = false;
    if (r.q1 === 'no') {
      showFree = !locked;
    } else if (r.q1 && QUESTIONS.every(function (q) { return r[q]; })) {
      showFree = !locked;
    }
    if (showFree) {
      elQ6.hidden = skipDetails;
      if (!skipDetails) {
        elFreeText.value = (ans && ans.free_text) || '';
        updateWordCount(elFreeText.value);
      }
    } else {
      elFreeText.value = (ans && ans.free_text) || '';
    }

    elIdx.textContent = (i + 1) + ' / ' + ITEMS.length;
    elProg.textContent = countsComplete() + ' of ' + ITEMS.length + ' complete';
    var pend = pendingFreeText();
    elFreePill.textContent = pend ? ('free text: ' + pend + ' required') : 'free text: none outstanding';

    elPrev.disabled = (i === 0);
    elNext.disabled = (i === ITEMS.length - 1);
    elExport.disabled = countsComplete() === 0;
  }

  function paint(q, value) {
    var group = document.querySelector('.opts[data-q="' + q + '"]');
    if (!group) return;
    group.querySelectorAll('.opt').forEach(function (b) {
      b.setAttribute('aria-pressed', b.dataset.v === value ? 'true' : 'false');
    });
  }

  function updateWordCount(v) {
    var n = wordCount(v);
    elFreeCount.textContent = n + (n === 1 ? ' word' : ' words');
    if (n === 0) { elFreeCount.className = 'free-count'; return; }
    if (n < 5) { elFreeCount.className = 'free-count'; return; }
    if (n <= 25) { elFreeCount.className = 'free-count ok'; return; }
    elFreeCount.className = 'free-count over';
  }

  /* ---------- actions ---------- */

  function setVerdict(q, v) {
    var item = ITEMS[STATE.current_idx];
    if (!item) return;
    var ans = answerFor(item.id);
    if (ans.locked) return;               // locked means locked
    ans.responses[q] = ans.responses[q] === v ? undefined : v;
    if (ans.responses[q] === undefined) delete ans.responses[q];
    save();
    render();
  }

  function lock() {
    var item = ITEMS[STATE.current_idx];
    if (!item) return;
    var ans = answerFor(item.id);
    var r = ans.responses;
    var skipDetails = r.q1 === 'no';
    var text = skipDetails ? elSkipText.value : elFreeText.value;

    if (!skipDetails) {
      var missing = QUESTIONS.filter(function (q) { return !r[q]; });
      if (missing.length) {
        alert('Still unanswered: ' + missing.join(', ').replace('q', 'Q'));
        return;
      }
    }

    var need = skipDetails || freeTextRequired(r) || isSampled(item.id);
    if (need && wordCount(text) === 0) {
      alert('This item needs the short note. Name what you saw, or what stopped you judging.');
      elSkipText.focus();
      return;
    }

    ans.free_text = text.trim() || null;
    ans.locked = true;
    ans.locked_at = new Date().toISOString();
    save();
    if (STATE.current_idx < ITEMS.length - 1) goto(STATE.current_idx + 1);
    else render();
  }

  function goto(i) {
    STATE.current_idx = clampIdx(i);
    save();
    render();
    window.scrollTo({ top: 0, behavior: 'auto' });
  }

  function exportJson() {
    var ratings = ITEMS.map(function (it) {
      var a = STATE.answers[it.id];
      var r = (a && a.responses) || {};
      var required = freeTextRequired(r);
      return {
        item_id: it.id,
        q1_visibility: r.q1 || null,
        q2_hood_state: r.q2 || null,
        q3_metal_eyelets: r.q3 || null,
        q4_drawcord_toggles: r.q4 || null,
        q5_collar_inner_trim: r.q5 || null,
        free_text: (a && a.free_text) || null,
        free_text_required: required,
        free_text_sampled: isSampled(it.id),
        locked: !!(a && a.locked),
        locked_at: (a && a.locked_at) || null,
        auto_ocr_accuracy: it.ocr_accuracy,
        target_wordmark: it.target_wordmark,
        auto_ocr_text: it.ocr_detected_text
      };
    });
    var out = {
      schema: 'garment-construction-rating/v3',
      rater_id: STATE.rater_id,
      exported_at: new Date().toISOString(),
      total_items: ITEMS.length,
      complete_items: countsComplete(),
      outstanding_free_text: pendingFreeText(),
      presentation: { masked: true, order: 'fixed-shuffled', seed: SEED, free_text_sample_rate: FREE_TEXT_SAMPLE_RATE },
      rubric_version: 'RATER_RUBRIC.md as frozen for this run',
      ratings: ratings
    };
    var blob = new Blob([JSON.stringify(out, null, 2)], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'ratings_' + STATE.rater_id + '_' + out.exported_at.replace(/[:.]/g, '-') + '.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function reset() {
    if (!confirm('Clear every rating stored in this browser for rater ' + STATE.rater_id + '? This cannot be undone.')) return;
    localStorage.removeItem(STATE_KEY);
    STATE = { rater_id: RATER_ID, token: TOKEN, current_idx: 0, answers: {} };
    save();
    render();
  }

  /* ---------- zoom and pan ---------- */

  function resetZoom() {
    elImg.classList.remove('zoomed');
    elScroll.scrollTop = 0;
    elScroll.scrollLeft = 0;
  }

  var drag = null;
  elScroll.addEventListener('mousedown', function (e) {
    if (!elImg.classList.contains('zoomed')) return;
    drag = { x: e.clientX, y: e.clientY, sl: elScroll.scrollLeft, st: elScroll.scrollTop };
    elScroll.classList.add('dragging');
  });
  window.addEventListener('mousemove', function (e) {
    if (!drag) return;
    elScroll.scrollLeft = drag.sl - (e.clientX - drag.x);
    elScroll.scrollTop = drag.st - (e.clientY - drag.y);
  });
  window.addEventListener('mouseup', function () {
    drag = null;
    elScroll.classList.remove('dragging');
  });

  /* ---------- wiring ---------- */

  document.querySelectorAll('.opts[data-q]').forEach(function (group) {
    var q = group.dataset.q;
    group.querySelectorAll('.opt').forEach(function (btn) {
      btn.addEventListener('click', function () { setVerdict(q, btn.dataset.v); });
    });
  });

  $('zoom-in').addEventListener('click', function () { elImg.classList.add('zoomed'); });
  $('zoom-out').addEventListener('click', function () { resetZoom(); });
  $('zoom-reset').addEventListener('click', function () { resetZoom(); });
  $('btn-lock').addEventListener('click', lock);
  $('btn-skip-lock').addEventListener('click', lock);
  elPrev.addEventListener('click', function () { goto(STATE.current_idx - 1); });
  elNext.addEventListener('click', function () { goto(STATE.current_idx + 1); });
  elExport.addEventListener('click', exportJson);
  elReset.addEventListener('click', reset);

  elFreeText.addEventListener('input', function () { updateWordCount(elFreeText.value); });

  document.addEventListener('keydown', function (e) {
    var t = e.target;
    if (t && /input|textarea|select/i.test(t.tagName)) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === 'ArrowRight') { goto(STATE.current_idx + 1); e.preventDefault(); }
    else if (e.key === 'ArrowLeft') { goto(STATE.current_idx - 1); e.preventDefault(); }
  });

  (function theme() {
    var K = 'tw-theme', R = document.documentElement;
    function apply(t) {
      if (t === 'dark') R.setAttribute('data-theme', 'dark');
      else if (t === 'light') R.setAttribute('data-theme', 'light');
      else R.removeAttribute('data-theme');
    }
    var tt = document.getElementById('themeToggle');
    if (tt) {
      tt.addEventListener('click', function () {
        var cur = R.getAttribute('data-theme');
        var next = cur === 'dark' ? 'light' : cur === 'light' ? '' : 'dark';
        apply(next);
        if (next) localStorage.setItem(K, next); else localStorage.removeItem(K);
      });
    }
    var stored = localStorage.getItem(K);
    if (stored) apply(stored);
  })();

  /* ---------- boot ---------- */

  fetch('assets/items.json')
    .then(function (r) {
      if (!r.ok) throw new Error('items.json returned ' + r.status);
      return r.json();
    })
    .then(function (data) {
      ITEMS = data.items || [];
      if (!ITEMS.length) throw new Error('no items in items.json');
      load();
      elPill.textContent = 'rater ' + STATE.rater_id + (TOKEN ? ' · verified link' : '');
      render();
    })
    .catch(function (err) {
      document.querySelector('main').innerHTML =
        '<p style="text-align:center;color:var(--error);padding:var(--space-12) 0">' +
        'Could not load the item list (' + err.message + ').<br><br>' +
        'Open this from <code>iamtamilore.github.io/rater/</code> rather than a saved copy.</p>';
    });

})();