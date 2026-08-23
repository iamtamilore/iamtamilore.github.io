// Minimal app-shell cache so the page opens instantly and is installable.
// Data (entries) never gets cached here - that's IndexedDB's job in app.js.
const CACHE = "bank-shell-v3";
const SHELL = ["./", "index.html", "app.js", "manifest.json"];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)));
  self.skipWaiting();
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return; // never intercept GitHub API writes
  // network-first, cache fallback: a hard refresh (or any online load) always
  // gets the real current deploy. cache only covers you when offline. this
  // avoids ever needing another manual CACHE version bump for a content fix.
  e.respondWith(
    fetch(e.request)
      .then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(e.request, copy)).catch(() => {});
        return res;
      })
      .catch(() => caches.match(e.request))
  );
});
