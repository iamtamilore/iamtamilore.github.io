"use strict";

const REPO = "iamtamilore/idea_bank";
const BRANCH = "master";
const API = `https://api.github.com/repos/${REPO}/contents`;
const CLIP_CAP = 25 * 1024 * 1024;
// 25MB = phone-side cap (base64 memory + single PUT reality). The
// idea_bank README's ~60MB policy applies to clips arriving by other
// means (AirDrop / manual copy into inbox/) - two caps, two channels.

// ---------- token storage ----------
function getToken() { return localStorage.getItem("bank_token") || ""; }
function setToken(t) { localStorage.setItem("bank_token", t); }

const tokenInput = document.getElementById("tokenInput");
const tokenStatus = document.getElementById("tokenStatus");
tokenInput.value = getToken();
renderTokenStatus();
function renderTokenStatus() {
  tokenStatus.textContent = getToken()
    ? "token saved on this device only."
    : "no token saved yet - captures will queue until one is set.";
}
document.getElementById("btnSaveToken").addEventListener("click", () => {
  setToken(tokenInput.value.trim());
  renderTokenStatus();
  flushQueue();
});

// ---------- tabs ----------
let activePane = "video";
document.querySelectorAll(".tab").forEach((tb) => {
  tb.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((x) => x.classList.remove("on"));
    tb.classList.add("on");
    activePane = tb.dataset.pane;
    ["video", "photo", "link"].forEach((p) =>
      document.getElementById("pane-" + p).classList.toggle("on", p === activePane)
    );
    paintGate();
  });
});

// ---------- chips ----------
const chosenAspects = new Set();
document.querySelectorAll(".chip").forEach((c) => {
  c.addEventListener("click", () => {
    c.classList.toggle("on");
    c.classList.contains("on") ? chosenAspects.add(c.dataset.a) : chosenAspects.delete(c.dataset.a);
  });
});

// ---------- target reference ----------
let targetFile = null;
const targetToggle = document.getElementById("targetToggle");
const targetPrev = document.getElementById("targetPrev");
const targetInput = document.getElementById("targetInput");
targetToggle.addEventListener("click", () => {
  if (targetFile) {
    targetFile = null;
    targetPrev.classList.remove("on");
    targetToggle.textContent = "+ attach a reference to apply this to (optional)";
  } else {
    targetInput.click();
  }
});
targetInput.addEventListener("change", () => {
  const f = targetInput.files[0];
  if (!f) return;
  targetFile = f;
  document.getElementById("targetImg").src = URL.createObjectURL(f);
  targetPrev.classList.add("on");
  targetToggle.textContent = "- remove reference";
});

// ---------- photo pick ----------
const photoDrop = document.getElementById("photoDrop");
const photoInput = document.getElementById("photoInput");
let photoFile = null;
photoDrop.addEventListener("click", () => photoInput.click());
photoInput.addEventListener("change", () => {
  photoFile = photoInput.files[0];
  if (!photoFile) return;
  photoDrop.classList.add("filled");
  photoDrop.innerHTML = "";
  const img = document.createElement("img");
  img.src = URL.createObjectURL(photoFile);
  photoDrop.appendChild(img);
});

// ---------- video pick + IN/OUT ----------
const videoDrop = document.getElementById("videoDrop");
const videoInput = document.getElementById("videoInput");
const clipCtrl = document.getElementById("clipCtrl");
const rangeRead = document.getElementById("rangeRead");
const grabCanvas = document.getElementById("grabCanvas");
let videoFile = null;
let videoEl = null;
let inSec = null, outSec = null;
let inFrameBlob = null, outFrameBlob = null;

videoDrop.addEventListener("click", () => { if (!videoEl) videoInput.click(); });
videoInput.addEventListener("change", () => {
  videoFile = videoInput.files[0];
  if (!videoFile) return;
  videoDrop.classList.add("filled");
  videoDrop.innerHTML = "";
  videoEl = document.createElement("video");
  videoEl.src = URL.createObjectURL(videoFile);
  videoEl.playsInline = true;
  videoEl.muted = true;
  videoEl.controls = false;
  videoDrop.appendChild(videoEl);
  clipCtrl.style.display = "grid";
  rangeRead.textContent = "play, then tap mark in / mark out";
  paintGate();
});

