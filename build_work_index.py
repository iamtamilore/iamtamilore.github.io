#!/usr/bin/env python3
"""Build the public-safe work index from the verified engineering inventory.

Source of truth:
  /home/newtazer/Desktop/NCI/2ND/IMAGE VID GEN/research/ca2_submission/cv_build/inventory.json

The public output excludes local paths, internal tool identifiers, prospect records,
signed-in browser details and other private operational data.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = Path("/home/newtazer/Desktop/NCI/2ND/IMAGE VID GEN/research/ca2_submission/cv_build/inventory.json")
OUT_DATA = ROOT / "data" / "work_inventory.json"
OUT_PAGE = ROOT / "work" / "index.html"

CATEGORY_LABELS = {
    "applied_ai": "Applied AI",
    "evaluation_harness": "Evaluation harness",
    "llm_infrastructure": "LLM infrastructure",
    "mcp_integration": "MCP integration",
    "orchestration": "Orchestration",
    "production_pipeline": "Production pipeline",
    "professional": "Professional systems",
    "quality_assurance": "Quality assurance",
    "research": "Research",
}

STATUS = {
    "zenpai_multichannel_episode_pipeline": ("Production", "Episodes, workflow and channels are published."),
    "cron_orchestrator_and_ledger": ("Production", "Scheduled work and outcomes are recorded in an append-only ledger."),
    "posting_quality_gates": ("Partial", "Gates A to D execute in the posting loop. Gate E is defined but is not executed there."),
    "llm_gateway_ask_py": ("Production", "Budget, cache, model routing and spend limits run behind one gateway."),
    "capability_search_index": ("Production", "Measured model findings are indexed for local retrieval."),
    "browser_mcp_automation_engine": ("Internal", "The public version abstracts away signed-in profiles and private browser state."),
    "unified_log_mcp": ("Internal", "The public version abstracts away private cross-client logs and scope contents."),
    "code_search_mcp": ("Production", "The local code index and its rebuilt embedding stack are available to the tool layer."),
    "wikipedia_mcp": ("Production", "A local server exposes the Wikipedia tool surface to the chat clients."),
    "minimax_api_audit": ("Research", "The documentation audit is retained as a dated research snapshot."),
    "brand_consistency_experiment": ("Research", "The confirmatory analysis is frozen separately from the later exploratory corpus."),
    "robustness_analysis": ("Evaluation", "Generation failures were recorded and grouped by cause rather than scored as wins alone."),
    "termsguard_ai": ("Published", "Case study, live demo, source and verification evidence are available."),
    "clinical_rag_records_engine": ("Published", "Case study, source and a limited adversarial retrieval test are available."),
    "imageqa_siamese_gate": ("Published", "Case study, baseline comparison, architecture and source are available."),
    "care_agent_bpmn_triage": ("Published", "Case study, BPMN diagrams, evaluation evidence and source are available."),
    "surge_pricing_rl_vs_ga": ("Unpublished", "The write-up exists. The public case-study route is not published."),
    "huawei_telecom_data_migration": ("Professional", "The public version abstracts client and employer details while preserving the engineering evidence."),
    "outreach_crm_engine": ("Internal", "The public version abstracts prospect records, private audit data and outreach history."),
    "model_bakeoff_harness": ("Evaluation", "A small, dated model bake-off records cost, time and visible defects."),
    "audition_rater_system": ("Evaluation", "Candidates were generated and judged through a multi-model panel."),
    "journey_evidence_log": ("Research", "Longitudinal observations are recorded with a validator."),
    "mohit_ui_image_app": ("Built", "The implementation is verified by source inspection. Runtime behaviour is not quantified here."),
    "episode_qa_gate_family": ("Production", "Brief, claims and frames are checked before the episode is rendered."),
    "mcp_reconnect_watchdog": ("Verified", "A transport failure was used to verify automatic recovery on code-search."),
    "episode_analysis_autopilot": ("Production", "Narration drives beats, shot needs and the analysis plan."),
    "reels_pipeline": ("Production", "Reference clips move from download to frame and JSON exports with status tracking."),
    "mullay_media_pipeline": ("Production", "Image and video jobs are routed by task rather than by one preferred model."),
    "oap_training_app": ("Scaffold", "The application was built end to end but has never been used in a live session."),
    "site_build_generator": ("Published", "This site is generated from the project sources under one design system."),
    "ai_tools_site": ("Published", "A dated text-rendering test records the model, cost and wall time."),
    "media_upscaler_pipeline": ("Incomplete", "The outcome ledger records failures and the output directory is empty."),
    "mobile_media_idea_bank": ("Scaffold", "The tool and convention contract exist. Only a test entry is indexed."),
    "trading_agent_dashboard": ("Prototype", "The dashboard routes models by asset class. It does not establish trading quality."),
    "personal_site_and_links_hub": ("Published", "Contact details, social identities and QR assets are published."),
    "multi_agent_mcp_layer": ("Verified", "Eight servers are configured. Recovery was verified end to end on code-search."),
    "post_render_video_qa_gate": ("Production", "Five checks refuse an episode when one check fails."),
}

DECISION_OVERRIDES = {
    "browser_mcp_automation_engine": "A browser tool broker had to expose a narrow, stable tool surface while keeping signed-in state and private profile data off the public surface.",
    "unified_log_mcp": "Several chat clients needed one searchable event record with explicit scope, so cross-project evidence could be found without losing its provenance.",
    "outreach_crm_engine": "Outreach claims needed a repeatable verification and audit trail so a message could be checked before it left the machine.",
    "huawei_telecom_data_migration": "A telecom data migration needed interface ownership, controlled acceptance tests and a fallback path for failures during cutover.",
    "wikipedia_mcp": "A local tool server had to give every chat client the same typed Wikipedia surface without depending on the host Node runtime.",
}

PROOF = {
    "termsguard_ai": ("Case study", "/p/termsguard/"),
    "clinical_rag_records_engine": ("Case study", "/p/clinical-rag/"),
    "imageqa_siamese_gate": ("Case study", "/p/image-qa/"),
    "care_agent_bpmn_triage": ("Case study", "/p/care-agent/"),
    "zenpai_multichannel_episode_pipeline": ("Gallery", "/products/"),
    "site_build_generator": ("This site", "/"),
    "personal_site_and_links_hub": ("Contact", "/meet/"),
    "model_bakeoff_harness": ("Tools", "/tools/"),
    "audition_rater_system": ("Rater", "/rater/"),
    "journey_evidence_log": ("Provenance", "/provenance/"),
    "mullay_media_pipeline": ("Workflow", "/how/"),
    "episode_analysis_autopilot": ("Workflow", "/products/workflow/"),
    "episode_qa_gate_family": ("Workflow", "/products/workflow/"),
    "post_render_video_qa_gate": ("Workflow", "/products/workflow/"),
    "outreach_crm_engine": ("Internal", "/provenance/"),
}


GLOSSARY = [
    ("System", "A working set of code, rules, data and services that solves one stated problem."),
    ("Project", "A body of work with a problem, a result and an honest limit. A project is not just a folder of files."),
    ("Pipeline", "A fixed sequence of steps. Each step takes the output of the previous step and passes it to the next one."),
    ("Workflow", "The order in which people and tools make decisions. It shows where work is handed over, checked or escalated."),
    ("Script", "A file of instructions that a computer follows. Scripts automate one repeated job."),
    ("Evaluation harness", "A controlled test that runs a model or system under known inputs, records what happened and applies a fixed scoring rule."),
    ("MCP", "Model Context Protocol. A standard that lets an AI application call tools through a typed interface instead of through loose prompts."),
    ("Metric", "A number used to answer a question. The index says what was counted, what was measured and what the number does not prove."),
    ("Baseline", "The simpler approach or earlier version used for comparison. Without a baseline, a result only says that something scored well."),
    ("Failure mode", "The specific way a system can go wrong. Each entry names the failure it was built to catch."),
    ("QA gate", "A quality-assurance check that refuses a result when it does not meet a stated rule."),
    ("API", "A defined interface that one program uses to request work from another program."),
    ("Orchestration", "The layer that decides what runs, when it runs and what happens when it fails."),
    ("RAG", "Retrieval-augmented generation. The system finds relevant source text first, then asks a model to answer using that text."),
    ("CPU inference", "Running a model on the computer's processor instead of a graphics card. It is usually slower, but it is easier to deploy and cheaper to run."),
    ("Seed", "A fixed starting number for a random process. Reusing the seed lets another person reproduce the same run."),
]

METRIC_EXPLANATIONS = {
    "zenpai_multichannel_episode_pipeline": "61 finished episode files were present when this inventory snapshot was taken. The number counts rendered videos. It does not prove that every episode passed the newest quality checks.",
    "cron_orchestrator_and_ledger": "18 scheduled jobs were registered and 18 crontab lines ran them. The ledger records whether each job fired, passed or failed, so a missing run is different from a failed run.",
    "posting_quality_gates": "Five checks were defined for the posting path. Gates A to D run in the posting loop. Gate E exists in the test file but is not executed by that loop.",
    "llm_gateway_ask_py": "23,459 model calls had been written to the ledger when this snapshot was taken. The count includes routed calls and their cost records. It is a historical snapshot, not a current total.",
    "capability_search_index": "280 measured findings were split into searchable chunks of 384 dimensions. A dimension is one number in a vector used to compare the meaning of two pieces of text.",
    "browser_mcp_automation_engine": "The broker exposed four tools to the chat client and kept a larger internal map behind them. The public version hides signed-in profiles and private browser state.",
    "unified_log_mcp": "209 events and 104 searchable vectors had been indexed when this snapshot was taken. Events are timestamped records. Vectors let the system find records by meaning as well as by exact words.",
    "code_search_mcp": "1,104 chunks from 144 files were indexed as 768-dimensional vectors. This lets a chat client search the meaning of code and text across the machine.",
    "wikipedia_mcp": "Five tools were exposed: article search, summary, section outline, random articles and full extract. The server runs locally, but the articles come from the public Wikipedia service.",
    "minimax_api_audit": "117 MiniMax documentation pages were fetched and read into a local corpus. The number counts documentation pages, not models tested and not media generated.",
    "brand_consistency_experiment": "718 scored images came from 9 briefs and 4 conditions in a planned 720-cell design. The images test whether a reference image keeps a generated subject consistent.",
    "robustness_analysis": "544 generation attempts produced 222 scored result cells across four image models. The harness records visible defects so the model can be judged on failures, not only on successful outputs.",
    "termsguard_ai": "102 hand-labelled reference clauses were used to judge new clauses: 52 fair and 50 unfair. These are examples reviewed and labelled by a person, not model output.",
    "clinical_rag_records_engine": "30 adversarial probes were designed to retrieve another patient's note. Scoped retrieval passed all 30 and leaked none. This is a limited synthetic test, not a clinical or privacy certification.",
    "imageqa_siamese_gate": "On 90 sealed test pairs, the original gate reached precision 1.00, recall 0.82, F1 0.90 and ROC-AUC 1.00. Sealed means the test set was not used while choosing the model or threshold.",
    "care_agent_bpmn_triage": "210 labelled tickets were split evenly into five categories, 42 per category. This is the training corpus used to build the ticket router.",
    "surge_pricing_rl_vs_ga": "637,976 ride records remained after metered taxi rides were removed because those records did not contain a quoted price.",
    "huawei_telecom_data_migration": "The CRM extraction was automated in Python and is documented as saving 15 hours of manual work each week. The number comes from the work record, not from a benchmark run on the site.",
    "outreach_crm_engine": "The internal snapshot held 16 prospects, 10 audits, 60 findings, 55 claim checks and 40 outreach events. Prospect details are not published.",
    "model_bakeoff_harness": "Three images were generated at six credits each. The balance moved from 816 to 798 credits, and each image took 66 to 71 seconds. Three images are a small sample, not a model failure rate.",
    "audition_rater_system": "42 candidate images were generated and judged through the panel. The number counts candidates taken through the selection process.",
    "journey_evidence_log": "462 observations were recorded in the longitudinal evidence log. An observation is a dated note tied to a source, not a conclusion pulled from memory.",
    "mohit_ui_image_app": "The Flask application contains 853 lines of code. The line count shows the size of the implementation. It does not measure runtime performance.",
    "episode_qa_gate_family": "The gate checks shot duration between 0.4 and 5.0 seconds, keeps the final shot at or below 4.0 seconds, keeps total shot duration within 0.6 seconds of the audio, and detects duplicate frames with a SHA-256 hash.",
    "mcp_reconnect_watchdog": "A SIGTERM signal stopped the code-search server. The watchdog changed the restart marker, opencode started the server again, and the tools returned. This was verified on one server.",
    "episode_analysis_autopilot": "The important lesson was learned after identical queries left half the shot needs with no usable candidate frames. Each shot need now receives its own character and action queries.",
    "reels_pipeline": "All 577 extracted frames were analysed, all 23 JSON exports were present and 12 generation calls were logged when this snapshot was taken.",
    "mullay_media_pipeline": "The written pipeline contains 475 lines, the image runner 184 lines and the video runner 131 lines. The line counts show documentation and implementation size, not output quality.",
    "oap_training_app": "1,217 examples were seeded and 1,207 cards were due for review. The application was built end to end but has never been used in a live session.",
    "site_build_generator": "182 commits and 26 index files existed on 10 November 2026. A commit is one saved change in the repository history. The index files are the generated pages.",
    "ai_tools_site": "Three text-rendering cases were generated at six credits each. The balance moved from 816 to 798 credits, and each image took 66 to 71 seconds. All three looked correct by eye, but three cases are not a failure rate.",
    "media_upscaler_pipeline": "The outcome ledger has four records. Two are marked FAILED, and the output directory has no files. The system is not a working upscaling pipeline.",
    "mobile_media_idea_bank": "One entry is indexed. Its test identifier shows that the bank is scaffolded but not yet used as a real media library.",
    "trading_agent_dashboard": "36 assets appear in the result set, with SAC, TD3 and PPO routed by asset class. The count describes dashboard contents. It does not establish that the strategies made profitable decisions.",
    "personal_site_and_links_hub": "The links repository contains 38 commits. It publishes contact details, social identities and QR assets.",
    "multi_agent_mcp_layer": "Eight MCP servers are configured across the project: unified log, kie.ai, code search, claude-mem, ask, ComfyUI, Wikipedia and browser. Recovery was verified end to end on code-search.",
    "post_render_video_qa_gate": "The gate runs five checks. If any check fails, it refuses the episode and exits with a non-zero code so a caller cannot treat failure as success.",
}

EXPLANATIONS_SOURCE = ROOT / "data" / "work_explanations.json"

PUBLIC_NAME_OVERRIDES = {
    "browser_mcp_automation_engine": "Browser MCP automation broker with isolated browser sessions",
    "outreach_crm_engine": "Outreach verification and audit database",
}

PUBLIC_STATUS_NOTES = {
    "browser_mcp_automation_engine": "The public version abstracts away private browser sessions and profile data.",
    "outreach_crm_engine": "The public version abstracts away contact records, private audit data and outreach history.",
}


PATH_ROOTS = [
    ("/mnt/2tb/zenpai", "the zenpai episode directory"),
    ("/mnt/2tb/anime_hive_test", "the anime hive episode directory"),
    ("/home/newtazer", "the local working directory"),
]


def redact_paths(value: str) -> str:
    """Replace machine filesystem paths with plain-language locations."""
    for root, replacement in PATH_ROOTS:
        value = value.replace(root, replacement)
    value = re.sub(r"/(?:mnt|home|tmp|var|opt|srv)/[^\s,;)\"']*", "the local working directory", value)
    return value


def public_text(value: str) -> str:
    value = value.replace("signed-in profile", "private browser session").replace("prospect", "contact")
    return redact_paths(value)


def public_system(system: dict, explanation: dict) -> dict:
    status, note = STATUS.get(system["id"], ("Documented", "The system is documented in the verified engineering inventory."))
    proof_label, proof_href = PROOF.get(system["id"], ("Inventory", "/cv/"))
    metrics = []
    for metric in explanation.get("metrics", []):
        clean = {key: public_text(value) if isinstance(value, str) else value for key, value in metric.items()}
        metrics.append(clean)
    return {
        "id": system["id"],
        "name": PUBLIC_NAME_OVERRIDES.get(system["id"], system["name"]),
        "category": system["category"],
        "category_label": CATEGORY_LABELS.get(system["category"], system["category"].replace("_", " ").title()),
        "decision": public_text(explanation.get("plain_problem", DECISION_OVERRIDES.get(system["id"], system["problem"]))),
        "what_it_does": public_text(explanation.get("what_it_does", system["problem"])),
        "mechanism": [public_text(step) for step in explanation.get("mechanism", [])],
        "metrics": metrics,
        "honest_limit": public_text(explanation.get("honest_limit", note)),
        "status": status,
        "status_note": public_text(PUBLIC_STATUS_NOTES.get(system["id"], note)),
        "proof_label": proof_label,
        "proof_href": proof_href,
    }


def card(system: dict) -> str:
    e = html.escape
    mechanism = "".join(f"<li>{e(step)}</li>" for step in system["mechanism"])
    metrics = "".join(
        f"""<div class="metric-explanation">
              <h4>{e(metric['value'])}</h4>
              <p><strong>What was measured:</strong> {e(metric.get('explanation', ''))}</p>
              <p><strong>What it supports:</strong> {e(metric.get('proves', ''))}</p>
              <p><strong>What it does not prove:</strong> {e(metric.get('does_not_prove', ''))}</p>
            </div>"""
        for metric in system["metrics"]
    )
    return f"""      <article class="work-card">
        <div class="work-card-head">
          <span class="eyebrow">{e(system['category_label'])}</span>
          <span class="tag">{e(system['status'])}</span>
        </div>
        <h2>{e(system['name'])}</h2>
        <section>
          <h3>The problem this system addresses</h3>
          <p>{e(system['decision'])}</p>
        </section>
        <section>
          <h3>What the system does</h3>
          <p>{e(system['what_it_does'])}</p>
        </section>
        <section>
          <h3>How it works</h3>
          <ol class="work-mechanism">{mechanism}</ol>
        </section>
        <section>
          <h3>What the measurements mean</h3>
          <div class="work-metrics">{metrics}</div>
        </section>
        <section>
          <h3>The honest limit</h3>
          <p>{e(system['honest_limit'])}</p>
          <p class="work-status"><strong>Current status:</strong> {e(system['status'])}. {e(system['status_note'])}</p>
        </section>
        <a class="cta cta-ghost" href="{e(system['proof_href'])}">{e(system['proof_label'])} &rarr;</a>
      </article>"""


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    explanations = json.loads(EXPLANATIONS_SOURCE.read_text(encoding="utf-8"))["systems"]
    systems = []
    for source_system in data["systems"]:
        explanation = explanations[source_system["id"]]
        public = public_system(source_system, explanation)
        source_values = [metric["value"] for metric in source_system["metrics"]]
        explained_values = [metric["value"] for metric in public["metrics"]]
        if source_values != explained_values:
            if len(source_values) != len(explained_values):
                raise ValueError(f"Metric count changed for {source_system['id']}")
            for metric, source_value in zip(public["metrics"], source_values):
                metric["value"] = public_text(source_value)
        systems.append(public)
    OUT_DATA.parent.mkdir(parents=True, exist_ok=True)
    OUT_DATA.write_text(json.dumps({"source": str(SOURCE), "systems": systems}, indent=2) + "\n", encoding="utf-8")

    cards = "\n".join(card(s) for s in systems)
    glossary = "".join(
        f"<div class=\"glossary-item\"><dt>{html.escape(term)}</dt><dd>{html.escape(definition)}</dd></div>"
        for term, definition in GLOSSARY
    )
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Work index | Taiwo Alabi</title>
<meta name="description" content="A complete, public-safe index of Taiwo Alabi's verified engineering systems, workflows, pipelines and research.">
<script>document.documentElement.setAttribute("data-theme",localStorage.getItem("tw-theme")||"")</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&display=swap">
<link rel="stylesheet" href="/assets/css/design-system.css">
<link rel="stylesheet" href="/assets/css/mark-zero.css">
<style>
  .work-intro {{ max-width: 72ch; }}
  .glossary {{ margin: var(--space-8) 0 var(--space-10); padding: var(--space-5); border: 1px solid var(--border); background: var(--surface); }}
  .glossary h2 {{ margin: var(--space-2) 0 var(--space-4); }}
  .glossary-list {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: var(--space-4); }}
  .glossary-item dt {{ font-weight: 700; margin-bottom: var(--space-1); }}
  .glossary-item dd {{ margin: 0; color: var(--text-3); font-size: var(--text-sm); }}
  .work-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: var(--space-5); margin-top: var(--space-6); }}
  .work-card {{ background: var(--surface); border: 1px solid var(--border); border-left: 3px solid transparent; padding: var(--space-5); transition: border-color var(--motion-duration) var(--motion-ease); }}
  .work-card:hover {{ border-left-color: var(--accent); }}
  .work-card-head {{ display: flex; justify-content: space-between; gap: var(--space-3); align-items: center; }}
  .work-card h2 {{ font-size: var(--text-xl); margin: var(--space-3) 0 var(--space-4); }}
  .work-card h3 {{ font-size: var(--text-base); margin: var(--space-5) 0 var(--space-2); }}
  .work-card h4 {{ font-size: var(--text-sm); margin: var(--space-4) 0 var(--space-2); }}
  .work-card p, .work-card li {{ font-size: var(--text-sm); line-height: 1.65; }}
  .work-card section {{ border-top: 1px solid var(--border); padding-top: var(--space-2); }}
  .work-mechanism {{ padding-left: var(--space-5); }}
  .work-mechanism li {{ margin-bottom: var(--space-3); }}
  .work-metrics {{ display: grid; gap: var(--space-3); }}
  .metric-explanation {{ border-left: 2px solid var(--border); padding-left: var(--space-4); }}
  .metric-explanation p {{ margin: var(--space-1) 0; }}
  .work-status {{ color: var(--text-3); }}
  .work-card .cta {{ display: inline-block; margin-top: var(--space-4); font-size: var(--text-sm); }}
</style>
</head>
<body>
<nav class="util" aria-label="Site">
  <a href="/">index</a>
  <a href="/work/" aria-current="page">work</a>
  <a href="/case-studies/">cases</a>
  <a href="/process/">process</a>
  <a href="/gallery/">gallery</a>
  <a href="/cv/">cv</a>
  <a href="/products/">episodes</a>
  <a href="/how/">how</a>
  <a href="/provenance/">logs</a>
  <a href="/tools/">tools</a>
</nav>
<main class="wrap">
  <header style="padding-top: var(--space-16);">
    <p class="eyebrow">Complete engineering index</p>
    <h1 class="claim-display">Every system starts with the failure it defends against.</h1>
    <p class="work-intro">This index covers {len(systems)} verified systems, workflows, pipelines and research efforts. Private operational details are removed. A system that failed, is unused or remains unvalidated says so here.</p>
  </header>
  <div class="rule"></div>
  <section class="glossary" aria-labelledby="glossary-title">
    <p class="eyebrow">Start here</p>
    <h2 id="glossary-title">The words used in this index</h2>
    <p>The entries below use engineering terms. These definitions explain what each term means here, before the systems begin.</p>
    <dl class="glossary-list">{glossary}</dl>
  </section>
  <section class="work-grid" aria-label="Engineering work">
{cards}
  </section>
  <div class="endcta">
    <a class="cta" href="/cv/">See the Agent Foundations CV</a>
    <a class="cta cta-ghost" href="/provenance/">Inspect the logs</a>
  </div>
</main>
</body>
</html>
"""
    OUT_PAGE.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAGE.write_text(doc, encoding="utf-8")
    print(f"built /work/ with {len(systems)} systems")


if __name__ == "__main__":
    main()
