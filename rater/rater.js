/* Rater UI - pure client-side. No backend.
 *
 * URL parameters:
 *   ?rater=A&token=xyz   - identifies this rater; stored in localStorage after first load
 *
 * State stored in localStorage under key 'rater-state-<rater_id>':
 *   { rater_id, token, current_idx, answers: { item_id: 'correct'|'incorrect'|'skipped' } }
 *
 * Export: downloads a JSON file with all answers + metadata, named after the rater id.
 */

(function() {
    'use strict';

    const PARAMS = new URLSearchParams(window.location.search);
    const RATER_ID = PARAMS.get('rater') || 'A';
    const TOKEN = PARAMS.get('token') || '';

    const STATE_KEY = `rater-state-${RATER_ID}`;
    const ITEMS_URL = 'assets/items.json';

    let ITEMS = [];
    let STATE = {
        rater_id: RATER_ID,
        token: TOKEN,
        current_idx: 0,
        answers: {}
    };

    // ---- DOM refs ----
    const elTitle = document.getElementById('title');
    const elMeta = document.getElementById('meta');
    const elImg = document.getElementById('garment');
    const elOcrAcc = document.getElementById('ocr-accuracy');
    const elOcrText = document.getElementById('ocr-text');
    const elTargetWm = document.getElementById('target-wordmark');
    const elRaterLabel = document.getElementById('rater-label');
    const elProgress = document.getElementById('progress');
    const elIdxDisplay = document.getElementById('idx-display');
    const elBtnCorrect = document.getElementById('btn-correct');
    const elBtnIncorrect = document.getElementById('btn-incorrect');
    const elBtnSkip = document.getElementById('btn-skip');
    const elBtnPrev = document.getElementById('btn-prev');
    const elBtnNext = document.getElementById('btn-next');
    const elBtnExport = document.getElementById('btn-export');
    const elBtnReset = document.getElementById('btn-reset');

    // ---- State ----
    function loadState() {
        try {
            const raw = localStorage.getItem(STATE_KEY);
            if (raw) {
                const saved = JSON.parse(raw);
                STATE.current_idx = saved.current_idx || 0;
                STATE.answers = saved.answers || {};
            }
        } catch (e) {
            console.warn('Failed to load state from localStorage:', e);
        }
    }

    function saveState() {
        try {
            localStorage.setItem(STATE_KEY, JSON.stringify(STATE));
        } catch (e) {
            console.warn('Failed to save state to localStorage:', e);
        }
    }

    function countAnswered() {
        return Object.values(STATE.answers).filter(a => a === 'correct' || a === 'incorrect').length;
    }

    // ---- Rendering ----
    function render() {
        const i = STATE.current_idx;
        if (i < 0) STATE.current_idx = 0;
        if (i >= ITEMS.length) STATE.current_idx = ITEMS.length - 1;

        const item = ITEMS[STATE.current_idx];
        if (!item) return;

        document.title = `Garment OCR Rater — Item ${i + 1}/${ITEMS.length}`;
        elTitle.textContent = `Item ${i + 1} of ${ITEMS.length}`;
        elMeta.textContent = `brief=${item.brief}  ·  condition=${item.condition} (${item.condition_name})  ·  replicate=${String(item.replicate).padStart(2, '0')}`;
        elImg.src = item.image;
        elImg.alt = `${item.brief} condition ${item.condition} replicate ${item.replicate}`;

        // ocr_accuracy may be null in scores.csv for some rows; show as —
        if (item.ocr_accuracy === null || item.ocr_accuracy === undefined) {
            elOcrAcc.textContent = '—';
        } else {
            elOcrAcc.textContent = (item.ocr_accuracy * 100).toFixed(1) + '%';
        }
        elTargetWm.textContent = item.target_wordmark || '—';
        elOcrText.textContent = item.ocr_detected_text || '(no text detected)';

        // judgement state
        const cur = STATE.answers[item.id];
        setJudgementActive(cur);

        // progress + nav
        const done = countAnswered();
        elProgress.textContent = `${done} / ${ITEMS.length} rated`;
        elIdxDisplay.textContent = `${i + 1} / ${ITEMS.length}`;
        elBtnPrev.disabled = (i === 0);
        elBtnNext.disabled = (i === ITEMS.length - 1);
        elBtnExport.disabled = (done === 0);
    }

    function setJudgementActive(value) {
        elBtnCorrect.classList.toggle('selected', value === 'correct');
        elBtnIncorrect.classList.toggle('selected', value === 'incorrect');
        elBtnSkip.classList.toggle('selected', value === 'skipped');
    }

    // ---- Actions ----
    function recordAnswer(verdict) {
        const item = ITEMS[STATE.current_idx];
        if (!item) return;
        if (verdict === null) {
            delete STATE.answers[item.id];
        } else {
            STATE.answers[item.id] = verdict;
        }
        saveState();
        render();
    }

    function goto(idx) {
        STATE.current_idx = idx;
        saveState();
        render();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function downloadJson() {
        const out = {
            rater_id: STATE.rater_id,
            token: STATE.token,
            brief: 'P1',
            exported_at: new Date().toISOString(),
            total_items: ITEMS.length,
            answered: countAnswered(),
            answers: STATE.answers,
            // include the items metadata for traceability
            items_metadata: ITEMS.map(it => ({
                id: it.id,
                condition: it.condition,
                replicate: it.replicate,
                ocr_accuracy: it.ocr_accuracy,
                auto_verdict: STATE.answers[it.id] || null
            }))
        };
        const blob = new Blob([JSON.stringify(out, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `ratings_${STATE.rater_id}_${out.exported_at.replace(/[:.]/g, '-')}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }

    function resetProgress() {
        if (!confirm(`Reset all of rater ${STATE.rater_id}'s progress? This clears localStorage for this rater only.`)) return;
        localStorage.removeItem(STATE_KEY);
        STATE = {
            rater_id: RATER_ID,
            token: TOKEN,
            current_idx: 0,
            answers: {}
        };
        saveState();
        render();
    }

    // ---- Wiring ----
    elBtnCorrect.addEventListener('click', () => recordAnswer('correct'));
    elBtnIncorrect.addEventListener('click', () => recordAnswer('incorrect'));
    elBtnSkip.addEventListener('click', () => recordAnswer('skipped'));

    // Click a selected button to un-rate it
    [elBtnCorrect, elBtnIncorrect].forEach(btn => {
        btn.addEventListener('dblclick', () => recordAnswer(null));
    });

    elBtnPrev.addEventListener('click', () => goto(STATE.current_idx - 1));
    elBtnNext.addEventListener('click', () => goto(STATE.current_idx + 1));
    elBtnExport.addEventListener('click', downloadJson);
    elBtnReset.addEventListener('click', resetProgress);

    document.addEventListener('keydown', (e) => {
        // Don't intercept while typing in inputs (there aren't any here, but be safe)
        if (e.target && /input|textarea/i.test(e.target.tagName)) return;
        if (e.key === 'ArrowRight' || e.key === 'j') goto(STATE.current_idx + 1);
        else if (e.key === 'ArrowLeft' || e.key === 'k') goto(STATE.current_idx - 1);
        else if (e.key === '1' || e.key === 'y') recordAnswer('correct');
        else if (e.key === '2' || e.key === 'n') recordAnswer('incorrect');
        else if (e.key === '3' || e.key === 's') recordAnswer('skipped');
    });

    // ---- Boot ----
    fetch(ITEMS_URL)
        .then(r => {
            if (!r.ok) throw new Error('items.json HTTP ' + r.status);
            return r.json();
        })
        .then(data => {
            ITEMS = data.items || [];
            if (ITEMS.length === 0) {
                document.querySelector('main').innerHTML = '<p style="text-align:center;color:#888;padding:40px">No items loaded.</p>';
                return;
            }
            loadState();
            elRaterLabel.textContent = `Rater: ${RATER_ID}${TOKEN ? ' · token set' : ''}`;
            render();
        })
        .catch(err => {
            document.querySelector('main').innerHTML =
                `<p style="text-align:center;color:#dc3545;padding:40px">Failed to load items.json: ${err.message}<br><br>Check that you opened this from the github.io site root.</p>`;
        });
})();