// ---------- clip ladder + zero-visual gate (SCOPE/03) ----------
function mb(b) { return (b / 1048576).toFixed(1) + " MB"; }
function slugify(s) {
  return String(s).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "")
    .split("-").filter(Boolean).slice(0, 5).join("-") || "capture";
}
function clipSize() { return (videoFile && videoFile.size) || 0; }
function hasRange() { return inSec !== null && outSec !== null; }
function visualOK() {
  if (!videoFile) return { ok: false, why: "pick or record a clip first" };
  if (clipSize() <= CLIP_CAP)
    return { ok: true, why: "clip " + mb(clipSize()) + " - will sync with frames" };
  if (hasRange())
    return { ok: true, why: "clip " + mb(clipSize()) + " - too big to sync, frames carry it" };
  return { ok: false, why: "clip too big to sync (" + mb(clipSize()) + ") - mark IN + OUT, or trim it" };
}
const gateHint = document.getElementById("gateHint");
function paintGate() {
  if (activePane !== "video" || !gateHint) return;
  const v = visualOK();
  gateHint.textContent = "to bank a video: " + v.why;
  gateHint.classList.toggle("ok", v.ok);
}
paintGate();

document.getElementById("btnPlay").addEventListener("click", () => {
  if (!videoEl) return;
  if (videoEl.paused) { videoEl.play(); } else { videoEl.pause(); }
});

async function grabFrame(time) {
  return new Promise((resolve) => {
    const v = document.createElement("video");
    v.src = videoEl.src;
    v.currentTime = time;
    v.muted = true;
    v.addEventListener("seeked", function onSeek() {
      v.removeEventListener("seeked", onSeek);
      grabCanvas.width = v.videoWidth || 640;
      grabCanvas.height = v.videoHeight || 360;
      const ctx = grabCanvas.getContext("2d");
      ctx.drawImage(v, 0, 0, grabCanvas.width, grabCanvas.height);
      grabCanvas.toBlob((blob) => resolve(blob), "image/jpeg", 0.85);
    }, { once: true });
  });
}

document.getElementById("btnIn").addEventListener("click", async () => {
  if (!videoEl) return;
  inSec = Math.round(videoEl.currentTime * 10) / 10;
  outSec = null;
  rangeRead.textContent = `in ${inSec.toFixed(1)}s - watching for out...`;
  inFrameBlob = await grabFrame(inSec);
  paintGate();
});
document.getElementById("btnOut").addEventListener("click", async () => {
  if (!videoEl || inSec === null) return;
  outSec = Math.max(videoEl.currentTime, inSec + 0.5);
  outSec = Math.round(outSec * 10) / 10;
  rangeRead.innerHTML = `range <b>${inSec.toFixed(1)}s to ${outSec.toFixed(1)}s</b>`;
  outFrameBlob = await grabFrame(outSec);
  paintGate();
});

// ---------- id + base64 helpers ----------
function makeId() {
  const now = new Date();
  const p = (n) => String(n).padStart(2, "0");
  const rand = Array.from({ length: 4 }, () => "0123456789abcdef"[Math.floor(Math.random() * 16)]).join("");
  return `${now.getFullYear()}-${p(now.getMonth() + 1)}-${p(now.getDate())}-${p(now.getHours())}${p(now.getMinutes())}-${rand}`;
}
function blobToBase64(blob) {
  return new Promise((resolve, reject) => {
    const r = new FileReader();
    r.onloadend = () => resolve(r.result.split(",")[1]);
    r.onerror = reject;
    r.readAsDataURL(blob);
  });
}

// ---------- IndexedDB queue ----------
let dbPromise = null;
function getDB() {
  if (dbPromise) return dbPromise;
  dbPromise = new Promise((resolve, reject) => {
    const req = indexedDB.open("bank-queue", 1);
    req.onupgradeneeded = () => req.result.createObjectStore("jobs", { keyPath: "id" });
    req.onsuccess = () => resolve(req.result);
    req.onerror = reject;
  });
  return dbPromise;
}
async function queueJob(job) {
  const db = await getDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction("jobs", "readwrite");
    tx.objectStore("jobs").put(job);
    tx.oncomplete = resolve;
    tx.onerror = reject;
  });
}
async function getQueuedJobs() {
  const db = await getDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction("jobs", "readonly");
    const req = tx.objectStore("jobs").getAll();
    req.onsuccess = () => resolve(req.result);
    req.onerror = reject;
  });
}
async function removeJob(id) {
  const db = await getDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction("jobs", "readwrite");
    tx.objectStore("jobs").delete(id);
    tx.oncomplete = resolve;
    tx.onerror = reject;
  });
}

