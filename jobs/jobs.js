/* Jobs tracker logic.
 *
 * The rebuild exists because the old one logged 361 sends and 0 replies. Sending
 * is not an outcome. Every stage below is recorded explicitly, and the funnel at
 * the top is computed from what actually came back rather than from what was
 * pressed.
 *
 * State is localStorage only. The previous version wrote to Firestore with the
 * config checked into a public repository, which meant the write path was
 * readable and writable by anyone who opened the repo, and the data was in
 * Google's project rather than in a file he owns.
 */

(function () {
  'use strict';

  var KEY = 'job-outcomes-v1';
  var CATALOG = window.JOBS_CATALOG || [];

  // Ordered so the funnel counts a rejection as a rejection and a call as progress.
  var STAGES = ['applied', 'silent', 'rejected', 'screening', 'assessment', 'interview', 'offer'];
  var LABEL = {
    applied: 'sent', silent: 'no response', rejected: 'rejected',
    screening: 'screening call', assessment: 'assessment',
    interview: 'interview', offer: 'offer'
  };
  // Anything at or beyond this index means the application got a real response.
  var RESPONSETO = { screening: 1, assessment: 1, interview: 1, offer: 1 };
  var STALE_DAYS = 14;

  var rows = [];
  var filter = 'all';

  var $ = function (id) { return document.getElementById(id); };

  /* ---------- state ---------- */

  function load() {
    try { rows = JSON.parse(localStorage.getItem(KEY) || '[]'); }
    catch (e) { console.warn('could not read tracker', e); rows = []; }
    if (!Array.isArray(rows)) rows = [];
  }

  function save() {
    localStorage.setItem(KEY, JSON.stringify(rows));
  }

  function uid() {
    return 'a' + Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
  }

  /* ---------- dates ---------- */

  function today() { return new Date().toISOString().slice(0, 10); }

  function daysBetween(a, b) {
    if (!a || !b) return null;
    return Math.round((new Date(b) - new Date(a)) / 86400000);
  }

  function isExpired(r) {
    return !!(r.deadline && daysBetween(today(), r.deadline) < 0);
  }

  function daysToDeadline(r) {
    return r.deadline ? daysBetween(today(), r.deadline) : null;
  }

  /* ---------- compute ---------- */

  function reached(r, stage) {
    var i = STAGES.indexOf(r.outcome || 'applied');
    return i >= STAGES.indexOf(stage);
  }

  function compute() {
    var c = { applied: 0, ack: 0, screen: 0, interview: 0, offer: 0, stale: 0, pending: 0 };
    rows.forEach(function (r) {
      c.applied++;
      var o = r.outcome || 'applied';
      if (RESPONSETO[o] || o === 'rejected') c.ack++;
      if (reached(r, 'screening')) c.screen++;
      if (reached(r, 'interview')) c.interview++;
      if (o === 'offer') c.offer++;
      if (o === 'applied' || o === 'silent') {
        var age = daysBetween(r.sent_on, today());
        if (age !== null && age >= STALE_DAYS) c.stale++;
        if (o === 'applied') c.pending++;
      }
    });
    return c;
  }

  function pct(n, d) {
    if (!d) return null;
    return Math.round((n / d) * 1000) / 10;
  }

  function fmt(v) { return v === null ? '—' : v + '%'; }

  function renderFunnel() {
    var c = compute();
    $('f-applied').textContent = c.applied;
    $('f-ack').textContent = c.ack;
    $('f-screen').textContent = c.screen;
    $('f-interview').textContent = c.interview;
    $('f-offer').textContent = c.offer;
    $('r-ack').textContent = fmt(pct(c.ack, c.applied));
    $('r-screen').textContent = fmt(pct(c.screen, c.ack));
    $('r-interview').textContent = fmt(pct(c.interview, c.screen));
    $('r-final').textContent = fmt(pct(c.offer, c.applied));
    $('r-aging').textContent = c.stale;
    $('rates-note').textContent = c.applied < 10
      ? 'A rate on fewer than 10 applications is noise, not a signal. ' + c.stale + ' still awaiting a verdict.'
      : c.stale + ' application' + (c.stale === 1 ? '' : 's') + ' past ' + STALE_DAYS + ' days with nothing back. Chase those or close them out.';
  }

  /* ---------- ledger ---------- */

  function badgeClass(r) {
    var o = r.outcome || 'applied';
    if (o === 'offer') return 'badge-win';
    if (o === 'interview' || o === 'assessment') return 'badge-advance';
    if (o === 'screening') return 'badge-call';
    if (o === 'rejected') return 'badge-reject';
    if (o === 'silent') return 'badge-silent';
    return 'badge-open';
  }

  function matches(r) {
    if (filter === 'all') return true;
    if (filter === 'open') return !r.outcome || r.outcome === 'applied';
    if (filter === 'responded') return !!RESPONSETO[r.outcome];
    if (filter === 'stale') {
      var age = daysBetween(r.sent_on, today());
      return age !== null && age >= STALE_DAYS && (!r.outcome || r.outcome === 'applied' || r.outcome === 'silent');
    }
    return true;
  }

  function renderLedger() {
    var host = $('ledger');
    var list = rows.slice().sort(function (a, b) {
      return (b.sent_on || '').localeCompare(a.sent_on || '');
    }).filter(matches);

    if (!list.length) {
      host.innerHTML = '<div class="empty">' + (rows.length
        ? 'Nothing in this view.'
        : 'Nothing logged yet. Log your first application above.') + '</div>';
      return;
    }

    host.innerHTML = list.map(function (r) {
      var dl = daysToDeadline(r);
      var dlTxt = '';
      if (r.deadline) {
        dlTxt = dl < 0 ? ' deadline passed ' + Math.abs(dl) + 'd ago'
          : ' closes in ' + dl + 'd';
      }
      return '<div class="job" data-id="' + r.id + '">' +
        '<div class="job-top">' +
          '<div><span class="job-co">' + esc(r.company) + '</span>' +
            '<div class="job-ro">' + esc(r.role) + '</div></div>' +
          '<span class="badge ' + badgeClass(r) + '">' + esc(LABEL[r.outcome || 'applied']) + '</span>' +
        '</div>' +
        '<div class="job-meta">' + esc(r.location || 'no location') + ' · ' + esc(r.source || '?') +
          ' · sent ' + esc(r.sent_on) + ' · ' + esc(r.cv || 'ai') + ' CV' + dlTxt + '</div>' +
        (r.why ? '<div class="job-why">' + esc(r.why) + '</div>' : '') +
        (r.outcome_note ? '<div class="job-why">note: ' + esc(r.outcome_note) + '</div>' : '') +
        '<div class="job-actions">' +
          (r.url ? '<a href="' + esc(r.url) + '" target="_blank" rel="noopener">open listing</a>' : '') +
          '<button data-act="outcome">record outcome</button>' +
          '<button data-act="delete">delete</button>' +
        '</div>' +
      '</div>';
    }).join('');
  }

  /* ---------- closing soon ---------- */

  function renderSoon() {
    var soon = rows.filter(function (r) {
      var d = daysToDeadline(r);
      return d !== null && d >= 0 && d <= 21 && (!r.outcome || r.outcome === 'applied');
    }).sort(function (a, b) { return daysToDeadline(a) - daysToDeadline(b); });

    var panel = $('soon-panel');
    if (!soon.length) { panel.hidden = true; return; }
    panel.hidden = false;
    $('soon-list').innerHTML = soon.map(function (r) {
      var d = daysToDeadline(r);
      return '<div class="soon-row">' +
        '<div><strong>' + esc(r.company) + '</strong> · ' + esc(r.role) + '</div>' +
        '<div class="soon-when' + (d > 7 ? ' soon-ok' : '') + '">' + d + ' day' + (d === 1 ? '' : 's') + '</div>' +
      '</div>';
    }).join('');
  }

  /* ---------- fit watch: what the old catalog quietly lost ---------- */

  function renderFit() {
    var logged = {};
    rows.forEach(function (r) { logged[(r.company || '').toLowerCase()] = true; });
    var todayD = today();

    var dead = CATALOG.filter(function (j) {
      if (!j.deadline_date) return false;
      return daysBetween(todayD, j.deadline_date) < 0 && !logged[(j.company || '').toLowerCase()];
    }).sort(function (a, b) { return (b.deadline_date || '').localeCompare(a.deadline_date || ''); });

    var host = $('fit-list');
    if (!dead.length) {
      host.innerHTML = '<div class="empty">Nothing in the saved list has lapsed unnoticed.</div>';
      return;
    }
    host.innerHTML = dead.map(function (j) {
      var d = daysBetween(todayD, j.deadline_date);
      return '<div class="fit-row"><span class="fit-co"><strong>' + esc(j.company) + '</strong> · ' + esc(j.role) + '</span>' +
        '<div class="fit-tag">closed ' + Math.abs(d) + ' day' + (Math.abs(d) === 1 ? '' : 's') + ' ago · never logged · ' +
        esc(j.location || '') + '</div></div>';
    }).join('');
  }

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }


  /* ---------- open roles (researched, with provenance) ---------- */

  var OPEN = window.OPEN_ROLES || { jobs: [], closed_do_not_apply: [] };
  var CONF_LABEL = {
    'seen-on-own-dashboard': 'seen on own dashboard',
    'unverified': 'unverified',
    'rolling-unconfirmed': 'rolling, unconfirmed'
  };

  function renderOpen() {
    var host = $('open-list');
    if (!host) return;
    var todayD = today();
    var list = (OPEN.jobs || []).slice().sort(function (a, b) {
      if (!a.deadline) return 1;
      if (!b.deadline) return -1;
      return a.deadline.localeCompare(b.deadline);
    });

    $('open-count').textContent = list.length + ' open';

    if (!list.length) {
      host.innerHTML = '<div class="empty">No researched roles loaded.</div>';
      return;
    }

    host.innerHTML = list.map(function (j) {
      var d = j.deadline ? daysBetween(todayD, j.deadline) : null;
      var when;
      if (d === null) when = '<span class="soon-when soon-ok">no date found</span>';
      else if (d < 0) when = '<span class="soon-when">closed ' + Math.abs(d) + 'd ago</span>';
      else when = '<span class="soon-when' + (d > 7 ? ' soon-ok' : '') + '">' +
        (d === 0 ? 'closes TODAY' : d + ' day' + (d === 1 ? '' : 's')) + '</span>';

      var fitCls = j.fit === 'high' ? 'badge-advance' : (j.fit === 'medium' ? 'badge-call' : '');
      return '<div class="job">' +
        '<div class="job-top">' +
          '<div><span class="job-co">' + esc(j.company) + '</span>' +
            '<div class="job-ro">' + esc(j.role) + '</div></div>' +
          '<div style="display:flex;gap:6px;flex-wrap:wrap">' +
            (j.already_applied ? '<span class="badge">already applied</span>' : '') +
            (fitCls ? '<span class="badge ' + fitCls + '">' + esc(j.fit) + ' fit</span>' : '') +
            when +
          '</div>' +
        '</div>' +
        '<div class="job-meta">' + esc(j.location || '') + ' · via ' + esc(j.source || '?') +
          ' · deadline ' + esc(j.deadline || 'not found') +
          ' · source of date: <strong>' + esc(CONF_LABEL[j.deadline_conf] || j.deadline_conf || 'unknown') + '</strong></div>' +
        (j.why ? '<div class="job-why">' + esc(j.why) + '</div>' : '') +
        '<div class="job-actions">' +
          (j.url ? '<a href="' + esc(j.url) + '" target="_blank" rel="noopener">open listing</a>' : '') +
          '<button data-act="prefill" data-co="' + esc(j.company) + '" data-ro="' + esc(j.role) + '" data-loc="' + esc(j.location) + '">log this one</button>' +
        '</div>' +
      '</div>';
    }).join('');
  }

  function renderClosed() {
    var host = $('closed-list');
    if (!host) return;
    var list = (OPEN.closed_do_not_apply || []).slice().sort(function (a, b) {
      return (b.closed || '').localeCompare(a.closed || '');
    });
    host.innerHTML = list.map(function (j) {
      return '<div class="fit-row"><span class="fit-co"><strong>' + esc(j.company) + '</strong> · ' + esc(j.role) + '</span>' +
        '<div class="fit-tag">closed ' + esc(j.closed) + '</div></div>';
    }).join('');
  }

  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('button[data-act="prefill"]');
    if (!b) return;
    $('f-company').value = b.dataset.co || '';
    $('f-role').value = b.dataset.ro || '';
    $('f-location').value = b.dataset.loc || '';
    $('f-date').value = today();
    $('log-form').scrollIntoView({ block: 'center' });
    $('f-why').focus();
  });

  /* ---------- events ---------- */

  $('log-form').addEventListener('submit', function (e) {
    e.preventDefault();
    var r = {
      id: uid(),
      company: $('f-company').value.trim(),
      role: $('f-role').value.trim(),
      location: $('f-location').value.trim(),
      source: $('f-source').value,
      url: $('f-url').value.trim(),
      deadline: $('f-deadline').value || '',
      cv: $('f-cv').value,
      sent_on: $('f-date').value || today(),
      why: $('f-why').value.trim(),
      outcome: 'applied',
      outcome_at: today(),
      outcome_note: ''
    };
    rows.unshift(r);
    save();
    renderAll();
    refreshOutcomeSelect();
    var n = $('log-note');
    n.textContent = 'Logged ' + r.company + '. Now record what comes back.';
    $('log-form').reset();
    $('f-date').value = today();
  });

  function setOutcome(id, status, date, note) {
    var r = rows.filter(function (x) { return x.id === id; })[0];
    if (!r) return;
    r.outcome = status;
    r.outcome_at = date || today();
    if (note !== undefined) r.outcome_note = note;
    save();
    renderAll();
  }

  $('o-save').addEventListener('click', function () {
    var id = $('o-app').value;
    var msg = $('o-note-msg');
    if (!id) { msg.textContent = 'Choose an application first.'; return; }
    setOutcome(id, $('o-status').value, $('o-date').value, $('o-note').value.trim());
    msg.textContent = 'Recorded.';
  });

  $('ledger').addEventListener('click', function (e) {
    var btn = e.target.closest('button[data-act]');
    if (!btn) return;
    var id = e.target.closest('.job').dataset.id;
    var row = rows.filter(function (x) { return x.id === id; })[0];
    if (!row) return;
    if (btn.dataset.act === 'delete') {
      if (!confirm('Delete ' + row.company + '?')) return;
      rows = rows.filter(function (x) { return x.id !== id; });
      save(); renderAll(); refreshOutcomeSelect();
    } else if (btn.dataset.act === 'outcome') {
      $('o-app').value = id;
      $('o-status').value = row.outcome || 'applied';
      $('o-date').value = today();
      $('o-note').value = row.outcome_note || '';
      $('o-status').scrollIntoView({ block: 'center' });
    }
  });

  document.querySelectorAll('.filters .fbtn').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.filters .fbtn').forEach(function (x) { x.classList.remove('active'); });
      b.classList.add('active');
      filter = b.dataset.f;
      renderLedger();
    });
  });

  $('btn-csv').addEventListener('click', function () {
    var head = ['company', 'role', 'location', 'source', 'url', 'cv', 'sent_on', 'deadline', 'outcome', 'outcome_at', 'outcome_note', 'why'];
    var q = function (v) { return '"' + String(v == null ? '' : v).replace(/"/g, '""') + '"'; };
    var csv = [head.join(',')].concat(rows.map(function (r) {
      return head.map(function (k) { return q(r[k]); }).join(',');
    })).join('\n');
    dl(new Blob([csv], { type: 'text/csv' }), 'applications.csv');
  });

  $('btn-json').addEventListener('click', function () {
    dl(new Blob([JSON.stringify(rows, null, 2)], { type: 'application/json' }), 'applications.json');
  });

  $('btn-clear').addEventListener('click', function () {
    if (!confirm('Delete every logged application? Export first if you want the record.')) return;
    rows = []; save(); renderAll(); refreshOutcomeSelect();
  });

  function dl(blob, name) {
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = name;
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    URL.revokeObjectURL(a.href);
  }

  function refreshOutcomeSelect() {
    var sel = $('o-app');
    var keep = sel.value;
    sel.innerHTML = '<option value="">choose…</option>' + rows.map(function (r) {
      return '<option value="' + r.id + '">' + esc(r.company) + ' — ' + esc(r.role) +
        ' (' + esc(LABEL[r.outcome || 'applied']) + ')</option>';
    }).join('');
    if (keep) sel.value = keep;
  }

  function renderAll() { renderFunnel(); renderLedger(); renderSoon(); renderFit(); renderOpen(); renderClosed(); refreshOutcomeSelect(); }

  (function theme() {
    var K = 'tw-theme', R = document.documentElement;
    function apply(t) {
      if (t === 'dark') R.setAttribute('data-theme', 'dark');
      else if (t === 'light') R.setAttribute('data-theme', 'light');
      else R.removeAttribute('data-theme');
    }
    var tt = $('themeToggle');
    if (tt) tt.addEventListener('click', function () {
      var cur = R.getAttribute('data-theme');
      var next = cur === 'dark' ? 'light' : cur === 'light' ? '' : 'dark';
      apply(next);
      if (next) localStorage.setItem(K, next); else localStorage.removeItem(K);
    });
    var stored = localStorage.getItem(K);
    if (stored) apply(stored);
  })();

  $('f-date').value = today();
  $('o-date').value = today();
  load();
  renderAll();
})();