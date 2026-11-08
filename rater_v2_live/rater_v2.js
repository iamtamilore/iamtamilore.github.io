/* Rater v2 — Serpentine Zip Geometry
 * Implements the v2 rubric for the serpentine zip panel (brief P1).
 * Q1: Curve count (exact integer: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10+)
 * Q2: Swing measurement (left / right / centre / cannot determine)
 * Q3: Visibility gate (yes / partly / no)
 * Q4: Free text (required when visibility=partly/no, or sampled 20%)
 */

(function () {
  'use strict';

  var params = new URLSearchParams(window.location.search);
  var RATER_ID = params.get('rater') || 'anonymous';
  var TOKEN = params.get('token') || '';
  var STATE_KEY = 'zip-rating/v2:' + RATER_ID;

  var SEED = 20261023;
  var FREE_TEXT_SAMPLE_RATE = 0.20;

  var ITEMS = [];
  var STATE = { rater_id: RATER_ID, token: TOKEN, current_idx: 0, answers: {} };

  var $ = function (id) { return document.getElementById(id); };
  var elImg = $('zip-image');
  var elScroll = $('stage-scroll');
  var elPill = $('rater-pill');
  var elProg = $('progress-pill');
  var elFreePill = $('free-pill');
  var elIdx = $('idx-display');
  var elPrev = $('btn-prev');
  var elNext = $('btn-next');
  var elExport = $('btn-export');
  var elReset = $('btn-reset');
  var elQ4 = $('q4-block');
  var elFreeText = $('free-text');
  var elFreeCount = $('free-count');

  /* ---------- 20% sample for free text ---------- */
  function isSampled(id) {
    var h = 0;
    for (var i = 0; i < id.length; i++) {
      h = ((h << 5) - h + id.charCodeAt(i)) | 0;
    }
    return Math.abs(h) % 100 < FREE_TEXT_SAMPLE_RATE * 100;
  }

  function freeTextRequired(ans) {
    if (!ans || !ans.q3) return false;
    if (ans.q3 === 'no' || ans.q3 === 'partly') return true;
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
      return ['q1', 'q2', 'q3'].every(function (q) { return a.responses[q]; }) && a.locked === true;
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
      STATE.answers[id] = { responses: {}, locked: false, free_text: null };
    }
    return STATE.answers[id];
  }

  function hasAnyAnswers() {
    return Object.keys(STATE.answers || {}).some(function (k) {
      var a = STATE.answers[k];
      return a && a.responses && Object.keys(a.responses).length > 0;
    });
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

    document.title = 'Zip rating v2, item ' + (i + 1) + ' of ' + ITEMS.length;

    var small = 'assets/img-sm/' + item.id + '.jpg';
    var full = 'assets/img/' + item.id + '.png';
    elImg.srcset = small + ' 768w, ' + full + ' 1254w';
    elImg.sizes = '(max-width: 700px) 100vw, 1000px';
    elImg.src = full;
    elImg.alt = 'Serpentine zip crop ' + item.id;
    resetZoom();

    var ans = STATE.answers[item.id];
    var r = (ans && ans.responses) || {};
    var locked = !!(ans && ans.locked);

    // Q1: Curve count
    paint('q1', r.q1);
    // Q2: Swing
    paint('q2', r.q2);
    // Q3: Visibility
    paint('q3', r.q3);
    $('q3-note').hidden = !r.q3 || r.q3 === 'yes';

    var skipDetails = r.q3 === 'no';

    // Free text opens after lock
    var showFree = false;
    if (r.q3 === 'no') {
      showFree = !locked;
    } else if (r.q1 && r.q2 && r.q3) {
      showFree = !locked;
    }
    if (showFree) {
      elQ4.hidden = skipDetails;
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
    if (ans.locked) return;
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

    var missing = ['q1', 'q2', 'q3'].filter(function (q) { return !r[q]; });
    if (missing.length) {
      alert('Still unanswered: Q' + missing.map(function(x){return x[1];}).join(', Q'));
      return;
    }

    var need = freeTextRequired(r) || isSampled(item.id);
    var text = elFreeText.value;
    if (need && wordCount(text) === 0) {
      alert('This item needs the short note. Name what you saw, or what stopped you judging.');
      elFreeText.focus();
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
        original_condition: it.condition,
        original_replicate: it.replicate,
        q1_curve_count: r.q1 || null,
        q2_swing: r.q2 || null,
        q3_visibility: r.q3 || null,
        free_text: (a && a.free_text) || null,
        free_text_required: required,
        free_text_sampled: isSampled(it.id),
        locked: !!(a && a.locked),
        locked_at: (a && a.locked_at) || null,
      };
    });
    var out = {
      schema: 'serpentine-zip-rating/v2',
      rater_id: STATE.rater_id,
      exported_at: new Date().toISOString(),
      total_items: ITEMS.length,
      complete_items: countsComplete(),
      outstanding_free_text: pendingFreeText(),
      presentation: { masked: true, order: 'fixed-shuffled', seed: SEED, free_text_sample_rate: FREE_TEXT_SAMPLE_RATE },
      rubric_version: 'RATER_RUBRIC.md v2 (serpentine zip)',
      ratings: ratings
    };
    var blob = new Blob([JSON.stringify(out, null, 2)], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'zip_ratings_' + STATE.rater_id + '_' + out.exported_at.replace(/[:.]/g, '-') + '.json';
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

  /* ---------- brief screen and start ---------- */
  var elBrief = $('brief');
  var elWork = $('work');
  var elBriefGo = $('brief-go');

  function startRating() {
    if (elBrief) elBrief.hidden = true;
    if (elWork) elWork.hidden = false;
    render();
    window.scrollTo(0, 0);
  }

  if (elBriefGo) {
    elBriefGo.addEventListener('click', startRating);
    elBriefGo.dataset.pendingStart = '1';
  }

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
      var countEls = document.querySelectorAll('[data-item-count]');
      for (var i = 0; i < countEls.length; i++) {
        countEls[i].textContent = String(ITEMS.length);
      }
      document.title = 'Zip rating v2, item 1 of ' + ITEMS.length;
      if (elBriefGo && elBriefGo.dataset.pendingStart === '1' && hasAnyAnswers()) {
        startRating();
      }
      render();
    })
    .catch(function (err) {
      document.querySelector('main').innerHTML =
        '<p style="text-align:center;color:var(--error);padding:var(--space-12) 0">' +
        'Could not load the item list (' + err.message + ').<br><br>' +
        'Open this from the deployed URL rather than a saved copy.</p>';
    });

})();