async function commitFile(path, base64Content, message) {
  const token = getToken();
  if (!token) throw new Error("no token");
  const put = (sha) =>
    fetch(`${API}/${path}`, {
      method: "PUT",
      headers: {
        Authorization: `Bearer ${token}`,
        Accept: "application/vnd.github+json",
      },
      body: JSON.stringify(Object.assign({ message, content: base64Content, branch: BRANCH }, sha ? { sha } : {})),
    });
  let res = await put(null);
  if (res.status === 409) {
    // a partial earlier attempt already left this file - fetch its sha and update instead of create
    const g = await fetch(`${API}/${path}?ref=${BRANCH}`, { headers: { Authorization: `Bearer ${token}` } });
    const j = await g.json().catch(() => null);
    if (j && j.sha) res = await put(j.sha);
  }
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`github api ${res.status}: ${body.slice(0, 200)}`);
  }
}

async function runJob(job) {
  for (const f of job.files) {
    await commitFile(f.path, f.base64, `bank: ${job.id}`);
  }
}

// lastFlushError: so the queue banner can show what's actually wrong
// instead of a canned "will send when back online" while online and failing.
let lastFlushError = null;
async function flushQueue() {
  if (!navigator.onLine || !getToken()) return updateQueueBar();
  const jobs = await getQueuedJobs();
  lastFlushError = null;
  // per-job isolation: one bad job must never block the rest of the queue
  for (const job of jobs) {
    try {
      await runJob(job);
      await removeJob(job.id);
    } catch (e) {
      console.warn("flush failed for", job.id, e);
      lastFlushError = (e && e.message) || String(e);
    }
  }
  updateQueueBar();
}
async function updateQueueBar() {
  const jobs = await getQueuedJobs();
  const bar = document.getElementById("queueBar");
  if (jobs.length === 0) {
    bar.classList.remove("show");
    return;
  }
  if (!getToken()) {
    bar.textContent = `${jobs.length} queued - add a token in settings`;
  } else if (!navigator.onLine) {
    bar.textContent = `${jobs.length} queued, will send when back online`;
  } else if (lastFlushError) {
    bar.textContent = `${jobs.length} queued - failing: ${lastFlushError}`;
  } else {
    bar.textContent = `${jobs.length} queued`;
  }
  bar.classList.add("show");
}
window.addEventListener("online", flushQueue);
updateQueueBar();

// ---------- build + submit entry ----------
const statusEl = document.getElementById("status");
function setStatus(msg, cls) {
  statusEl.textContent = msg;
  statusEl.className = cls || "";
}

