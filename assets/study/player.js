(function () {
  "use strict";

  // ---------- theme ----------
  (function () {
    try {
      var t = localStorage.getItem("study-theme");
      if (t) document.documentElement.dataset.theme = t;
    } catch (e) {}
  })();

  function fmt(sec) {
    sec = Math.max(0, Math.floor(sec || 0));
    var m = Math.floor(sec / 60), s = sec % 60;
    var h = Math.floor(m / 60);
    m = m % 60;
    if (h > 0) return h + ":" + String(m).padStart(2, "0") + ":" + String(s).padStart(2, "0");
    return m + ":" + String(s).padStart(2, "0");
  }

  function key(courseId, epId) { return "study:" + courseId + ":" + epId; }

  function loadState(courseId, epId) {
    try {
      var raw = localStorage.getItem(key(courseId, epId));
      return raw ? JSON.parse(raw) : null;
    } catch (e) { return null; }
  }
  function saveState(courseId, epId, state) {
    try { localStorage.setItem(key(courseId, epId), JSON.stringify(state)); } catch (e) {}
  }
  function lastPlayed(courseId, episodes) {
    var best = null;
    episodes.forEach(function (ep) {
      var s = loadState(courseId, ep.id);
      if (s && s.t > 3 && !s.done && (!best || s.upd > best.state.upd)) best = { ep: ep, state: s };
    });
    return best;
  }

  var RATES = [1, 1.25, 1.5, 2];

  function StudyPlayer(root, opts) {
    var courseId = opts.courseId;
    var episodes = opts.episodes; // [{id, week, title, dur, src}]
    var audio = new Audio();
    audio.preload = "metadata";

    var bar = root.querySelector(".player-bar");
    var titleEl = bar.querySelector(".pb-title");
    var statusEl = bar.querySelector(".pb-status");
    var seek = bar.querySelector(".pb-seek");
    var tCur = bar.querySelector(".pb-time.left");
    var tRem = bar.querySelector(".pb-time.right");
    var playBtn = bar.querySelector(".pb-play");
    var back15 = bar.querySelector(".pb-back");
    var fwd30 = bar.querySelector(".pb-fwd");
    var speedBtn = bar.querySelector(".pb-speed");
    var handoffBtn = bar.querySelector(".pb-handoff");
    var toast = root.querySelector(".toast");

    var current = null; // episode object
    var rateIdx = 0;

    function showToast(msg) {
      toast.textContent = msg;
      toast.classList.add("show");
      clearTimeout(showToast._t);
      showToast._t = setTimeout(function () { toast.classList.remove("show"); }, 1600);
    }

    function urlFor(ep, t) {
      var u = new URL(location.href);
      u.hash = "ep=" + ep.id + "&t=" + Math.floor(t || 0);
      return u.toString();
    }

    function updateUrl() {
      if (!current) return;
      history.replaceState(null, "", urlFor(current, audio.currentTime));
    }

    function setMediaSession() {
      if (!("mediaSession" in navigator) || !current) return;
      navigator.mediaSession.metadata = new MediaMetadata({
        title: current.title,
        artist: "Week " + current.week,
        album: opts.courseTitle || "Study"
      });
      navigator.mediaSession.setActionHandler("play", function () { play(); });
      navigator.mediaSession.setActionHandler("pause", function () { pause(); });
      navigator.mediaSession.setActionHandler("seekbackward", function () { skip(-15); });
      navigator.mediaSession.setActionHandler("seekforward", function () { skip(30); });
      navigator.mediaSession.setActionHandler("seekto", function (d) {
        if (d.seekTime != null) audio.currentTime = d.seekTime;
      });
    }

    function renderRows() {
      var listEl = root.querySelector(".ep-list");
      listEl.innerHTML = "";
      episodes.forEach(function (ep) {
        var s = loadState(courseId, ep.id);
        var row = document.createElement("a");
        row.href = "#";
        row.className = "ep-row" + (current && current.id === ep.id ? " active" : "");
        var pct = s && ep.dur ? Math.min(100, (s.t / ep.dur) * 100) : 0;
        var subLine = s && s.done ? "Done"
          : s && s.t > 3 ? "Last at " + fmt(s.t)
          : "Not started";
        row.innerHTML =
          '<div class="ep-top">' +
            '<span class="ep-chip">Wk ' + ep.week + '</span>' +
            '<span class="ep-title">' + ep.title + '</span>' +
            '<span class="ep-dur">' + fmt(ep.dur) + '</span>' +
          '</div>' +
          '<div class="ep-sub">' + subLine + '</div>' +
          '<div class="ep-progress"><i style="width:' + pct + '%"></i></div>';
        row.addEventListener("click", function (e) {
          e.preventDefault();
          loadEpisode(ep, s && !s.done ? s.t : 0);
          play();
        });
        listEl.appendChild(row);
      });
    }

    function renderContinue() {
      var card = root.querySelector(".continue-card");
      var lp = lastPlayed(courseId, episodes);
      if (!lp) { card.classList.remove("show"); return; }
      card.classList.add("show");
      card.querySelector(".cc-title").textContent = "Week " + lp.ep.week + " - " + lp.ep.title;
      card.querySelector(".cc-sub").textContent = "Resume from " + fmt(lp.state.t);
      card.onclick = function () { loadEpisode(lp.ep, lp.state.t); play(); };
    }

    function loadEpisode(ep, atTime) {
      persist(); // flush the outgoing episode's position - setting src won't fire "pause"
      current = ep;
      audio.src = ep.src;
      titleEl.textContent = "Week " + ep.week + " - " + ep.title;
      var savedForThis = loadState(courseId, ep.id);
      var ri = savedForThis ? RATES.indexOf(savedForThis.rate) : -1;
      if (ri > -1) rateIdx = ri;
      audio.playbackRate = RATES[rateIdx];
      speedBtn.textContent = RATES[rateIdx] + "×";
      var applySeek = function () {
        if (atTime && atTime > 0) {
          audio.currentTime = Math.min(atTime, audio.duration || atTime);
          statusEl.textContent = "Resumed from " + fmt(atTime) + " · saved on this device";
        } else {
          statusEl.textContent = "Starting from the beginning";
        }
        audio.removeEventListener("loadedmetadata", applySeek);
      };
      audio.addEventListener("loadedmetadata", applySeek);
      bar.classList.add("show");
      setMediaSession();
      renderRows();
    }

    function play() { audio.play(); }
    function pause() { audio.pause(); }
    function skip(delta) { audio.currentTime = Math.max(0, Math.min((audio.duration || 1e9), audio.currentTime + delta)); }

    function persist() {
      if (!current) return;
      var dur = audio.duration || current.dur || 0;
      var done = dur > 0 && audio.currentTime / dur >= 0.95;
      saveState(courseId, current.id, { t: audio.currentTime, dur: dur, upd: Date.now(), rate: RATES[rateIdx], done: done });
    }

    // ---- events ----
    audio.addEventListener("play", function () { playBtn.textContent = "⏸"; });
    audio.addEventListener("pause", function () { playBtn.textContent = "▶"; persist(); renderRows(); renderContinue(); });
    audio.addEventListener("timeupdate", function () {
      if (!current) return;
      var dur = audio.duration || current.dur || 0;
      seek.max = dur || 0;
      seek.value = audio.currentTime;
      tCur.textContent = fmt(audio.currentTime);
      tRem.textContent = "-" + fmt(Math.max(0, dur - audio.currentTime));
      if (Math.floor(audio.currentTime) % 10 === 0) { persist(); updateUrl(); }
    });
    seek.addEventListener("input", function () { audio.currentTime = Number(seek.value); });
    playBtn.addEventListener("click", function () { audio.paused ? play() : pause(); });
    back15.addEventListener("click", function () { skip(-15); });
    fwd30.addEventListener("click", function () { skip(30); });
    speedBtn.addEventListener("click", function () {
      rateIdx = (rateIdx + 1) % RATES.length;
      audio.playbackRate = RATES[rateIdx];
      speedBtn.textContent = RATES[rateIdx] + "×";
      persist();
    });
    handoffBtn.addEventListener("click", function () {
      if (!current) return;
      updateUrl();
      navigator.clipboard.writeText(location.href).then(function () {
        showToast("Link copied - open it on the other device");
      }).catch(function () {
        showToast(location.href);
      });
    });
    document.addEventListener("visibilitychange", function () { if (document.hidden) persist(); });
    window.addEventListener("pagehide", persist);

    // ---- keyboard shortcuts (desk mode) ----
    document.addEventListener("keydown", function (e) {
      var tag = (document.activeElement && document.activeElement.tagName) || "";
      if (tag === "INPUT" || tag === "TEXTAREA") return;
      if (e.metaKey || e.ctrlKey || e.altKey) return;
      if (!current && e.code !== "KeyH") return;
      switch (e.code) {
        case "Space": e.preventDefault(); audio.paused ? play() : pause(); break;
        case "ArrowLeft": skip(-15); break;
        case "ArrowRight": skip(30); break;
        case "Home": audio.currentTime = 0; break;
        case "ArrowUp": rateIdx = Math.min(RATES.length - 1, rateIdx + 1); audio.playbackRate = RATES[rateIdx]; speedBtn.textContent = RATES[rateIdx] + "×"; break;
        case "ArrowDown": rateIdx = Math.max(0, rateIdx - 1); audio.playbackRate = RATES[rateIdx]; speedBtn.textContent = RATES[rateIdx] + "×"; break;
        case "KeyM":
          if (current) {
            var s = loadState(courseId, current.id) || { t: audio.currentTime, dur: audio.duration };
            s.done = !s.done; s.upd = Date.now();
            saveState(courseId, current.id, s);
            renderRows(); renderContinue();
          }
          break;
        case "KeyH": handoffBtn.click(); break;
        default:
          if (e.code.startsWith("Digit") && audio.duration) {
            var n = Number(e.code.replace("Digit", ""));
            audio.currentTime = (n / 10) * audio.duration;
          }
      }
    });

    // ---- boot: URL hash wins, else last played ----
    (function boot() {
      var m = location.hash.match(/ep=([^&]+)&t=(\d+)/);
      if (m) {
        var ep = episodes.find(function (e) { return e.id === m[1]; });
        if (ep) { loadEpisode(ep, Number(m[2])); renderContinue(); return; }
      }
      renderContinue();
    })();

    renderRows();
  }

  window.StudyPlayer = StudyPlayer;
})();
