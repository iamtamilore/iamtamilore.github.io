"""Generate a study-audio hub page (episode list + sticky player) from a course spec.

Reusable across subjects: add a new dict to COURSES below, run this script,
audio files already sit in assets/audio/<course_id>/weekN.m4a.
"""
from pathlib import Path
import subprocess
import json

ROOT = Path(__file__).resolve().parent

def probe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True
    ).stdout.strip()
    return round(float(out)) if out else 0

COURSES = [
    dict(
        id="eeai",
        title="Engineering & Evaluating AI Systems - H9EEAI",
        audio_dir=ROOT / "audio" / "eeai",
        episodes=[
            dict(id="w1", week=1, title="AI System Basics", file="week1.m4a"),
            dict(id="w2", week=2, title="Designing ML Systems", file="week2.m4a"),
            dict(id="w3", week=3, title="Data Quality & Leakage", file="week3.m4a"),
            dict(id="w4", week=4, title="Architecting AI Systems", file="week4.m4a"),
            dict(id="w5", week=5, title="Serving & Evaluation", file="week5.m4a"),
            dict(id="w6", week=6, title="Complexity & Sensitivity", file="week6.m4a"),
            dict(id="w7", week=7, title="ML Deployment", file="week7.m4a"),
        ],
    ),
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light dark">
<meta name="robots" content="noindex">
<title>{title} - Study</title>
<link rel="stylesheet" href="/assets/study/player.css">
</head>
<body class="study-body">
<div class="study-wrap">
  <div class="study-header">
    <h1>{title}</h1>
    <button class="theme-toggle" id="themeToggle" type="button">Theme</button>
  </div>

  <div class="continue-card">
    <div class="cc-text">
      <div class="cc-label">Continue listening</div>
      <div class="cc-title"></div>
      <div class="cc-sub"></div>
    </div>
    <button class="cc-play" aria-label="Resume">&#9654;</button>
  </div>

  <div class="ep-list"></div>

  <div class="kbd-hint">
    <kbd>Space</kbd> play/pause &nbsp; <kbd>&larr;</kbd> -15s &nbsp; <kbd>&rarr;</kbd> +30s &nbsp;
    <kbd>&uarr;</kbd><kbd>&darr;</kbd> speed &nbsp; <kbd>M</kbd> mark done &nbsp; <kbd>H</kbd> copy link
  </div>
</div>

<div class="player-bar">
  <div class="pb-inner">
    <div class="pb-title"></div>
    <div class="pb-status"></div>
    <div class="pb-row">
      <span class="pb-time left">0:00</span>
      <input class="pb-seek" type="range" min="0" max="100" value="0" step="1">
      <span class="pb-time right">-0:00</span>
    </div>
    <div class="pb-controls">
      <button class="pb-btn pb-back" aria-label="Back 15 seconds">&#8630;15</button>
      <button class="pb-btn pb-play" aria-label="Play">&#9654;</button>
      <button class="pb-btn pb-fwd" aria-label="Forward 30 seconds">30&#8631;</button>
      <button class="pb-speed" type="button">1&times;</button>
      <button class="pb-handoff" type="button">Copy link</button>
    </div>
  </div>
</div>

<div class="toast"></div>

<script src="/assets/study/player.js"></script>
<script>
  document.getElementById("themeToggle").addEventListener("click", function () {{
    var root = document.documentElement;
    var cur = root.dataset.theme === "dark" ? "light"
      : root.dataset.theme === "light" ? "" : "dark";
    if (cur) root.dataset.theme = cur; else delete root.dataset.theme;
    try {{ localStorage.setItem("study-theme", cur); }} catch (e) {{}}
  }});

  new StudyPlayer(document.body, {{
    courseId: "{course_id}",
    courseTitle: {course_title_json},
    episodes: {episodes_json}
  }});
</script>
</body>
</html>
"""

def build_course(course):
    episodes = []
    for ep in course["episodes"]:
        audio_path = course["audio_dir"] / ep["file"]
        dur = probe_duration(audio_path)
        episodes.append({
            "id": ep["id"],
            "week": ep["week"],
            "title": ep["title"],
            "dur": dur,
            "src": "/audio/" + course["id"] + "/" + ep["file"],
        })

    out_dir = ROOT / "study" / course["id"]
    out_dir.mkdir(parents=True, exist_ok=True)
    html = TEMPLATE.format(
        title=course["title"],
        course_id=course["id"],
        course_title_json=json.dumps(course["title"]),
        episodes_json=json.dumps(episodes),
    )
    (out_dir / "index.html").write_text(html)
    print(f"Wrote {out_dir / 'index.html'}  ({len(episodes)} episodes)")

if __name__ == "__main__":
    for course in COURSES:
        build_course(course)