document.getElementById("btnBank").addEventListener("click", async () => {
  const why = document.getElementById("whyBox").value.trim();
  if (!why) { setStatus("say what you liked about it first - that's the whole point.", "err"); return; }
  const rights = document.getElementById("rightsSwitch").checked ? "real-person" : "clear";
  const aspects = Array.from(chosenAspects);
  const now = new Date();
  const p = (n) => String(n).padStart(2, "0");
  const dateStr = `${now.getFullYear()}-${p(now.getMonth() + 1)}-${p(now.getDate())}`;
  const timeStr = `${p(now.getHours())}${p(now.getMinutes())}`;
  const slug = slugify(why || activePane);
  const base = `inbox/${dateStr}-${timeStr}-${slug}`;

  const capture = {
    captured_at: now.toISOString(),
    captured_from: "pwa - iphone",
    type: activePane,
    slug_hint: slug,
    why,
    aspects,
    clip: null,
    rights,
    target: null,
    origin: null,
    files: [],
  };

  const files = [];

  if (activePane === "video") {
    const v = visualOK();
    if (!v.ok) { setStatus(v.why, "err"); return; }

    if (hasRange()) {
      capture.clip = { in: inSec, out: outSec };
    }

    if (clipSize() <= CLIP_CAP) {
      // clip syncs - motion preserved for Module 8 at use-time
      files.push({ path: `${base}/clip.mp4`, base64: await blobToBase64(videoFile) });
      capture.files.push("clip.mp4");
      if (hasRange()) {
        if (inFrameBlob) { files.push({ path: `${base}/frames/in.jpg`, base64: await blobToBase64(inFrameBlob) }); capture.files.push("frames/in.jpg"); }
        if (outFrameBlob) { files.push({ path: `${base}/frames/out.jpg`, base64: await blobToBase64(outFrameBlob) }); capture.files.push("frames/out.jpg"); }
      } else {
        // auto-grab: one frame at current time so Claude always gets eyes
        const g = await grabFrame(videoEl.currentTime);
        if (g) { files.push({ path: `${base}/frames/grab.jpg`, base64: await blobToBase64(g) }); capture.files.push("frames/grab.jpg"); }
      }
    } else {
      // >25MB, IN+OUT required by the gate above - frames only, deferred
      capture.clip_deferred = true;
      capture.clip_local = { name: videoFile.name, size: videoFile.size };
      if (inFrameBlob) { files.push({ path: `${base}/frames/in.jpg`, base64: await blobToBase64(inFrameBlob) }); capture.files.push("frames/in.jpg"); }
      if (outFrameBlob) { files.push({ path: `${base}/frames/out.jpg`, base64: await blobToBase64(outFrameBlob) }); capture.files.push("frames/out.jpg"); }
    }
  } else if (activePane === "photo") {
    if (!photoFile) { setStatus("pick a photo first.", "err"); return; }
    files.push({ path: `${base}/source.jpg`, base64: await blobToBase64(photoFile) });
    capture.files.push("source.jpg");
  } else if (activePane === "link") {
    const url = document.getElementById("linkUrl").value.trim();
    if (!url) { setStatus("paste a link first.", "err"); return; }
    capture.origin = { app: null, url };
  }

  if (targetFile) {
    capture.target = { intent: document.getElementById("targetIntent").value.trim() || null };
    files.push({ path: `${base}/target.jpg`, base64: await blobToBase64(targetFile) });
    capture.files.push("target.jpg");
  }

  files.push({ path: `${base}/capture.json`, base64: btoa(unescape(encodeURIComponent(JSON.stringify(capture, null, 2)))) });

  const job = { id: makeId(), base, files };

  setStatus("saving...", "");
  try {
    if (navigator.onLine && getToken()) {
      await runJob(job);
      setStatus("banked. queued for next harvest on your machine.", "ok");
    } else {
      await queueJob(job);
      setStatus(getToken() ? "offline - queued, will send when back online." : "no token set - queued until you add one in settings.", "");
      updateQueueBar();
    }
    resetForm();
  } catch (e) {
    console.error(e);
    await queueJob(job);
    setStatus("queued for retry - " + (e && e.message ? e.message : "unknown error"), "err");
    updateQueueBar();
  }
});

function resetForm() {
  document.getElementById("whyBox").value = "";
  document.querySelectorAll(".chip.on").forEach((c) => c.classList.remove("on"));
  chosenAspects.clear();
  document.getElementById("rightsSwitch").checked = false;
  document.getElementById("linkUrl").value = "";
  photoFile = null;
  photoDrop.classList.remove("filled");
  photoDrop.innerHTML = '<span>Tap to pick or take a photo</span><input type="file" id="photoInput" accept="image/*">';
  document.getElementById("photoInput").addEventListener("change", () => {}); // re-bound below on next load
  videoFile = null; videoEl = null; inSec = null; outSec = null; inFrameBlob = null; outFrameBlob = null;
  videoDrop.classList.remove("filled");
  videoDrop.innerHTML = '<span>Tap to pick or record a video</span><input type="file" id="videoInput" accept="video/*">';
  clipCtrl.style.display = "none";
  rangeRead.textContent = "";
  if (gateHint) gateHint.textContent = "";
  targetFile = null;
  targetPrev.classList.remove("on");
  targetToggle.textContent = "+ attach a reference to apply this to (optional)";
  // note: photo/video pickers are recreated above; a page reload keeps things simplest for now
  setTimeout(() => location.reload(), 900);
}

// ---------- service worker ----------
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("sw.js").catch(() => {});
}

flushQueue();
