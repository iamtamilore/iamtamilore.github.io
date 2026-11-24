# Full site content export, all live pages


Generated on 2026-11-24 directly from the built HTML in this repo, which is the source of truth for what's actually live. This is a snapshot: regenerate it with `python3 extract_site_content.py` after any copy change.


---

## PAGE: /

- LINK: [index](/)
- LINK: [work](/work/)
- LINK: [cases](/case-studies/)
- LINK: [process](/process/)
- LINK: [gallery](/gallery/)
- LINK: [cv](/cv/)
- LINK: [skim](/skim/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
- LINK: [episodes](/products/)
- LINK: [channels](/channels/)
- LINK: [jobs](/jobs/)
- LINK: [corpus](/corpus/)
MSc Artificial Intelligence, NCI  ·  graduating January 2027

## I make AI output verifiable before it ships.
- LINK: [Book a 30-minute call](mailto:newalabitaiwo625@gmail.com?subject=30-minute%20call)
One email. I reply with two times that work.
Every system below names the failure it defends against before the thing it adds. That order
      is the argument, and it is the reason this site has a log page instead of a testimonials section.
Stack Python  ·  SQL  ·  FastAPI  ·  Flask  ·  Docker  ·  Kubernetes  ·  PostgreSQL  ·  pgvector  ·  FAISS  ·  RAG  ·  LangGraph  ·  sentence-transformers  ·  scikit-learn  ·  TensorFlow/Keras  ·  LLM evaluation  ·  confidence calibration  ·  Power BI  ·  BPMN 2.0  ·  GDPR data lineage
Browse all 37 systems Case studies See the CV Episodes Workflow blueprint How I build things The raw logs
- LINK: [Browse all 37 systems](/work/)
- LINK: [Case studies](/case-studies/)
- LINK: [See the CV](/cv/)
- LINK: [Episodes](/products/)
- LINK: [Workflow blueprint](/products/blueprint.html)
- LINK: [How I build things](/how/)
- LINK: [The raw logs](/provenance/)

### Four case studies, the failure each one defends against

#### TermsGuard AI
Reads the small print in a privacy policy and flags the unfair parts. A live demo on
          HuggingFace, source on GitHub, and a 12-case regression suite that runs against the
          deployed service (not a notebook). When the verification fails, the page says so
          instead of pretending it ran.
- LINK: [Try it now →](https://newtazer-terms-guard-ai.hf.space)
- LINK: [Case study →](/p/termsguard/)
- LINK: [Weekly corpus of 9 EU + Big Tech policies →](/corpus/)
- LINK: [code](https://github.com/iamtamilore/terms-guard-ai)

#### Care Agent
Two bots that took over two jobs I used to do by hand every morning at Huawei. One
          reads complaints and decides which of five teams they belong to. The other runs the
          process. Below 0.55 confidence it hands the ticket to a human instead of forcing a
          label. 95.2% on the held-out set; the process was mapped in BPMN before any code.
- LINK: [Case study →](/p/care-agent/)
- LINK: [code](https://github.com/iamtamilore/customer-care-automation)

#### Smart Medical Records
A doctor asks in plain English and gets the answer out of that patient's own notes.
          The search filters to one patient before it ranks, so a different patient's note
          cannot surface. Self-hosted on the hospital's own machine, so the data never leaves.
- LINK: [Case study →](/p/clinical-rag/)
- LINK: [code](https://github.com/iamtamilore/agentic_rag_fastapi)

#### Image QA Gate
The moment an AI-generated model stops being the person you asked for, this catches
          it. Built so the agency can ship AI-generated imagery without the wrong face going
          out. A neural net reads the generated image against a locked reference, with a
          cutoff tuned on validation data only and 90 sealed test pairs.
- LINK: [Case study →](/p/image-qa/)
- LINK: [code](https://github.com/iamtamilore/campaign-image-qa)

#### Huawei, Globacom data team
Telecom mediation moves call records to fourteen downstream consumers. The constraint
          was never throughput, it was trust: a bad deploy means a customer is billed twice.
          On a 100k+ row validation pass, found a 14% reporting discrepancy nobody had seen.
- LINK: [On the CV →](/cv/)
Browse all 37 systems The four case studies How the pipelines run The evidence gallery
- LINK: [Browse all 37 systems](/work/)
- LINK: [The four case studies](/case-studies/)
- LINK: [How the pipelines run](/process/)
- LINK: [The evidence gallery](/gallery/)

### The thing nobody else publishes

#### 80 images, four conditions, a frozen rubric
Everyone building on image models shows you the good outputs. So I ran the opposite test.
          Eighty garment images across four generation conditions, presented to human raters in a
          seeded shuffle, with condition and filenames masked and the rubric frozen before anyone
          rated anything. The rubric gates on one question first: is this image clear enough to
          judge at all. If the answer is no, the rest is skipped rather than guessed.
The interesting part is not the score. It is that an automatic OCR score and a human
          judgement disagree often enough to matter, and the only way to find out which one is right
          is to ask a person who cannot see the pipeline.
- LINK: [The instrument →](/tools/)
- LINK: [Every call behind it →](/provenance/)

### 03 Get in touch
I make AI output verifiable before it ships. Every system here names the failure it
    defends against, and every number was measured, not estimated.
Email me 60-second skim CV as PDF
- LINK: [Email me](mailto:newalabitaiwo625@gmail.com)
- LINK: [60-second skim](/skim/)
- LINK: [CV as PDF](/Alabi_Taiwo_CV.pdf)
- LINK: [newalabitaiwo625@gmail.com](mailto:newalabitaiwo625@gmail.com)
- LINK: [linkedin.com/in/tami-alabi](https://www.linkedin.com/in/tami-alabi/)
- LINK: [github.com/iamtamilore](https://github.com/iamtamilore)
- LINK: [+353 87 004 2838](https://wa.me/353870042838?text=Hi%20Taiwo%2C%20I%20saw%20your%20portfolio)
- LINK: [cv](/cv/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
- LINK: [jobs](/jobs/)

---

## PAGE: /cv/

- LINK: [index](/)
- LINK: [work](/work/)
- LINK: [cases](/case-studies/)
- LINK: [process](/process/)
- LINK: [gallery](/gallery/)
- LINK: [cv](/cv/)
- LINK: [episodes](/products/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
- LINK: [Download the Agent Foundations PDF](/Alabi_Taiwo_CV.pdf)
- LINK: [Browse all 37 systems](/work/)
How to read this CV

### Terms used in the application
The CV keeps the exact wording used for applications. The definitions below explain the engineering terms for a reader who has not worked with AI systems.

## Taiwo Alabi
Backend Engineer (Python), AI Engineering: Agent
Foundations
newalabitaiwo625@gmail.com | +353 87 004 2838 |
linkedin.com/in/tami-alabi | github.com/iamtamilore |
iamtamilore.github.io | County Dublin D03 K0Y3, Ireland

### Profile
I build Python backend services that run AI agents, and I write the
evaluations that prove they behave. The system I own is the multi-model
gateway every model call on my machine passes through, with a response
cache, a per-call budget guard, a daily spend ceiling and a detector
that quarantines reasoning burns. Around it I wired eight MCP servers
into one agent layer and added a watchdog that restores a dead server
with no human intervention, plus a scheduling layer for 18 scheduled
jobs that separates a job which fired and failed from one that never
fired. The Smart Medical Records Engine is a clinical assistant on
FastAPI and PostgreSQL with retrieval scoped per patient in the query,
an audit log of every access and name redaction on the stored log. The
Customer Care Process Automation system is an AI routing agent reaching
95.2% routing accuracy on 42 held out tickets, behind a confidence gate
that escalates uncertain tickets to a human instead of guessing. Read the case
study . At Huawei, I automated CRM extraction in Python, validated
100k+ rows of engagement data in SQL, tested a bank’s customer care line
integration interface by interface, and helped design over 440 User
Acceptance Test cases for a data migration covering 400 million daily
call records. MSc Artificial Intelligence (part-time), National College
of Ireland, completing January 2027. Based in Dublin, working remotely
across Irish and UK timezones.
- LINK: [Read the case
study](https://iamtamilore.github.io/p/care-agent/)

### Selected Systems
Multi-model LLM
gateway : Python, sqlite, kie.ai, OpenRouter, NVIDIA NIM
- LINK: [Multi-model LLM
gateway](https://iamtamilore.github.io/work/)
Problem: Every model call was a direct provider call, so there was
no cache, no per-call budget, no spend ceiling, no lineage, and no way
to tell a reasoning burn from a real answer.
Action: I built one chokepoint for every call, with a sha256
response cache keyed on model, messages and parameters, a per-call
budget guard, a daily cumulative ceiling read from the ledger, and a
detector that quarantines a response where completion tokens equal
reasoning tokens and content is empty.
Result: The ledger held 52,215 calls on 23 November 2026, with token
counts, endpoint and cost. The registry separates vendor facts, which a
fetch overwrites, from user facts, which are hand-kept, so a scheduled
catalogue sync cannot silently drop a routing decision.
Limit: The gateway runs on one machine. It has no failover, so a
host outage takes every dependent client with it.
Multi-agent MCP
layer : MCP protocol, Python, Node.js, opencode, Claude
Code
- LINK: [Multi-agent MCP
layer](https://iamtamilore.github.io/work/)
Problem: Each AI client on the machine had its own route to models,
memory, code, the web and the browser, so every client drifted into
different behaviour.
Action: I wired eight MCP servers into one layer, unified-log,
kie-ai, code-search, claude-mem, ask, comfyui, wikipedia and browser,
and the global config now registers nine, including the browser
orchestrator. The gateway is exposed as MCP tools, so an agent in a chat
reaches models through the same budget, cache and ledger as the command
line.
Result: A watchdog tails the transport error log, bumps the affected
server’s restart marker in both config files, and the client respawns
the server, verified end to end on a SIGTERM with no human
intervention.
Limit: The recovery path was exercised against a SIGTERM on one
server. It has not been tested against a hung process or a crashed
dependency.
Cron
orchestration with a verification ledger : bash, Python,
JSONL ledger, systemd
- LINK: [Cron
orchestration with a verification ledger](https://iamtamilore.github.io/work/)
Problem: 18 scheduled jobs could fail without anyone noticing. A job
that fires and fails and a job that never fires leave identical evidence
in a log file.
Action: I routed every crontab line through one runner with a job
name argument and made the orchestrator compare the job registry against
an append-only ledger, writing an explicit per-run outcome so the two
failure modes are distinguishable. It self-heals the one repairable
drift, and notifications fire only on a state change, because a monitor
that repeats a known-bad state every fifteen minutes trains the reader
to ignore it.
Result: 18 jobs under one registry and 3,284 ledger records, with
the exit code visible to anything watching it, 0 healthy and 1 not.
Smart
Medical Records Engine : FastAPI, PostgreSQL with pgvector,
Docker Compose
- LINK: [Smart
Medical Records Engine](https://iamtamilore.github.io/p/clinical-rag/)
Problem: A doctor has ten minutes and a patient history spread
across years of notes, and the one critical line, a past reaction to a
medicine, gets missed.
Action: I built a clinical assistant that answers plain English
questions from that patient’s own records, with the patient_id carried
into the retrieval query so no other patient’s notes can surface, an
audit log of every access, and the patient’s name redacted from the
stored log. Thirty adversarial probes tried to pull another patient’s
note and none got through.
Result: I ran the whole stack, the API, PostgreSQL with 768
dimensional vector search and a self hosted Llama 3.1, across four
Docker Compose services, designed to run inside a hospital network so no
patient record leaves it.
Limit: The data is synthetic and the system has not been tested with
clinicians. Scoping trusts the patient_id on the request, so it stops
one query mixing two patients but not a doctor opening the wrong file.
Redaction covers the name only. Answer quality against a labelled
benchmark is unmeasured.

### Evaluation and Quality
Engineering
Turing, Remote (Dublin) : Apr 2026 to May 2026 AI Quality Analyst, Google Gemini evaluation
programme
Measured the quality of Google Gemini responses on personalization
features.
Wrote prompts to test the models and documented the process for a
Reinforcement Learning from Human Feedback project.
Automated QA Gate for AI Generated Imagery :
TensorFlow/Keras, ResNet50, scikit-learn
Built a gate over frozen ResNet50 Siamese features that reaches
precision 1.00 at F1 0.90 on 90 sealed test pairs, against pixel
difference at F1 0.59 and kNN at F1 0.26. Pixel difference also reaches
precision 1.00, so the gain over that baseline is recall, 0.82 against
0.42.
Tuning the decision threshold from the sigmoid default of 0.5 to
0.4821, on validation data only, recovered all eight missed pairs
without adding a false positive and lifted F1 from 0.90 to 1.00 on the
same 90 sealed pairs.
The advantage is not statistically settled. McNemar’s test against
pixel difference returned p = 0.19, so 90 pairs cannot rule out
luck.
Public write up with ROC curve and confusion matrix. Read the
write-up
- LINK: [Read the
write-up](https://iamtamilore.github.io/p/image-qa/)

### Professional Experience
Huawei Technologies (via RGS), Globacom Telecommunications
department, Lagos
Data Analyst Intern, then Data Specialist : Mar 2025
to Dec 2025, internship extended by the team
Worked with stakeholders to identify data and reporting
requirements, turning raw data into relevant and meaningful
insights.
Profiled and transformed the source data, then managed the Power BI
assets built on it, including reports, dashboards, workspaces and
underlying datasets, and designed scalable data models with advanced
analytics enabled.
Designed and tested the API layer for a cloud integration between
the contact centre platform and a commercial bank’s customer care line,
testing every interface by hand with a command-line tool before it went
near a voice prompt.
Created database structures and tables from 20+ business
requirements, and dashboards in SSRS and Tableau showing 30+ KPIs across
departmental operations.
Wrote Python scripts to automate daily CRM data extraction, cutting
manual reporting time by 15 hours per week, and validated 100k+ rows of
engagement data in SQL, surfacing a 14% discrepancy in monthly active
user metrics.
Worked with the solutions architect on a data migration architecture
for 400 million daily call records, partitioning customer data into
domain specific buckets, and with the test team designed over 440 User
Acceptance Test cases so faults were caught before launch.

### Education
National College of Ireland, Dublin : Jan 2026 to Jan
2027 MSc Artificial Intelligence (part-time) Modules:
Machine Learning, Intelligent Agents and Process Automation, AI Driven
Decision Making, Engineering and Evaluating AI, Natural Language
Processing, Data Governance and Ethics, Database Programming,
Foundations of AI.
Afe Babalola University, Lagos : Sep 2021 to Feb 2025 BSc Computer Science, Second Class Honours, Upper Division
(2.1)

### Technical Skills
Python backend and APIs: Python, FastAPI, Flask,
REST services, asynchronous and background processing, data models,
PostgreSQL, SQL, data modeling, SQLite.
Agent platforms: MCP servers, agent orchestration,
multi agent flows, tool calling, model routing, fallback chains, LLM
gateways, RAG pipelines, LLM evaluation, vector search (pgvector,
FAISS), Claude API, LangGraph, confidence gating and human
escalation.
Testing and operations: pytest patterns, automated
evaluation harnesses, confusion matrix analysis, ROC curves, cron and
scheduler orchestration, append-only ledgers, self-healing watchdogs,
Docker, Docker Compose, Kubernetes, Google Cloud, autoscaling.
Data and governance: Power BI, SSRS, Tableau, GDPR
data cataloging, data lineage, data quality validation, UAT design.
Tools: Git, GitHub, Claude Code, native Linux,
Microsoft 365.

### Certifications
Kubernetes: clusters, pods, auto scaling, memory management,
distributed systems (Udemy, 2026): View
certificate
- LINK: [View
certificate](https://www.udemy.com/certificate/UC-ba3bf541-de9d-4505-9868-d80dfd766b2b/)

### Work Authorisation
Irish Stamp 2 during my MSc: 20 hours per week in term, 40 hours per
week over college holidays. My final examinations are in January 2027.
NCI issues my final results in early 2027, and I am awarded the degree
at the Spring Graduation ceremony in April 2027. From the final results
I can apply for Irish Stamp 1G post-study graduate work permission,
which permits full time employment at 40 hours per week. I am looking
for a role that will sponsor an employment permit.
- LINK: [Email Taiwo](mailto:newalabitaiwo625@gmail.com?subject=Agent%20Foundations%20application)
- LINK: [See the complete work index](/work/)

---

## PAGE: /work/

- LINK: [index](/)
- LINK: [work](/work/)
- LINK: [cases](/case-studies/)
- LINK: [process](/process/)
- LINK: [gallery](/gallery/)
- LINK: [cv](/cv/)
- LINK: [episodes](/products/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
Complete engineering index

## Every system starts with the failure it defends against.
This index covers 37 verified systems, workflows, pipelines and research efforts. Private operational details are removed. A system that failed, is unused or remains unvalidated says so here.
Start here

### The words used in this index
The entries below use engineering terms. These definitions explain what each term means here, before the systems begin.

### Multi-channel short-form video production pipeline

#### The problem this system addresses
Creating short vertical videos for several YouTube channels can become repetitive and inconsistent when people must manually choose images and render every episode. This system prevents manual render-stage work, repeated shots across channels, repeated closing promises, and incorrect image rotation from reaching the finished video.

#### What the system does
This system turns source images into finished vertical short-form videos. A pipeline is a series of automated steps that pass work from one stage to the next. A vision model is an image-reading program that chooses a suitable frame using the written episode instructions, and ffmpeg is a command-line tool that assembles images, sound, timing, and video into a final file. Each channel has separate instructions, voice settings, and image supply rules so the channels can remain distinct.

#### How it works
First, the SOURCE stage gathers possible images for each required shot. A shot is one planned visual moment in a video. Each shot need has its own search questions so different moments do not accidentally receive the same image candidates.
Next, PREFILTER removes or rejects unsuitable source images before selection. This reduces the chance that the selection step spends time considering obviously unusable images.
ROTCHECK corrects or checks image rotation before an image is selected. This order matters because selecting an image before fixing its orientation could cause the wrong version to be chosen.
SELECT gives the written brief and candidate images to qwen3-vl-235b. A model is a trained computer program, and this vision model can inspect images and compare them with the brief. It chooses one frame for each shot need.
CROP converts the selected image into the vertical 9:16 shape required for the short video. VERIFY runs quality checks, called QA gates, before rendering. A QA gate is a rule that must pass before work can continue.
BUILD uses ffmpeg to create the final video. The fixed order is enforced by the main runner script, and the order matters because rendering before checks would allow known problems into the output.

#### What the measurements mean

##### 61 rendered EP_*.mp4 episodes on disk
What was measured: This counted 61 finished video files whose names matched the EP_*.mp4 pattern on the computer. The unit is rendered episode files.
What it supports: It directly supports that 61 episode files existed in the checked location.
What it does not prove: It does not prove that every file was watched, published, error-free, unique, or produced without any human work before the render stage.

##### 6 channel configurations: anime_hive, capital_postmortem, forgotten_fronts, luxury_archive, zenpai
What was measured: This records six channel configurations. A configuration is a set of settings and rules for one channel. The source lists six as the count but names five channel identifiers.
What it supports: It directly supports that the inventory records six channel configurations.
What it does not prove: It does not prove that all six named configurations are currently complete or that the five displayed names account for all six.

##### 149 commits
What was measured: This counted 149 saved changes in the project's Git history. Git is a tool that records versions of files over time, and a commit is one saved group of changes.
What it supports: It directly supports that the repository history contains 149 commits at the measurement point.
What it does not prove: It does not measure video quality, reliability, team size, or the amount of useful work in each commit.

##### select_frames.py uses MODEL = 'qwen3-vl-235b'
What was measured: This records the exact model name configured in the frame selection program. The model is the computer program used to inspect candidate images and choose frames.
What it supports: It directly supports that the selection program is configured to use qwen3-vl-235b.
What it does not prove: It does not prove that every selection was successful, correct, or reviewed by a person.

#### The honest limit
The source does not measure the rate of incorrect selections, duplicate shots, repeated closing promises, failed QA checks, rendering failures, publication success, viewer response, or how many episodes were made for each channel. The source also records six configurations but displays only five names.
Current status: Production. Episodes, workflow and channels are published.
- LINK: [Gallery →](/products/)

### Cron orchestration layer with append-only verification ledger

#### The problem this system addresses
Some scheduled jobs were failing without making it clear whether they had run and failed or had never run at all. This system prevents that specific loss of evidence by recording a separate result for each expected job run.

#### What the system does
A cron job is a task that a computer starts at a planned time, and each of the 18 jobs first passes through a small script that gives the run a known name. An orchestrator is a program that checks whether the expected jobs are running, and a registry is a list of those expected jobs. A ledger is a record that only adds new entries, so this system writes one JSONL record, meaning one JSON object per line, for each observed job outcome. The system can repair a drifted copy of one document, sends a notification only when the overall condition changes, and returns exit code 0 when healthy or 1 when not healthy.

#### How it works
First, every scheduled job is routed through the common runner script with the job name as its first argument. This gives later checks one consistent name for identifying the job.
Next, the runner records whether that named job actually started and what happened during the run. This matters because a failed run must leave different evidence from a run that never started.
The orchestrator then compares the registry, which lists the jobs that should exist, with the append-only ledger, which records what actually happened. Comparing the expected list with the recorded outcomes exposes both missing runs and failed runs.
For each check, the system adds a new per-run result instead of overwriting an older result. Keeping old entries makes the history reviewable and prevents a later status from hiding an earlier failure.
If the document mirror has drifted, the orchestrator repairs that one known repairable problem. It does not claim to repair every possible job failure.
The system compares the current health state with the previous health state before sending a notification. This order prevents repeated messages about the same unchanged problem.
Finally, it returns 0 for a healthy check and 1 for an unhealthy check. This lets another program or service detect the result without reading the detailed ledger.

#### What the measurements mean

##### 18 distinct scheduled jobs, 18 crontab lines
What was measured: There are 18 different named jobs in the schedule and 18 nonempty schedule lines that start those jobs. A crontab is the schedule file used by cron, the service that starts commands at specified times.
What it supports: This directly supports that 18 scheduled jobs and 18 schedule entries were counted.
What it does not prove: It does not prove that all 18 jobs ran successfully, ran on time, or remained healthy.

##### 3,284 append-only ledger records
What was measured: The ledger contains 3,284 recorded lines. Each line is an added record of an observed event or job outcome, and append-only means existing records are not replaced by newer ones.
What it supports: This directly supports that 3,284 ledger records existed when counted.
What it does not prove: It does not prove that every expected run was recorded, that every record is correct, or that the jobs succeeded.

##### registry names: sync_registry, sync_kie_catalog, ingest_findings, ingest_transcripts, verify_llm, termsguard, modelwatch, release_watch, perfume_stock, sync_zenpai_docs, sync_zenpai_repo, cron_orchestrator, outreach_reply_check, outreach_pre_send_gate, zenpai_analytics, zenpai_replenish, zenpai_upload, zenpai_outreach
What was measured: This is the exact list of 18 names stored in the job registry. Each name identifies one expected scheduled job, such as a job that synchronizes information, checks a condition, or performs an upload.
What it supports: This directly supports which 18 job names were present in the registry.
What it does not prove: It does not prove that these jobs ran, completed successfully, produced correct results, or matched every schedule entry.

#### The honest limit
The supplied evidence does not measure job duration, missed-run frequency over a defined period, notification delivery, repair success rates, or the correctness of each job's work. The system self-heals only the stated document-mirror drift, and no broader automatic repair capability is established.
Current status: Production. Scheduled work and outcomes are recorded in an append-only ledger.
- LINK: [Inventory →](/cv/)

### Posting quality gates A to E

#### The problem this system addresses
Several publishing channels could accidentally release posts with repeated subjects, reused closing promises, copied descriptions, weak results, or the wrong speaking style. This system prevents those specific mistakes from reaching a channel when the relevant checks are actually run.

#### What the system does
This system is a set of five named checks, called gates, that inspect a proposed post before publishing. A gate is a rule that can approve or refuse an item. The checks compare performance data, subjects, closing promises, affiliate text, channel voice, and speaking speed against required rules. Four gates are connected to the publishing workflow, while the fifth is defined but not actually enforced in the tested loop.

#### How it works
Gate A checks the known ratio for the brief. A ratio is a measured result compared with a required baseline. If the ratio is below 1.0, the brief is refused because it does not meet the minimum performance rule.
Gate B checks whether the subject has already been used and whether the closing promise has already been spent. A closing promise is the final invitation or expected next action in a post. Refusing repeats protects the publishing schedule from reusing the same idea or ending.
Gate C follows the chain of available closing promises and ranks tied choices by lift. Lift means the measured improvement or response associated with an option. This gate is used to choose among acceptable options rather than simply accepting every option.
Gate D creates the affiliate description when the required information is available. If the description cannot be created, it records the precise reason the affiliate check failed instead of silently allowing the item through.
Gate E checks the channel's assigned expressive voice preset and its words-per-second pacing band. A voice preset is a stored set of speaking-style choices, and words per second measures how quickly narration is spoken. The documented loop for this gate has no assertion body, so it does not currently enforce the check there.
The publishing scripts call Gates A and B during queue creation and call Gate D for affiliate descriptions. The source description does not show a publishing-path call for Gate C or an executed per-channel loop for Gate E.

#### What the measurements mean

##### Gate A at queue_gates.py:142, Gate B at :245, Gate C at :312, Gate D at :287, Gate E at test_gates.py:247
What was measured: The five gate definitions were found at these source locations. The numbers after the colons are source line numbers, not performance measurements.
What it supports: The five gates are named and defined in the codebase.
What it does not prove: It does not prove that every gate runs in production or that every gate passes its checks.

##### Gates A and B invoked from weekly_queue.py:194 and :204, Gate D from :213
What was measured: The publishing queue calls Gate A, Gate B, and Gate D at the listed source locations. The numbers are source line numbers.
What it supports: These three gates are connected to the publishing queue at those locations.
What it does not prove: It does not prove that Gate C or Gate E is executed in the publishing path, or that the connected gates always receive complete data.

##### Gate E is defined but its per-channel loop body is empty in test_gates.py, so it is documented and defined rather than executed there
What was measured: The test file contains the definition and a loop intended to check each channel, but the loop body is empty. Therefore, no per-channel assertion is made by that section.
What it supports: Gate E is not enforcing its documented checks in that test loop.
What it does not prove: It does not prove that no other code elsewhere performs a voice or pacing check.

#### The honest limit
The evidence supports four gates as defined and only Gates A, B, and D as directly invoked from the cited publishing queue. Gate E is defined but has an empty enforcement body in the cited test code. The source does not provide measured pass rates, production failure counts, or proof that Gate C runs in the publishing path.
Current status: Partial. Gates A to D execute in the posting loop. Gate E is defined but is not executed there.
- LINK: [Inventory →](/cv/)

### Multi-model LLM gateway with budget, cache and spend ceiling

#### The problem this system addresses
Different tasks used to contact language models directly, so repeated requests could spend money again and there was no single record of what happened. This system prevents uncontrolled spending, missing records, incorrect routing, and accepting a response that used reasoning effort but returned no usable answer.

#### What the system does
This system is a central program that sends every language model request through one controlled route. A language model is software that reads messages and produces text, while an endpoint is the network service that receives the request. The system chooses a model and service, can use a saved answer instead of making the request again, checks spending limits, records the result, and can retry one known temporary provider failure. It also keeps provider information separate from user-maintained routing decisions so an automatic catalogue update does not replace a deliberate local choice.

#### How it works
First, a caller sends a request to the gateway instead of contacting a model service directly. This order matters because the gateway can apply the same checks and record keeping to every request.
Next, the gateway identifies the requested job, such as research or drafting, and resolves it to a primary model and possibly a fallback model. A primary model is the first model tried, and a fallback is a replacement used when the first route cannot complete the job. This keeps routing decisions in one place.
If the caller supplied a specific model, the gateway uses that model's own provider and endpoint rather than looking it up as if it belonged to another provider. This prevents a valid model override from being sent to the wrong service.
Before contacting a provider, the gateway creates a SHA-256 cache key from the model, messages, and request settings. SHA-256 is a repeatable method for turning those inputs into a fixed fingerprint. If the fingerprint already has an answer, the gateway returns the saved answer, which prevents an identical request from spending money twice.
If there is no cached answer, the gateway estimates the request cost and compares it with the per-call budget. It refuses the request when the estimate is above the allowed amount, before provider usage occurs.
The gateway then reads the day's previous costs from its ledger and checks the daily cumulative cap. A ledger is a local record of events, and a cumulative cap is a maximum total for the day. This check comes after the per-call check because both the individual request and the day's total must be safe.
The gateway sends an approved request to the selected endpoint. For the specified kie.ai Claude route, it retries a temporary provider error with a bounded backoff, meaning it waits for a limited amount of time between a limited number of attempts. This handles a temporary failure without retrying forever.
When a response arrives, the gateway checks for a reasoning burn. This is a response where the completion token count equals the reasoning token count and the visible content is empty. Tokens are pieces of text counted by the model service. The gateway quarantines this result instead of treating it as a successful answer.
Finally, the gateway stores the request outcome, token counts, cost, and endpoint in the ledger, and stores the usable response in the cache when appropriate. Recording happens after the result is known so the record can describe what actually occurred.

#### What the measurements mean

##### 23,459 logged calls
What was measured: This is the exact number of model call records counted in the system's database. A call means one recorded attempt to use a language model service.
What it supports: The database contains 23,459 recorded model call events at the time of measurement.
What it does not prove: It does not prove that all calls were successful, useful, unique, correctly routed, or paid for.

##### 572 media jobs and 40 uploads logged
What was measured: This counts 572 recorded media-generation or media-related jobs and 40 recorded upload events. A media job is a tracked request involving media generation or processing, while an upload is a tracked transfer of data to a service.
What it supports: The database contains those counts of media jobs and uploads.
What it does not prove: It does not prove that the jobs or uploads completed successfully, produced acceptable media, or represent all media activity outside the system.

##### standing daily caps: 8.00 USD total and 3.50 USD per model, set from this machine's own 90-day spend history
What was measured: The configured spending limits allow up to 8.00 USD across all models in one day and up to 3.50 USD for any one model in one day. The limits were chosen using 90 days of spending records from the same machine.
What it supports: The system has these configured daily spending ceilings and that their stated reference was the machine's own 90-day history.
What it does not prove: It does not prove that the limits are sufficient, that every provider reports cost accurately, or that future spending will stay below them.

##### median observed day 0.64 USD, worst day 7.12 USD, measured over 22 active days
What was measured: Across 22 days on which activity occurred, the middle daily spend was 0.64 USD and the highest observed daily spend was 7.12 USD. The median is the middle value after daily amounts are ordered.
What it supports: It describes the recorded spending distribution for those 22 active days.
What it does not prove: It does not describe inactive days, future usage, unrecorded spending, or whether the selected caps are financially appropriate.

##### the restored registry holds 12 top-level keys and 18 routing jobs, and every job resolves: research, draft, boiler, arith, second_opinion, premium_review, the 7 media routes, the 3 verification routes, adjudicate, voice_draft, use_existing and vision
What was measured: The registry is the configuration that stores model and routing information. It contains 12 main entries and 18 named jobs, and each listed job can be converted into a usable model route during the stated check.
What it supports: The stated registry check found 12 top-level keys, 18 routing jobs, and no unresolved job among the named routes.
What it does not prove: It does not prove that every provider endpoint is currently available, that each route produces good answers, or that every fallback works in live conditions.

##### the registry carries 20 OpenRouter models, 15 kie.ai media models, 13 kie.ai Claude models and 3 free NVIDIA NIM models
What was measured: This counts model entries grouped by provider and use category in the registry. OpenRouter, kie.ai, and NVIDIA NIM are separate services that can receive model requests, and the NVIDIA NIM entries are marked free in this registry.
What it supports: The registry contains the stated numbers of model entries in those groups.
What it does not prove: It does not prove that all listed models are reachable, currently offered, free in actual use, or suitable for every task.

##### three live end-to-end calls were made after the restore and all three returned their expected token: the free NVIDIA NIM route returned REGISTRY OK, an OpenRouter slug override returned SLUG OK, and the default kie.ai Claude draft route returned GATEWAY OK
What was measured: Three complete tests sent requests through the gateway and received the expected short confirmation text. One tested the free NVIDIA NIM route, one tested choosing a specific OpenRouter model identifier, and one tested the default kie.ai Claude route for drafting.
What it supports: Those three tested routes completed successfully at that time and returned the expected confirmation values.
What it does not prove: It does not prove broad reliability, quality, capacity under load, correct billing in all cases, or successful operation of every other route.

##### 16 CLI subcommands: call, upload, generate, status, canary, report, grant, mark, recall, search, workflow, speak, source, capability and aliases
What was measured: The command-line interface exposes 16 named command functions, including calling models, uploading data, generating media, viewing status, running checks, reporting, searching, running workflows, speaking text, and inspecting sources or capabilities. A command-line interface is a text-based way to operate a program, and aliases are alternate names for commands.
What it supports: The program's help output lists these 16 command functions or command entries.
What it does not prove: It does not prove that every command works correctly in all situations or that every command is used regularly.

#### The honest limit
The inventory does not report the percentage of requests served from cache, the number of blocked calls, the number of quarantined reasoning burns, cache savings, retry success rates, provider uptime, answer quality, or the accuracy of cost estimates. It also does not show whether every listed route has been tested end to end. The source contains a different call count in a separate resume bullet, but this system's supplied metric is 23,459 logged calls, so the reason for that discrepancy is not measured here.
Current status: Production. Budget, cache, model routing and spend limits run behind one gateway.
- LINK: [Inventory →](/cv/)

### Local capability-search index over measured model findings

#### The problem this system addresses
People previously chose a model for an unclear task from memory, while evidence about past model performance was spread across notes and conversation records. This system prevents an old, dead, or poorly supported model from being selected simply because someone remembered it or found its name in an unrelated file.

#### What the system does
This system searches evidence about what models are good at, rather than merely searching for files. It combines ordinary word matching with semantic matching, which means it can find text that has a similar meaning even when it uses different words. It represents text as an embedding, a list of numbers that summarizes meaning, and compares those lists to rank possible matches. It also records when a model is stale, meaning known to be unavailable or replaced, so that search results can warn against using it.

#### How it works
First, the system gathers four evidence sources: personal notes, session transcripts, verified findings, and the current kie.ai model catalogue. A source is simply the kind of record from which information was taken. Keeping the sources separate helps show where a finding came from.
Next, it divides the source material into 280 smaller chunks. A chunk is a searchable piece of text. Smaller pieces make it easier to connect a specific task to the relevant evidence instead of returning an entire long record.
For each chunk, the system stores ordinary searchable text information for BM25 matching. BM25 is a scoring method that gives higher scores when the important words in a query appear in a relevant chunk, while reducing the importance of words that appear everywhere.
The system also turns each chunk into an embedding with all-MiniLM-L6-v2. An embedding is a list of numbers representing the text's meaning, and this model produces 384 numbers for each chunk. This second method helps find related wording that does not share the exact same terms.
When someone asks which model fits a job, the system compares the request with the indexed chunks using word matching and embedding similarity. It then ranks evidence about model capability rather than returning only matching filenames.
The system checks its stale markers while presenting findings. A stale marker records that a model should not be trusted for routing, along with why it was marked and when. This step matters after retrieval because a strong text match is still unsafe if the matching model is known to be dead.
When the underlying notes or catalogue change, a rebuild command recreates the local index without a network call. Rebuilding after source changes keeps search results aligned with the stored evidence, while avoiding an unnecessary external request.

#### What the measurements mean

##### 280 chunks indexed at 384 dimensions
What was measured: The index contains 280 searchable text chunks, and each chunk's embedding contains 384 numeric dimensions. A dimension is one position in the list of numbers used to represent meaning.
What it supports: The index has the stated number of chunks and the stated embedding size.
What it does not prove: It does not prove that the chunks are complete, accurate, well divided, or that semantic search returns the correct model.

##### source split: 22 own notes, 198 session transcripts, 33 verified findings, 27 live kie.ai catalogue entries
What was measured: The 280 chunks are attributed to 22 personal notes, 198 conversation transcripts, 33 verified findings, and 27 entries from the live kie.ai catalogue. These numbers describe the composition of the indexed material.
What it supports: The index records this stated distribution of chunks across four source categories.
What it does not prove: It does not prove that the sources are independent, current, unbiased, or correct, and it does not measure search precision or recall.

##### 1 model marked stale: qwen3-max-thinking, confirmed dead 404 and replaced by qwen3.8-max-0902
What was measured: One model, qwen3-max-thinking, is marked stale because a 404 response confirmed that it was unavailable. A 404 is a service response meaning the requested resource was not found. The record says it was replaced by qwen3.8-max-0902.
What it supports: The index contains one stale-model record with that name, reason, and replacement.
What it does not prove: It does not prove that the replacement is equivalent, available in the future, or correct for every task that used the old model.

##### live kie.ai catalogue holds 27 models
What was measured: The current captured kie.ai catalogue contains 27 model entries. A catalogue is a list of models reported as available by that service at the time it was captured.
What it supports: The stored catalogue snapshot contains 27 kie.ai model entries.
What it does not prove: It does not prove that all 27 models remain available, that they work, or that the catalogue is complete or current after the measurement.

#### The honest limit
The inventory does not report search precision, recall, F1, ROC-AUC, ranking accuracy, user acceptance, or comparisons against a simpler search method. It does not say how often the index is rebuilt, how quickly catalogue changes are detected, or whether every stale model is found. The source also does not provide a measured evaluation showing that the BM25 and embedding combination selects better models than memory or another routing method.
Current status: Production. Measured model findings are indexed for local retrieval.
- LINK: [Inventory →](/cv/)

### Browser MCP automation broker with isolated browser sessions

#### The problem this system addresses
A computer program needed to control a real web browser, but giving an AI every available browser action would make the list of choices too large. The system prevents the AI from choosing the wrong browser action because it uses a small public tool list and checks web elements through the browser's accessibility tree instead of trusting text read from an image.

#### What the system does
This system is a browser automation broker, meaning a small service that receives simple requests and sends them to a larger browser-control system. The AI sees 4 tools, while the broker can internally select from 44 Playwright actions. Playwright is a library that controls a web browser. The system also keeps 29 browser profiles, where a profile is a separate set of browser settings and stored website data, and uses a pinned Chromium build, which is a fixed browser version, for compatibility. It can run without displaying a browser window, called headless mode, and checks the browser's accessibility tree, which is a structured description of page elements used by assistive technology, before clicking.

#### How it works
First, the AI receives only 4 broker tools instead of the full set of 44 browser actions. This keeps the choice list small and reduces the chance that the AI selects an unsuitable low-level action.
Next, the broker translates the selected request into one of the 44 internal Playwright actions. Playwright is the software library that performs actions such as opening pages, clicking, typing, and uploading files.
The browser runs with a fixed Chromium build. Chromium is the browser engine, and keeping its version fixed matters because changing the browser version can make stored browser data unreadable.
When the system needs to identify a page element, it reads the accessibility tree first. This tree gives each usable element a structured identity, so the system can click the identified element rather than clicking based only on words recognized from a screenshot.
Before using a paid model to interpret a page, the system performs free, repeatable checks first. This observation ladder matters because simple checks can solve easy cases without spending money or adding uncertainty.
The browser can run in headless mode, meaning no visible browser window is drawn. This reduces memory use when a person does not need to watch the browser.

#### What the measurements mean

##### 4 exposed broker tools over a 44-entry internal TOOL_MAP
What was measured: The broker presents 4 tools to the AI and has an internal map containing 44 browser actions. A tool is a callable operation, and the internal map connects a requested operation to the code that performs it.
What it supports: This directly supports that the public interface is smaller than the internal browser capability.
What it does not prove: It does not prove that all 44 actions work correctly, that the AI chooses correctly, or that the system is fast in real workloads.

##### 29 private browser sessions on disk
What was measured: There are 29 browser profiles stored on the computer. A profile is a separate collection of browser data and settings.
What it supports: This directly supports that 29 profiles were present in the measured storage location.
What it does not prove: It does not prove that every profile is usable, current, or tested.

##### headed 1,528 MB RSS across 14 processes against headless 1,186 MB across 12, a 342 MB saving
What was measured: The visible-browser test used 1,528 megabytes of RSS across 14 processes, while the no-window test used 1,186 megabytes across 12 processes. RSS means resident set size, or the amount of computer memory currently held by those processes. The difference between the two measurements was 342 megabytes.
What it supports: This directly supports that headless mode used 342 MB less memory in that measured comparison.
What it does not prove: It does not prove the same saving for different pages, workloads, browser sessions, or numbers of profiles.

##### 5.4 GB of profiles on disk
What was measured: The stored browser profiles occupied 5.4 gigabytes of disk space. Disk space is long-term storage, not the same thing as active memory use.
What it supports: This directly supports the measured storage size of the profiles.
What it does not prove: It does not prove how much of that data is needed, how quickly it can be read, or how much memory the profiles use while running.

#### The honest limit
The inventory does not measure task success rate, click accuracy, upload completion rate, browser startup time, or failures across real websites. It also does not show whether all 29 profiles remain usable or whether the memory comparison holds under active workloads.
Current status: Internal. The public version abstracts away private browser sessions and profile data.
- LINK: [Inventory →](/cv/)

### Unified scoped event log and vector index across chat clients

#### The problem this system addresses
Different chat programs stored their records separately, so a decision made in one program was difficult to find in another. The system prevents cross-project results from being mistaken for current-project evidence by attaching a scope label and applying scope filtering in the database.

#### What the system does
This system stores events, which are records of actions or messages, in one append-only database, meaning new records are added without rewriting old records. It also stores searchable numerical representations called vectors, which allow related text to be found by meaning rather than exact wording. Each record has a scope, meaning a label for the project or system it belongs to. Five tools are available to chat clients, while three maintenance operations are kept in a local command-line program, which is a text-based tool used by an operator.

#### How it works
First, each client sends an event to the shared event store. An event is a record such as a tool call, decision, or message, and the shared store prevents each client from keeping an isolated history.
Next, the event receives a scope label. A scope identifies the project or broader area that the event belongs to.
The database applies scope filtering before returning results. This order matters because filtering in the database is more dependable than asking a language model to ignore unrelated results after they have already been retrieved.
The system also creates vectors for selected text. A vector is a list of numbers that represents the meaning or characteristics of text, allowing a similarity search to find related wording.
A watcher service drains the capture queue, which is a waiting list of events. A separate vector worker creates embeddings, meaning numerical text representations, so recording events and calculating search data do not block each other.
The five normal tools remain available through MCP, which is a standard way for an AI client to call external tools. Three maintenance tools stay in the local command-line program because registering them permanently would add unnecessary tool descriptions to every request.
Search results include their source scope, including when a search crosses scopes. This makes the origin visible instead of hiding it.

#### What the measurements mean

##### 209 events and 104 vectors
What was measured: The event database contained 209 event records, and the vector database contained 104 vector records. An event is a stored occurrence, while a vector is a numerical representation used for similarity search.
What it supports: This directly supports the recorded counts in the two databases at measurement time.
What it does not prove: It does not prove that every event has a vector, that the vectors are accurate, or that searches return the right results.

##### 4 scopes: ca2_submission, practicum-research, system-wide, zenpai-pipeline
What was measured: The system registered 4 scope labels: ca2_submission, practicum-research, system-wide, and zenpai-pipeline. A scope label identifies the project or area associated with a record.
What it supports: This directly supports that four scope names were configured.
What it does not prove: It does not prove that users always assign the correct scope or that scope boundaries are complete.

##### 5 registered tools: log_event, search_log, search_memory, search_all, vector_search
What was measured: The MCP interface registered 5 callable tools with these names. The tools record events, search stored logs, search memory, search across scopes, and search using vector similarity.
What it supports: This directly supports the number and names of tools exposed through MCP.
What it does not prove: It does not prove that every tool is reliable, fast, or used by clients.

##### maintenance CLI exposes 3 tools kept out of the MCP protocol: index_vectors, import_existing_logs, log_stats
What was measured: A local command-line program provides 3 maintenance operations named index_vectors, import_existing_logs, and log_stats. They are not registered as MCP tools, so they do not appear in the normal AI tool list.
What it supports: This directly supports that three maintenance operations were kept outside the MCP interface.
What it does not prove: It does not prove that the maintenance operations run automatically or that their outputs are correct.

#### The honest limit
The inventory does not measure search precision, recall, response time, duplicate rate, deletion behavior, or whether all client events are captured. It also does not establish that the 104 vectors cover all 209 events.
Current status: Internal. The public version abstracts away private cross-client logs and scope contents.
- LINK: [Inventory →](/cv/)

### Local code-search MCP with a rebuilt embedding stack

#### The problem this system addresses
A code-search service stopped connecting because its software took too long to start and one search library was incompatible with the computer's graphics software. The system prevents silent empty search results by pinning compatible dependencies and using a smaller graphics-card batch size.

#### What the system does
This system searches source code by converting code chunks into vectors and comparing them with a FAISS index. FAISS is a library for fast similarity search, and an index is a data structure that organizes searchable vectors. The index uses 768 numerical dimensions, meaning each code chunk is represented by 768 numbers, and uses IndexFlatIP, which compares vectors using inner product similarity. The system uses EmbeddingGemma 300M, a 300-million-parameter model that turns text into vectors, on a graphics processor. Its software versions are pinned, meaning fixed to tested ranges, and the searchable index is stored outside the Python environment so rebuilding the environment does not delete it.

#### How it works
First, the system pins the main software versions. A dependency is a library required by another program, and version pinning prevents an automatic update from changing behavior unexpectedly.
Next, it uses the CPU version of FAISS at 1.9.0.post1. FAISS is the search library, and the CPU version avoids relying on an incompatible graphics-specific wheel for the index operation.
The codebase is divided into chunks. A chunk is a smaller section of a file that can be represented and searched independently.
EmbeddingGemma 300M converts each chunk into a vector with 768 dimensions. The model must create these vectors before similarity search can work.
The model processes 4 chunks at a time on the graphics processor. A batch is the group processed in one operation, and the smaller batch avoids exhausting the available graphics memory.
The vectors are placed in an IndexFlatIP index. IndexFlatIP compares a query vector with stored vectors using inner product, a mathematical similarity score.
When a user searches, the query is converted into the same kind of vector and compared with the stored vectors. Using the same representation for both sides matters because otherwise the similarity scores would not be meaningful.
The index is stored outside the software environment. This means rebuilding the environment can replace libraries without rebuilding the entire searchable data set.

#### What the measurements mean

##### 1,104 chunks across 144 files at 768 dimensions, IndexFlatIP
What was measured: The index contained 1,104 code chunks taken from 144 files. Each chunk was represented by a vector with 768 numbers, and the index type was IndexFlatIP.
What it supports: This directly supports the size, file coverage, vector dimension, and index type recorded for the code index.
What it does not prove: It does not prove that the chunks are complete, that search results are relevant, or that the index is up to date.

##### 3 indexed projects
What was measured: The code-search service reported 3 projects as indexed. A project is a separate codebase or collection of files included in search.
What it supports: This directly supports that three projects were registered in the search service.
What it does not prove: It does not prove that every file in each project was indexed or that searches work equally well across them.

##### cold import reduced from 81 to 88 seconds for torch and over 240 seconds hang for sentence-transformers, down to 1.0 and 3.2 seconds after the pin set
What was measured: Before the dependency changes, importing torch took a measured range from 81 to 88 seconds, and importing sentence-transformers hung for more than 240 seconds. After the version pins, the corresponding import times were 1.0 seconds and 3.2 seconds. A cold import is the first loading of a library when it is not already loaded in the process.
What it supports: This directly supports that the measured import times improved after the dependency pin set.
What it does not prove: It does not prove total service latency, search quality, or performance on other machines.

##### full MCP server reaches its first handler in 3.6 seconds and completes all imports in 9.6 seconds
What was measured: The complete MCP server reached its first request-handling function in 3.6 seconds and finished loading all imports in 9.6 seconds. An import is the step where a program loads a library and its code.
What it supports: This directly supports the measured startup milestones for the server.
What it does not prove: It does not prove that searches finish quickly, that startup is stable after updates, or that all requests succeed.

#### The honest limit
The inventory does not report search precision, recall, F1, ROC-AUC, query latency, reindexing time, or index freshness. It also does not measure how often the former silent empty-result failure occurred after the fix.
Current status: Production. The local code index and its rebuilt embedding stack are available to the tool layer.
- LINK: [Inventory →](/cv/)

### Wikipedia MCP server on a private Node runtime

#### The problem this system addresses
The system needed a local way to look up encyclopedia information through typed tools, where typed means each tool has a defined purpose and input shape. The system prevents failures caused by using the wrong Node version or repeatedly downloading a large package dependency set.

#### What the system does
This system is a local server that receives requests through a text connection and calls Wikipedia's public web services. It exposes 5 tools for searching articles, getting summaries, listing sections, selecting random articles, and retrieving extracts. Node 22.11 is a JavaScript runtime, meaning software that runs JavaScript programs, and it is used instead of the older system runtime. The package and its required supporting packages were copied from a successful installation so the setup did not need to download the full dependency collection again.

#### How it works
First, the server starts with the private Node 22.11 runtime. A runtime is the program that executes JavaScript, and using the intended version prevents an incompatible loader from being selected.
Next, the server loads the Wikipedia package and its supporting packages. Supporting packages are libraries that the main package needs in order to run.
The server communicates with Wikipedia through its web APIs. An API is a defined way for one program to request data from another program.
Each request is matched to one of the 5 typed tools. The fixed tool definitions tell the client what each operation does and what kind of input it accepts.
The selected tool calls either the MediaWiki Action API or the MediaWiki REST v1 API. These are two public interfaces provided by Wikipedia's software for retrieving article data.
The server returns the result to the calling AI client over a local standard-input and standard-output connection. This connection uses text sent into the process and text returned from it.

#### What the measurements mean

##### 5 tools: search_wikipedia, get_article_summary, get_article_sections, get_random_articles, get_article_extract
What was measured: The server exposes 5 tools with the listed names. Each tool represents one kind of Wikipedia lookup operation.
What it supports: This directly supports the number and names of the tools available from the local server.
What it does not prove: It does not prove that the tools return correct results for every query or remain compatible with future Wikipedia changes.

##### package version 0.1.2
What was measured: The installed Wikipedia package reported version 0.1.2. A package version identifies a particular release of the software.
What it supports: This directly supports the reported package release.
What it does not prove: It does not prove that the package is the newest release, secure, or fully tested.

##### 0 credits per call
What was measured: The measured cost for each tool call was 0 credits. A credit is a usage unit charged by a service, so this means no such usage unit was charged in the stated setup.
What it supports: This directly supports the reported credit cost per call.
What it does not prove: It does not prove that network access, computer resources, or future service changes will have no cost.

#### The honest limit
The inventory does not measure response time, uptime, Wikipedia data freshness, failed requests, rate-limit behavior, or factual accuracy of returned articles. It also does not validate every tool against every type of query.
Current status: Production. A local server exposes the Wikipedia tool surface to the chat clients.
- LINK: [Inventory →](/cv/)

### Live MiniMax API documentation and pricing audit

#### The problem this system addresses
People assumed that every MiniMax API endpoint had the same control for changing how much reasoning the model uses, and they also assumed the pricing page explained that control. This audit prevents incorrect integration instructions, unsupported pricing claims, and failed API requests caused by using the wrong setting or trying to disable reasoning in an unsupported way.

#### What the system does
This system reads the vendor's live documentation instead of relying on memory or older examples. It checks every documentation link to see whether the page still exists. It compares the reasoning setting across three API connection styles, called protocols, and tests real requests to see what the service accepts. It records the results in an audit document and publishes a short public explanation.

#### How it works
First, fetch the vendor's markdown documentation list. Markdown is plain text with simple formatting, so it can be read and searched consistently without depending on how a web page looks in a browser.
Next, fetch all 117 linked documentation pages and save the text locally for inspection. Reading the same saved material prevents later conclusions from depending on a changing web page.
Then, check each documentation link with an HTTP request. HTTP is the standard system used by browsers and programs to request web pages, and a successful status such as 200 means the page responded successfully.
Search the documentation for the reasoning control and identify its exact name for each protocol. A protocol is a defined way for a program to communicate with a service. The control is named output_config.effort for the Anthropic-compatible endpoint, reasoning_effort for the OpenAI-compatible endpoint, and reasoning.effort for the OpenAI Responses endpoint.
Send test requests that attempt to disable reasoning. Testing matters because documentation can be incomplete or ambiguous. The tests showed that thinking disabled or effort none returns HTTP 400, which means the request is rejected as invalid.
Write the findings as an audit and a browser-agent short. A browser agent is software that records actions and results while operating a browser, so the public explanation has supporting evidence rather than only a verbal claim.

#### What the measurements mean

##### 117 documentation pages fetched and read locally
What was measured: This counts the number of vendor documentation pages that were downloaded and read from saved markdown text.
What it supports: It directly supports that the stated review covered 117 documentation pages rather than only a small sample.
What it does not prove: It does not prove that the documentation was complete, correct, or unchanged after the review.

##### 117 of 117 links returned HTTP 200, zero rot
What was measured: All 117 checked documentation links returned HTTP status 200, which normally means the requested page was available. Zero rot means none of the checked links appeared broken at the time of checking.
What it supports: It directly supports that every checked link responded successfully during the audit.
What it does not prove: It does not prove that the pages contained the expected content or will remain available later.

##### pricing page mentions effort 0 times, thinking 0 times and reasoning 0 times across the full document
What was measured: The full pricing document was searched for the words effort, thinking, and reasoning, and each word appeared zero times.
What it supports: It directly supports that those three terms were not present in the pricing document that was checked.
What it does not prove: It does not prove that the pricing page had no related information using different words, or that another pricing page could not mention the setting.

##### 5 public GitHub comments posted under iamtamilore on MiniMax-AI/minimax-code issues #507, #576, #521 twice and #289, each with its live comment URL
What was measured: This counts five public comments made under the named account across the listed repository issues. Issue #521 received two comments, which is why it appears twice.
What it supports: It directly supports that the audit findings were shared publicly in five comments with live links to those comments.
What it does not prove: It does not prove that the vendor reviewed the comments, accepted the findings, or changed its documentation or API.

#### The honest limit
The audit does not measure the reliability, speed, cost, or output quality of the different reasoning settings. It also does not prove that every undocumented behavior was discovered. The test specifically found that thinking disabled or effort none returned HTTP 400, but it did not establish whether other ways of reducing reasoning exist.
Current status: Research. The documentation audit is retained as a dated research snapshot.
- LINK: [Inventory →](/cv/)

### Brand-consistency factorial experiment with a reference image

#### The problem this system addresses
The question was whether showing a reference image and using a carefully structured prompt help an image model reproduce a brand wordmark correctly. This experiment prevents conclusions based only on a few attractive examples or on personal visual impressions.

#### What the system does
This system creates images under four combinations: a plain prompt or a structured prompt, each with or without a reference image. A prompt is the written instruction given to the image model, and a reference image is an example image supplied to guide the result. It checks the generated images with OCR, which means software that reads text from pictures, and with CIEDE2000, a numerical measure of color difference. It then compares the groups using statistical tests, which estimate whether an observed difference is larger than would be expected from random variation.

#### How it works
First, define a 2 by 2 factorial design. This means crossing two choices, prompt style and reference-image use, to create four conditions. Defining all four conditions first matters because it makes the comparison balanced and makes it possible to test whether the two choices interact.
Next, prepare nine briefs and generate 20 images for each condition and brief. A brief is one specific image task. Repeated images are needed because one generation can succeed or fail by chance.
Keep the confirmatory set fixed before looking at the comparison. Confirmatory means the main test chosen in advance, while exploratory means an additional analysis considered after or alongside the main test. Fixing the main set first reduces the chance of changing the question after seeing the results.
Score the wordmark with OCR exact match. An exact match means the text read from the image is exactly the required brand wordmark, rather than merely looking similar.
Measure color with CIEDE2000. This is a standardized calculation of how different two colors appear numerically, with a smaller distance generally meaning closer colors.
Do not calculate CLIP or FID for the final set, and record why they were not used. CLIP is a model-based similarity score between images and text or images. FID is a distribution-level comparison often used for generated images. Recording the omission makes it clear that these measurements are unavailable rather than accidentally forgotten.
Use a stratified test for the 2 by 2 design. Stratified means comparing results within defined groups, such as briefs or tiers, before combining them. This order helps preserve the factorial structure and prevents a pooled comparison from hiding an interaction between prompt style and reference-image use.
Report the confirmatory and exploratory results separately. This prevents a secondary result from being presented as though it were the preselected main result.

#### What the measurements mean

##### 718 scored images across 9 briefs and 4 conditions, from a 720-cell design
What was measured: The planned design had 9 briefs multiplied by 4 conditions multiplied by 20 replicates, producing 720 planned image cells. Of those, 718 images received scores.
What it supports: It directly supports that the experiment covered the stated briefs and conditions and that 718 generated images were scored.
What it does not prove: It does not prove that the two missing images would have had the same results as the scored images or that every image was equally difficult.

##### confirmatory set: wordmark read correctly in 29 of 80 without a reference (0.362) and 49 of 80 with one (0.613), odds ratio 2.78 at p = 0.0026
What was measured: In the preselected confirmatory group, OCR read the wordmark correctly in 29 of 80 images without a reference, or 0.362, and in 49 of 80 images with a reference, or 0.613. The odds ratio of 2.78 compares the odds of a correct reading between the two groups. The p value of 0.0026 is the reported probability measure from the statistical test under its assumptions.
What it supports: It directly supports that the reference-image group had a higher wordmark exact-match rate in this confirmatory set, with the reported statistical result.
What it does not prove: It does not prove that the reference image caused the same improvement for every possible brand, prompt, model, or image task.

##### exploratory tier 1 set: 14 of 40 without reference (0.35) and 24 of 40 with one (0.60), odds ratio 2.79 at p = 0.043
What was measured: In the exploratory tier 1 group, OCR read the wordmark correctly in 14 of 40 images without a reference, or 0.35, and in 24 of 40 images with a reference, or 0.60. The odds ratio of 2.79 compares the odds of success between those groups. The p value of 0.043 is the reported result of the statistical test for this exploratory comparison.
What it supports: It directly supports that the reference-image group had a higher exact-match rate in this exploratory tier 1 group.
What it does not prove: Because this result is exploratory and uses only 40 images per comparison, it does not provide the same level of preplanned evidence as the confirmatory result.

##### current scores.csv holds 1,242 scored rows across 267 unique brief ids, so the scored set grew after the paper figures were fixed
What was measured: The current scoring file contains 1,242 rows, where each row represents a recorded score, and those rows refer to 267 distinct brief identifiers. This is a later and larger scored set than the one used for the fixed paper figures.
What it supports: It directly supports that the current scoring file contains 1,242 scored records covering 267 distinct briefs and that the dataset expanded after the paper figures were fixed.
What it does not prove: It does not prove that the later records were included in the published statistical results or that the later and earlier records are directly comparable.

##### 96 commits
What was measured: A commit is a saved version of changes in a version-control history. This counts 96 saved change points in the experiment's code and research materials.
What it supports: It directly supports that the project history contains 96 commits.
What it does not prove: It does not measure experiment quality, correctness, reproducibility, or the amount of work represented by each commit.

#### The honest limit
The final reported experiment did not compute CLIP or FID, so those aspects remain unmeasured. The design has 718 scored images rather than the planned 720, and the current scoring file has grown beyond the fixed paper figures. The results measure wordmark OCR and color distance, not general image quality, human preference, brand safety, or performance on all image models and brands.
Current status: Research. The confirmatory analysis is frozen separately from the later exploratory corpus.
- LINK: [Inventory →](/cv/)

### Model robustness and failure-cause analysis

#### The problem this system addresses
Different models were used different numbers of times, so simply comparing their raw failure counts could give a misleading result. This system prevents the specific failure of treating the number of attempts as if it were a fair sample size or treating every failure as the same kind of problem.

#### What the system does
This system records image-generation attempts made with four models and separates attempts that produced a usable scored result from attempts that did not. It groups failures by their cause for each model instead of reporting only one total failure number. A success rate is the share of scored attempts that succeeded, and a 95 percent confidence interval is a calculated range showing the uncertainty around that rate. The gpt model is used as the baseline, meaning the reference model against which the other models are compared. A stratified test compares models within matching model and condition groups, and the rejected alternative test is kept with the reason it was rejected.

#### How it works
First, record every generation attempt and identify which model made it. This preserves the unequal number of attempts instead of hiding it.
Next, identify whether each attempt produced a scored cell, meaning an output for which the evaluation could be completed. This matters because an attempt without a scored result should not silently count as a normal success or failure.
Then, label the cause of each failure for each model. This shows whether models fail in different ways rather than making all failures look identical.
Calculate each model's success rate from the scored results and calculate a 95 percent confidence interval around it. The interval communicates uncertainty, so a small difference is not automatically treated as a reliable difference.
Use gpt as the baseline and compare every other model with it. A baseline gives all comparisons the same reference point.
Use Fisher exact test where a comparison involves small counts. This test checks whether the observed success and failure counts could reasonably differ by chance without relying on a large-sample approximation.
Use the Cochran-Mantel-Haenszel test across model and condition pairs. This combines comparisons while accounting for the condition groups, which is why it is preferred to a single ungrouped comparison here.
Record the statistical method that was rejected and why. This makes the analysis auditable and prevents a later reader from assuming that an unreported method was used.

#### What the measurements mean

##### 544 generation attempts produced 222 scored cells across 4 models: flux, gpt, kontext, nano
What was measured: There were 544 total tries to generate outputs. Only 222 of those tries produced cells that could be scored, and the four models involved were flux, gpt, kontext, and nano.
What it supports: This directly supports that the attempt count and the usable scored-result count were different, and that the evaluation covered four named models.
What it does not prove: It does not prove that the four models received equal treatment, or that the scored cells were representative of every attempt.

##### per-model success rate: nano 0.5248, gpt 0.5106, kontext 0.314, flux 0.2695
What was measured: These are the shares of scored results that succeeded for each named model. For example, 0.5248 means that nano succeeded on about 52.48 percent of its scored results, not necessarily 52.48 percent of all generation attempts.
What it supports: This directly supports the reported difference in observed success rates among nano, gpt, kontext, and flux.
What it does not prove: The rates alone do not prove that one model is truly better, because uncertainty, unequal sample sizes, and differences in conditions may affect them.

##### credits consumed per model: gpt 432, nano 296, flux 190, kontext 190
What was measured: These numbers are the credits used by each model during the recorded work. A credit is the vendor's usage unit for running the generation service.
What it supports: This directly supports that the models consumed different amounts of the available usage budget.
What it does not prove: It does not show the cost per successful result, the quality obtained for each credit, or whether the credit prices were comparable across models.

##### baselines are briefs L1 and P2 with gpt as the baseline model
What was measured: The comparisons use briefs L1 and P2 as the reference task conditions, and gpt is the reference model. A baseline is the fixed point used to interpret differences in other models or conditions.
What it supports: This directly supports which task conditions and model were used as the comparison reference.
What it does not prove: It does not prove that gpt is the best model or that L1 and P2 represent every possible task.

#### The honest limit
The source shows that the data and statistical methods were recorded, but it does not provide the confidence interval values, the individual failure-cause counts, or the test results and significance values. The unequal number of attempts remains a limitation, and the 222 scored cells are not the same thing as 544 independent observations.
Current status: Evaluation. Generation failures were recorded and grouped by cause rather than scored as wins alone.
- LINK: [Inventory →](/cv/)

### TermsGuard contractual clause compliance pipeline

#### The problem this system addresses
Lawyers were spending time reviewing every flagged contract clause, including clauses that did not need attention. The system is meant to prevent important unfair clauses from being buried in a large amount of routine review work.

#### What the system does
This system examines contract clauses in two stages. First, a classifier, meaning a program that sorts text into categories, proposes which clauses may be concerning. Then Claude, a language model that reads text and produces a judgement, reviews up to 15 proposed clauses using relevant reference material. A retrieval index, meaning a searchable store of text fragments, finds supporting governance information. If the external model service is unavailable because no API key is set, the system still performs similarity matching and clearly reports that it did not receive a model verification.

#### How it works
The system starts with 102 hand-labelled clauses, meaning clauses that a person has already marked as fair or unfair. These examples give the first-stage classifier concrete examples to compare against.
The classifier compares clauses with the reference examples and proposes clauses that may be unfair. This comes first because sending every clause to the language model would use more time and service capacity.
The system searches a FAISS index. FAISS is a tool for finding text with similar meaning, and the index contains 4,527 chunks of governance reference material. This adds relevant background before a final judgement is made.
The system sends no more than 15 proposed clauses to Claude. Limiting the number keeps the review step bounded and focuses the model on the clauses most likely to need attention.
The result is routed using confidence thresholds. A score of 0.55 or more is treated as high confidence, while a score of 0.45 or more is treated as medium confidence. The exact routing behaviour below those levels is not further specified here.
When no API key is available, the system switches to matching-only mode instead of stopping. Every response includes verification_source and verification_error, which identify where the result came from and whether an error occurred, so a fallback cannot appear to be a successful model ruling.

#### What the measurements mean

##### 102 hand-labelled reference clauses, 52 fair and 50 unfair
What was measured: The reference set contains 102 clauses in total: 52 were labelled fair and 50 were labelled unfair by a person.
What it supports: It proves the classifier had a small, explicitly labelled reference set with both outcome types.
What it does not prove: It does not prove that the classifier generalises accurately to contracts outside this reference set.

##### 4,527 reference chunks in the retrieval index
What was measured: The search index contains 4,527 separate pieces of governance reference material that can be retrieved for context.
What it supports: It proves the system has a substantial stored reference collection available during review.
What it does not prove: It does not prove that the retrieved material is always relevant or that the final rulings are correct.

##### up to 15 flagged clauses sent to the model per analysis
What was measured: For one analysis, the model receives no more than 15 clauses that the first stage has flagged.
What it supports: It proves there is a limit on how many clauses reach the slower model-based ruling stage.
What it does not prove: It does not prove that all important clauses are included among those 15.

##### end-to-end latency 28 seconds reduced to under 10 for short policies
What was measured: The complete processing time was 28 seconds before an improvement, and became less than 10 seconds for short policies after the improvement. Latency means elapsed waiting time from request to result.
What it supports: It proves the measured response time improved for short policies.
What it does not prove: It does not prove that long policies have the same response time or that the system is always available.

##### matching-only fallback when no key is set, with verification_source and verification_error on every response
What was measured: When the required model-service key is missing, the system uses text matching instead of model verification and includes two fields describing the verification source and any error.
What it supports: It proves the fallback is designed to be visible in the returned result rather than silently replacing model verification.
What it does not prove: It does not prove that matching-only results are as accurate as model-verified results.

##### 34 commits on the deployment repository
What was measured: The deployment repository contains 34 recorded code-change entries called commits.
What it supports: It proves that at least 34 changes were recorded in that repository.
What it does not prove: It does not measure reliability, quality, usage, or production success.

#### The honest limit
The source does not report classifier precision, recall, or accuracy on an independent test set. The reference set is small, the quality of the model rulings is not quantified here, and the fallback's accuracy is not measured. The retrieval collection size and latency figures do not establish legal correctness.
Current status: Published. Case study, live demo, source and verification evidence are available.
- LINK: [Case study →](/p/termsguard/)

### Smart Medical Records Engine with per-patient retrieval

#### The problem this system addresses
A clinical assistant could accidentally retrieve one patient's note while answering a question about another patient if both notes used similar words. The system is designed to prevent cross-patient record leakage.

#### What the system does
This is a clinical RAG system, meaning it retrieves relevant records and gives them to a language model to help form an answer. It makes the patient identifier part of the search boundary, rather than searching everyone and filtering results later. A local language model runs inside the hospital network, while authorization, redaction, and audit recording happen around the request. An audit log is a record of who requested information and what retrieval or answer activity occurred.

#### How it works
A physician request is first checked for authorization. Authorization means checking that the person is allowed to access the requested patient's information.
The request is associated with a patient_id, which is the identifier for one patient. This identifier is included in the retrieval query itself, so records for other patients are excluded before similarity search returns results.
Each note stores a 768-number embedding beside its patient_id. An embedding is a numerical representation of meaning, and a vector is the ordered list of numbers used for similarity comparison.
PostgreSQL with pgvector searches the permitted patient's stored note vectors for relevant matches. PostgreSQL is the database, and pgvector is the database extension that supports vector similarity search.
PII redaction removes or hides personally identifying information where the application requires it. PII means information that can identify a person, such as a name or address.
The matching notes are passed to llama3.1 running through Ollama on the local network. This order keeps the records inside the hospital environment before the model generates an answer.
The system writes retrieval and answer events to an audit log. Recording these events makes later review possible and provides evidence of what the system did.
The API, database, model, and supporting parts run as four Docker Compose services on one private network. Docker Compose starts and connects these services in a controlled environment.

#### What the measurements mean

##### 30 adversarial probes designed to leak cross-patient data, 30 of 30 passed, zero leaked
What was measured: Testers created 30 deliberately difficult requests intended to expose another patient's information. All 30 tests passed, and no cross-patient information was exposed in those tests.
What it supports: It proves the tested privacy boundary resisted all 30 designed probes.
What it does not prove: It does not prove that no undiscovered attack or implementation error could ever leak data.

##### 768-dimensional pgvector embeddings stored on the same row as patient_id
What was measured: Each database record stores a 768-number meaning representation together with the identifier of the patient to whom the note belongs.
What it supports: It proves the database design keeps the patient boundary available at the same record level as the searchable representation.
What it does not prove: It does not by itself prove that every query, permission check, or answer respects that boundary.

##### 4 Docker Compose services on one private network
What was measured: The application, database, language model, and another supporting component are run as four connected services inside one network that is not publicly exposed by the described design.
What it supports: It proves the system has a separated four-service deployment structure with private service-to-service connectivity.
What it does not prove: It does not prove the network is secure against every deployment or configuration mistake.

##### self-hosted llama3.1 via Ollama, no record leaves the hospital network
What was measured: The llama3.1 language model is operated locally through Ollama, and the stated design keeps clinical records inside the hospital network rather than sending them to an external model service.
What it supports: It proves the intended model-serving arrangement is local and designed to keep records on the private network.
What it does not prove: It does not prove that every operational log, backup, or future integration has the same data boundary.

#### The honest limit
The privacy result covers 30 designed probes, not every possible request or attack. The source does not provide clinical answer accuracy, response time, availability, or independent security testing beyond those probes. Actual patient data and operational deployment details are not described here.
Current status: Published. Case study, source and a limited adversarial retrieval test are available.
- LINK: [Case study →](/p/clinical-rag/)

### Image QA gate over frozen ResNet50 Siamese features

#### The problem this system addresses
An image-generation process could put the wrong person's identity into an image even when the pose looked correct. The gate is designed to prevent this dangerous false positive, meaning incorrectly accepting two different people as the same person.

#### What the system does
This system checks whether an image has the intended identity and whether its overall grade or quality fits the requirement. It uses a Siamese network, which compares two images by sending them through matching processing paths, on top of frozen ResNet50 features. ResNet50 is a pretrained image-recognition model, and frozen means its learned features are not changed during this task. The system makes an accept or reject decision using a threshold, which is a chosen score boundary.

#### How it works
The system extracts visual features from images with ResNet50. Features are measurable patterns such as shapes and identity-related visual information, and using a pretrained model avoids learning all visual patterns from the beginning.
The Siamese network compares the features from the relevant image pair. Its two matching paths are intended to measure whether the images represent the same identity or satisfy the required relationship.
The gate checks two conditions rather than only one. Identity similarity must be high, and grade fit must be below its threshold, so an image with a good pose but the wrong person can still be rejected.
The decision threshold is selected using validation data. Validation data is data used to choose settings, and keeping the test data separate prevents the test result from being used to tune the system.
The threshold changes from 0.5 to 0.4821 after validation tuning. This happens before final evaluation so the reported test result measures the chosen rule rather than a rule adjusted after seeing the test answers.
The gate runs on a CPU, meaning a general-purpose processor rather than a graphics processor. This allows it to operate as an inline check during image processing instead of only as a later batch job.

#### What the measurements mean

##### Siamese gate: precision 1.00, recall 0.82, F1 0.90, ROC-AUC 1.00 on 90 sealed test pairs
What was measured: On 90 test pairs whose answers were kept separate from tuning, precision was 1.00, meaning every accepted positive case was correct in this test. Recall was 0.82, meaning the system found 82 percent of the positive cases. F1 was 0.90, a single score combining precision and recall. ROC-AUC was 1.00, meaning the score ordering separated the tested positive and negative pairs perfectly across thresholds.
What it supports: It proves the gate performed strongly on these 90 sealed test pairs, especially for avoiding false positive acceptances.
What it does not prove: It does not prove the same performance on new identities, image conditions, or a larger test set.

##### baselines: pixel difference F1 0.59 and kNN F1 0.26
What was measured: Two simpler comparison methods were tested. Pixel difference had an F1 score of 0.59, while kNN, meaning a method that uses nearby examples to decide, had an F1 score of 0.26.
What it supports: It proves the tested Siamese method scored higher on F1 than these two comparison methods in the reported evaluation.
What it does not prove: It does not prove that these were the best possible versions of the comparison methods or that the result applies outside this dataset.

##### threshold moved from 0.5 to 0.4821, recovering all 8 misses with no new false positives and lifting F1 from 0.90 to 1.00
What was measured: Changing the decision boundary from 0.5 to 0.4821 caused the validation-tuned system to recover 8 previously missed cases and introduced no additional incorrect acceptances in the reported result. F1 increased from 0.90 to 1.00.
What it supports: It proves this threshold change improved the measured result under the stated evaluation conditions.
What it does not prove: It does not prove that the same threshold is optimal for future data or that no false positives will occur in deployment.

##### per-image gate latency 133 ms on CPU, roughly 450 images a minute
What was measured: The gate took 133 milliseconds to process one image on a CPU. At that measured rate, it could process approximately 450 images in one minute.
What it supports: It proves the reported check is fast enough to be considered for inline processing on the tested CPU setup.
What it does not prove: It does not prove the same speed on different hardware, image sizes, or concurrent workloads.

#### The honest limit
The evaluation uses 90 sealed test pairs, and the source does not describe how representative they are of future images. The system's behaviour under image corruption, unusual lighting, multiple people, or changing identities is not measured here. The reported threshold improvement must be understood in the context of the stated evaluation data.
Current status: Published. Case study, baseline comparison, architecture and source are available.
- LINK: [Case study →](/p/image-qa/)

### Customer Care BPMN triage agent

#### The problem this system addresses
Customer-care tickets were being routed manually, and a wrong route could send a customer to a queue that could not help. The system is designed to prevent uncertain tickets from being forced into an unreliable automatic category.

#### What the system does
This system reads a customer-care ticket and predicts which category should handle it. It uses Naive Bayes, a simple statistical classifier that estimates categories from the words in the ticket. The workflow is shown as BPMN, a diagram format for business processes, so the automatic step and the human escalation step are visible. When the classifier is not confident enough, the ticket goes to a person instead of being automatically routed.

#### How it works
The system starts with a labelled corpus of 210 tickets. A corpus is a collection of documents, and labelled means each ticket already has a known category for learning.
Naive Bayes learns how words are associated with each category. It is deliberately simple because the dataset is small and the business can more easily understand its decisions than a more complicated model.
For a new ticket, the classifier calculates a confidence score for its most likely category. This score expresses how strongly the available word evidence supports that category.
The system compares the score with 0.55. If the score is below 0.55, the ticket is sent to a human; this step matters because uncertainty is handled explicitly rather than hidden inside an automatic decision.
If the score meets the required confidence, the workflow routes the ticket to the predicted category. BPMN represents both paths so the process can be reviewed as a business workflow, not only as source code.
The prediction is evaluated on held-out tickets. Held-out means the tickets were kept out of training so the evaluation tests the model on examples it did not learn from.

#### What the measurements mean

##### labelled corpus 210 tickets, 42 per category
What was measured: The learning collection contains 210 categorised tickets, with 42 tickets assigned to each category.
What it supports: It proves the classifier was built from an evenly sized labelled collection of 210 examples.
What it does not prove: It does not prove that 42 examples per category are enough to represent real customer-care traffic.

##### routing accuracy on held-out tickets 95.2%, which is 40 of 42
What was measured: On 42 tickets not used for training, the system routed 40 to the correct category. This equals a reported accuracy of 95.2 percent.
What it supports: It proves the system made 40 correct routing decisions in that held-out sample.
What it does not prove: It does not prove a 95.2 percent rate for future tickets because the test sample is small.

##### confidence threshold 0.55, below which a human decides
What was measured: A prediction with a confidence score below 0.55 is not automatically accepted; a human makes the routing decision instead.
What it supports: It proves the workflow has an explicit rule for escalating lower-confidence predictions.
What it does not prove: It does not prove that 0.55 is the best threshold or that human decisions are always correct.

##### the write-up states 42 held-out tickets is a thin evaluation, so the accuracy claim is reported with that limit attached
What was measured: The evaluation uses only 42 test tickets, and the project description explicitly calls this a small or thin test.
What it supports: It proves the reported accuracy is accompanied by an explicit warning about the test size.
What it does not prove: It does not provide evidence about performance on a larger or more varied ticket population.

#### The honest limit
The held-out evaluation is small, with 42 tickets. The source does not report coverage of changing customer language, category imbalance in real traffic, human-routing quality, or long-term production use.
Current status: Published. Case study, BPMN diagrams, evaluation evidence and source are available.
- LINK: [Case study →](/p/care-agent/)

### Surge pricing policy comparison, reinforcement learning against a genetic algorithm

#### The problem this system addresses
A ride-hailing pricing policy needed to be chosen between two learning methods, but the methods had to be compared fairly. The experiment is designed to prevent one method from appearing better merely because it received different data or random conditions.

#### What the system does
This system simulates pricing strategies using real Boston ride records as input data. It compares Q-learning, a method that learns actions from rewards over time, with a genetic algorithm, a method that improves a population of candidate policies through selection and variation. Several fixed strategies provide baselines, meaning reference methods for comparison. Each method is tested with the same number of seeds and simulated days so the comparison focuses on the method rather than accidental randomness.

#### How it works
The system prepares 637,976 ride records and removes metered Taxi-tier rides because those records do not contain a quoted price for this experiment. This makes the input fit the pricing calculation.
It defines the reward as daily revenue. A reward is the numerical result that a learning method tries to improve, so both learning methods are judged using the same business objective.
The Q-learning agent observes a simulated situation and learns which pricing action tends to produce higher future rewards. The genetic algorithm instead creates candidate pricing policies and repeatedly keeps and varies the better-performing candidates.
The experiment also runs flat pricing and a third baseline. These reference strategies show what the learning methods achieve compared with simpler alternatives.
Every strategy is evaluated on the same 8 random seeds and 30 simulated days per seed. A seed is a fixed starting value for random number generation, so reusing the same seeds makes the comparison more consistent.
The global seed is set to 42. This makes the experiment reproducible, meaning another run with the same code and inputs can recreate the same random setup.
The report compares average daily revenue and average ride fare, then explains why one method performed better. Separating results from explanation helps distinguish the measured outcome from an interpretation of the outcome.

#### What the measurements mean

##### 637,976 ride records after dropping metered Taxi-tier rides
What was measured: After removing the specified rides without quoted prices, the experiment used 637,976 ride records as its input data.
What it supports: It proves the reported experiment was based on 637,976 prepared records.
What it does not prove: It does not prove that the records represent all ride-hailing demand or that the simulation predicts real-world revenue.

##### 8 seeds of 30 simulated days per strategy
What was measured: Each strategy was tested under 8 fixed random starting conditions, with each condition representing 30 simulated days.
What it supports: It proves every strategy received repeated evaluation across the same stated number of simulated runs.
What it does not prove: It does not prove that 8 seeds or 30 days are enough to capture all possible market conditions.

##### GA reached 855,244 USD average daily revenue, 13,442 average ride fare and +21.4 percent, against Q-learning at +18.2 percent
What was measured: The genetic algorithm produced an average daily revenue of 855,244 USD, an average fare of 13,442, and a reported improvement of +21.4 percent. Q-learning's reported improvement was +18.2 percent.
What it supports: It proves the genetic algorithm had the higher reported improvement than Q-learning in this simulation.
What it does not prove: It does not prove that either policy would produce the same result in live operations or that revenue is the only important business outcome.

##### global SEED = 42 for exact reproduction
What was measured: The experiment sets its global random-number starting value to 42 so the same random sequence can be recreated when the other conditions are unchanged.
What it supports: It proves the experiment has a stated reproducibility setting for its random choices.
What it does not prove: It does not prove that different seeds would lead to the same ranking or conclusions.

#### The honest limit
The results come from simulation rather than a live pricing deployment. The source does not measure rider welfare, driver supply, fairness, regulatory effects, demand changes caused by prices, or performance on future data. The outcome may depend on the chosen simulator, reward, seeds, and baselines.
Current status: Unpublished. The write-up exists. The public case-study route is not published.
- LINK: [Inventory →](/cv/)

### Telecom CRM and call-record data migration programme

#### The problem this system addresses
Customer information was stored in several business systems, and those systems sometimes disagreed about the same person or about the number of active customers. The work was designed to prevent incorrect, incomplete, or duplicated data from being trusted by reports and later systems.

#### What the system does
This is a set of data migration and checking processes for a telecom operator. A CRM, or customer relationship management system, is the system that stores customer information, and Python scripts copy that information into a cleaner format. SQL, a language for asking questions of stored data, compares the copied records with the original records to find missing or inconsistent data. KPI dashboards, which are screens showing important operational measurements, display more than 30 measures, while UAT, or user acceptance testing, checks whether the migrated data and related functions behave as expected.

#### How it works
First, customer records are extracted from the CRM. Extraction means reading records from one system and preparing them for use elsewhere, and it happens first because later checks need a defined copy of the source data.
Next, Python scripts clean and validate the extracted records. Python is a programming language, and validation means checking whether data follows expected rules before other people rely on it.
Then, SQL compares the number of extracted rows with the number of rows in the source system. A row is one stored record, and this comparison happens after extraction so that missing records can be identified before reporting or migration continues.
The process checks for disagreements between systems, including duplicate identities. An identity is the set of information used to represent one customer, and a duplicate identity occurs when two systems represent the same customer with different keys, or identifying values.
The team worked with the solutions architect on a migration architecture for 400 million daily call records. A migration architecture is the planned design for moving and organizing data, and designing it before implementation matters because the size and daily volume affect how the data can be handled.
The validated information is used in KPI dashboards and in formal UAT. A dashboard is a visual display of measurements, and a test case is one documented check of expected behavior; testing after validation provides a structured way to find problems before users trust the result.

#### What the measurements mean

##### CRM extraction in Python saved 15 hours per week
What was measured: This measured the amount of staff time saved each week by using Python to extract CRM data instead of performing the same extraction manually. The unit is hours per week.
What it supports: It directly supports that the extraction work required less manual time after automation.
What it does not prove: It does not prove that every extracted record was correct, complete, or free of duplicate identities.

##### SQL validation of 100,000 plus rows caught a 14 percent monthly active user discrepancy
What was measured: This means SQL checks covered more than 100,000 data rows and found that the reported number of monthly active users differed by 14 percent between the compared sources. A monthly active user is a user counted as active during a month; the percentage is the size of the discrepancy between the compared counts.
What it supports: It directly supports that the SQL comparison detected a substantial disagreement in the checked data before it reached a dashboard.
What it does not prove: It does not show that all data disagreements were found, explain the full cause of the discrepancy, or prove that the discrepancy was completely corrected.

##### more than 30 KPI dashboards delivered
What was measured: This counted more than 30 dashboards showing KPIs, or key performance indicators. A KPI is a selected measurement used to monitor an operational result, and the unit counted was dashboards delivered.
What it supports: It directly supports that more than 30 operational dashboard views were produced.
What it does not prove: It does not prove that the dashboards were accurate, used by customers, or based on fully reconciled data.

##### data migration architecture for 400 million daily call records, worked on with the solutions architect
What was measured: This describes the planned design work for moving or organizing 400 million call records generated each day. A call record is a stored description of a telecom call, and the unit is records per day; the metric also states that the work was done with the solutions architect.
What it supports: It directly supports experience planning for a data movement design at the stated daily record volume and collaboration with a solutions architect.
What it does not prove: It does not prove that 400 million records were successfully migrated, that the architecture was deployed, or that it met a measured performance target.

##### 440 plus user acceptance test cases executed
What was measured: This counted more than 440 documented UAT checks that were run. Each test case is one defined situation with expected results, and executed means the check was performed rather than merely written down.
What it supports: It directly supports that more than 440 formal user acceptance checks were carried out.
What it does not prove: It does not prove that all tests passed, that the tests covered every important failure, or that users accepted the final migration.

#### The honest limit
The information does not measure whether the full migration was completed, whether all duplicate customer identities were resolved, or whether every record was correct after migration. It does not state how many UAT cases passed or failed, whether the dashboards were used, or whether the planned architecture was deployed. The source also does not provide a complete accuracy rate, a measured processing time, or proof that the 14 percent discrepancy was fixed.
Current status: Professional. The public version abstracts client and employer details while preserving the engineering evidence.
- LINK: [Inventory →](/cv/)

### Outreach verification and audit database

#### The problem this system addresses
Sending an outreach message with an unchecked claim about a company or product can damage the sender's credibility. This system prevents factual claims from being treated as verified without a recorded check and prevents suppressed or opted-out contacts from being selected through ordinary queue views.

#### What the system does
This system is a customer relationship management database, meaning a structured store of information about contacts, research, and messages. It stores contacts, audits, findings, claim checks, opt-outs, planned posts, and outreach events in SQLite, a small database format. Each claim in a message gets its own record showing whether it was checked. Database views are saved queries that present only records meeting specific rules, such as contacts that are not suppressed.

#### How it works
First, the database stores a contact record. A contact is a potential contact, and the record gives the system one place to track that contact's status.
An audit then records a review of the contact or company. An audit finding is one individual result from that review. Keeping findings in a separate table allows one audit to contain many findings without repeating the audit information.
Each factual statement planned for an outreach message becomes a claim check. The claim check stores the statement and its verification state, such as checked or still needing verification. This creates a record before sending rather than relying on memory.
Opt-out and suppression information is stored and exposed through views. An opt-out means the person has asked not to receive messages, while suppression means the system should exclude the contact. Using views makes the same exclusion rule available wherever the contact queue is read.
The posting schedule records what is planned, while outreach events record what was actually sent or attempted. Keeping these separate prevents a plan from being mistaken for a completed message.

#### What the measurements mean

##### 16 contacts, 10 audits, 60 audit findings, 55 claim checks and 40 outreach events
What was measured: The database contained 16 contact records, 10 audit records, 60 individual audit finding records, 55 claim check records, and 40 outreach event records. The unit for each number is a database row in the named table.
What it supports: It directly supports the recorded amount of data in each of those tables at the time of measurement.
What it does not prove: It does not prove that the claims were all correct, that messages were delivered, that contacts consented, or that the database contains every real-world outreach activity.

##### tables include contacts, audits, audit_findings, claim_checks, outreach_events, opt_out, posting_schedule and views v_contact_status, v_claims_to_verify, v_suppressed, v_contact_queue
What was measured: This lists the database tables and saved views. Tables hold stored records. Views are saved database questions that show a filtered or combined list without copying the underlying records.
What it supports: It directly supports that these named storage structures and views exist in the database.
What it does not prove: It does not prove that every view is correct, that every record is complete, or that the suppression rules were tested against every possible sending path.

#### The honest limit
The source does not measure claim accuracy after sending, delivery rate, response rate, consent quality, or whether a message was sent outside the database. It also does not provide details about the individual contacts, which are intentionally not included here.
Current status: Internal. The public version abstracts away contact records, private audit data and outreach history.
- LINK: [Internal →](/provenance/)

### Cross-model image bakeoff with defect capture

#### The problem this system addresses
Choosing an image model based on reputation can miss how it behaves on the exact task that matters. This system prevents the specific failure of selecting a model that looks attractive in general but produces incorrect product details or text in the required image.

#### What the system does
This system gives several image-generation models the same product image task and the same expected result. It records the task identifier, the usage credits spent, and the time taken for each run. People inspect the resulting images directly, because an optical character recognition tool, which tries to read text in an image, can give a low score even when the text looks correct to a person. The review names the exact defect, such as mirrored or reversed small text, instead of using only a general failure label. The winner is selected using both text accuracy and similarity to the product, rather than appearance alone.

#### How it works
Start with the same product shot, wordmark, and expectation set for each candidate model. Keeping the input and requirement fixed makes the comparison about the models rather than changing tasks.
Run the image request for each candidate and record the task identifier, credits spent, and wall time. Wall time means the elapsed time from starting the request to receiving the result.
Inspect each output visually. This step is necessary because an automated text-reading score may disagree with what a person can actually see.
Name the defect precisely when one appears. For example, mirrored text is text that is reversed left to right, which is different from text that is merely misspelled or unreadable.
Compare the models on text fidelity and product match. Text fidelity means whether the required words and their orientation are correct, while product match means whether the generated object still resembles the intended product.
Choose the model that performs best on those requirements, while retaining the cost and time information for the practical tradeoff.
Record competitors that are unavailable on the chosen vendor separately from models that were tested. This prevents an unavailable option from being mistaken for a poor-performing tested option.

#### What the measurements mean

##### 3 images at 6 credits each, balance 816 to 798 credits, 66 to 71 seconds per image
What was measured: A recorded run produced 3 images. Each image used 6 credits, the available balance decreased from 816 credits to 798 credits, and each image took between 66 and 71 seconds to complete.
What it supports: This directly supports the observed usage cost, balance change, and completion-time range for that run.
What it does not prove: It does not prove that all models always use 6 credits, always take 66 to 71 seconds, or have the same quality.

##### 5-model bakeoff covered gpt-image-2, nano-banana-2, grok-imagine-image, z-image and seedream, and gpt-image-2 won on text and product fidelity
What was measured: Five named image models were compared in the bakeoff: gpt-image-2, nano-banana-2, grok-imagine-image, z-image, and seedream. The recorded winner was gpt-image-2 when judged on correctness of the text and similarity to the product.
What it supports: This directly supports the tested model list and the recorded result for the stated comparison criteria.
What it does not prove: It does not prove that gpt-image-2 is the best model for other products, prompts, image styles, or evaluation criteria.

##### 3 of the commonly-named competitors have no image-generation offering on the vendor at all
What was measured: Three competitors that might commonly be mentioned were not available as image-generation options from the vendor used for this comparison. This is a count of unavailable offerings, not a count of failed image generations.
What it supports: This directly supports that three named or commonly discussed alternatives could not be tested through that vendor's image-generation service.
What it does not prove: It does not prove that those competitors cannot generate images elsewhere or that they would perform poorly if they were available.

#### The honest limit
The source does not provide the complete per-model scores, the exact number of images generated for every candidate, or a formal repeatability test. Visual review is useful for defects that automated text reading misses, but it is still dependent on the reviewers and is not a complete substitute for a larger measured evaluation.
Current status: Evaluation. A small, dated model bake-off records cost, time and visible defects.
- LINK: [Tools →](/tools/)

### Multi-model audition panel for generated hero selection

#### The problem this system addresses
One selected hero image is reused in roughly 300 later image generations, so a poor first choice can affect a large batch of work. This system prevents the specific failure of choosing a hero from one opinion or choosing an image with lighting or appearance that creates unwanted defects in every downstream result.

#### What the system does
This system creates 42 candidate hero images, with one candidate based on each mood-board source image. Four independent judge models each select and rank their top three candidates. Their choices are saved in a verdict file that records first, second, and third choices and counts how often each candidate was mentioned. Every candidate uses the same technical frame, meaning the same controlled image setup, so inherited lighting does not unfairly influence later images. The casting is left open so the image system invents a face instead of copying a real person's likeness, and the extraction format has no field for storing a likeness.

#### How it works
Generate one candidate for each of the 42 mood-board source images. This creates a broad set of alternatives before selecting a hero.
Keep the technical frame fixed for every candidate. A fixed frame controls the camera and lighting conditions, so one candidate does not receive an accidental advantage or introduce a directional shadow that later images will copy.
Ask four judge models to review the same candidate set independently. Independent judging reduces the risk that one judge's choice becomes the only opinion.
Have each judge record a first, second, and third choice. Ranking more than one choice preserves useful information when several candidates are acceptable.
Save the rankings in a standing verdict file and count mentions across judges. A mention count is the number of times a candidate appears in the judges' selected positions.
Use agreement among the judges to identify the leading candidate. Strong agreement is a clearer selection signal than a single isolated preference.
Keep the casting open and omit any field that could store a copied likeness. This makes the intended result an invented face rather than a stored identity reference.
Mark later authoritative rounds as replacing earlier rounds when the source record says they were superseded. This prevents an outdated selection from being treated as the final decision.

#### What the measurements mean

##### 42 candidates generated and judged
What was measured: The system created and evaluated 42 different possible hero images. A candidate is one proposed image that could be selected for later use.
What it supports: This directly supports the size of the candidate set that was generated and judged.
What it does not prove: It does not prove that all 42 candidates were equally good, equally diverse, or independently suitable for the downstream work.

##### 4 independent judges: gemini, qwen, gpt, llama
What was measured: Four named judge models independently reviewed the candidates: gemini, qwen, gpt, and llama. Independent means each judge made its ranking without the system presenting another judge's ranking as its answer.
What it supports: This directly supports the number and names of the judging models used.
What it does not prove: It does not prove that the judges were unbiased, that their judgments were human-equivalent, or that the models agreed on every candidate.

##### authoritative round is 4_brand_plus_garments, with rounds 1 to 3 superseded
What was measured: The final record identifies 4_brand_plus_garments as the authoritative round, meaning the round treated as current for this decision. Rounds 1, 2, and 3 were marked as replaced by that later round.
What it supports: This directly supports which round should be treated as the current source of the verdict and which earlier rounds should not be treated as final.
What it does not prove: It does not prove that the authoritative round was objectively better, or explain every reason the earlier rounds were replaced.

##### all 4 judges ranked aud_15 first, and 3 of 4 ranked aud_24 second
What was measured: Every one of the four judges placed the candidate named aud_15 in first place. Three of the four judges placed aud_24 in second place.
What it supports: This directly supports strong agreement on the first choice and substantial agreement on the second choice.
What it does not prove: It does not prove that aud_15 will produce the best downstream images, because downstream performance was not measured by this metric.

#### The honest limit
The source does not report a formal agreement statistic, human review comparison, downstream quality measurement across the roughly 300 later generations, or a test of whether the fixed technical frame actually prevented lighting defects. The system records judge consensus, but consensus among models is not the same as validated real-world quality.
Current status: Evaluation. Candidates were generated and judged through a multi-model panel.
- LINK: [Rater →](/rater/)

### Longitudinal experiment evidence log with a validator

#### The problem this system addresses
Research decisions and disagreements between numerical scores and human visual judgment were being reconstructed from memory after the work happened. This system prevents a later summary from silently changing what was observed, when it was observed, or how certain the observation was.

#### What the system does
This system records research observations as individual lines of structured text. Each line includes the kind of observation, a confidence level, and a timestamp. It marks whether an observation was captured live or reconstructed later, and it keeps a separate automatic record of media-generation calls. A validator checks the records for formatting errors and broken pieces before the log is used for the research write-up.

#### How it works
Record each observation as one JSONL line. JSONL means JSON objects stored one per line, so each observation can be added, checked, and processed separately without rewriting the whole file.
Include the observation kind, confidence, and timestamp. The kind says what sort of event was recorded, confidence says how certain the recorder is, and the timestamp says when it was recorded. Keeping these fields together preserves context for later review.
Mark live captures separately from backfilled reconstructions. A live capture is written close to the event, while a backfilled reconstruction is written later from memory or other evidence. This distinction prevents a later recollection from appearing to be contemporaneous evidence.
Capture generation calls automatically using a directory marker. A generation call is a request made to create media, and a directory marker is a known location or label that tells the logging system which calls belong to the experiment. Automatic capture reduces dependence on someone remembering to make a manual note.
Run the validator against the observation log. The validator is a checking program that looks for missing or malformed fields and broken shards, where a shard is a separated piece of stored log data. This catches structural problems before the records are treated as evidence.
Use the log as the main source for the thesis write-up. This order matters because the written conclusions are based on dated records rather than on a summary created after the outcome is known.

#### What the measurements mean

##### 462 observations recorded
What was measured: This counts 462 individual observation records in the JSONL evidence log.
What it supports: It directly supports that the log contains 462 recorded observations.
What it does not prove: It does not prove that all important events were recorded, that every observation is correct, or that the observations are independent.

##### media calls logged separately and automatically by directory marker
What was measured: Media-generation requests were recorded in a separate log, and the system identified which requests belonged to the work by using a directory marker. The metric is descriptive rather than a count, because no number of media calls is provided.
What it supports: It directly supports that media calls had a separate automatic logging mechanism tied to a directory marker.
What it does not prove: It does not show how many media calls were captured, whether every call was captured, or whether the recorded call details were complete.

#### The honest limit
The available evidence does not state how many records failed validation, whether any observations were corrected, or how many media calls were logged. The log records provenance and confidence, but it does not independently prove that an observation is true. It also does not measure the scientific quality of the underlying experiment or guarantee that no event was omitted.
Current status: Research. Longitudinal observations are recorded with a validator.
- LINK: [Provenance →](/provenance/)

### Flask image generation studio with streaming job updates

#### The problem this system addresses
Image generation can take time, so a user needs to see what is happening instead of waiting for a blank loading screen. The application is also designed to prevent invalid uploads and incorrect handling of a reference image.

#### What the system does
This is a Flask web application, meaning a Python program that serves pages and handles web requests. It starts an image-generation job and streams status lines to the browser as the job progresses. Streaming means sending updates as they are produced rather than waiting for the final result. The application also checks uploaded file types and converts local file locations into URLs that a remote interface can use.

#### How it works
The user submits an image-generation request through the web interface. Flask receives the request and starts the related generation work.
The backend runs the generation process as a subprocess, meaning a separate operating-system process. It reads output one line at a time so progress can be sent to the user while the job is still running.
The browser receives each progress line as it becomes available. This order matters because the user can see intermediate stages instead of receiving only a final success or failure message.
When generation produces a file on the local machine, the application translates its local path into a tunnel URL. A URL is an address the remote browser can request, while a local path is meaningful only on the machine that created the file.
Before saving an upload, the application checks that its file type is allowed. This reduces the chance that unsupported or unwanted files enter the workflow.
The application includes a regression test for a reference-image defect. A regression test is a repeatable check that confirms a previously fixed problem does not return after later code changes.

#### What the measurements mean

##### 853 lines of Flask application code
What was measured: The main Flask application file contains 853 lines of code, where code means written instructions executed by the application.
What it supports: It proves the measured application file has 853 lines.
What it does not prove: It does not prove the application is reliable, easy to maintain, or feature-complete.

##### streaming job updates, local path to tunnel URL translation, and a reference-handling defect fixed and covered by a regression test
What was measured: The application implements progress updates during jobs, changes local file locations into remotely usable addresses, and includes a repeatable test for a previously found reference-image problem.
What it supports: It proves these behaviours and the stated regression coverage are part of the recorded implementation.
What it does not prove: It does not provide a numerical measure of user experience, job success rate, upload security, or test coverage.

#### The honest limit
The source does not provide usage volume, generation success rate, latency, availability, or security-test results. The line count is not a performance measure. The system's image-generation quality is also not quantified.
Current status: Built. The implementation is verified by source inspection. Runtime behaviour is not quantified here.
- LINK: [Inventory →](/cv/)

### Episode-level QA gates for brief, claims and frames

#### The problem this system addresses
A video episode could look complete after rendering while still containing bad frames, mismatched narration, unsupported claims, an invalid script, or a malformed brief. This system prevents those specific problems from being discovered only after upload by checking the episode before it is published.

#### What the system does
This system is a group of checks for an episode, meaning one completed video and its supporting files. It checks the brief, narration script, factual claims, the connection between narration and shots, and the selected images or frames. A frame is one still image from a video, and a shot is a timed section of the video that uses one or more frames. The checks also compare shot timing with the audio so the pictures and spoken words do not drift apart.

#### How it works
The brief check examines the collection of planned episode information and confirms that it has the format the pipeline expects. A pipeline is an ordered set of processing steps that turns inputs into an output.
The script check examines the narration before rendering. Narration is the spoken text of the episode. Checking it early allows script errors to be rejected before time is spent generating video.
The claims check examines factual statements in the script and affiliate description. A claim is a statement presented as true. This check is intended to identify unsupported or invalid statements before publication.
The frame check examines selected images for duplication and quality rules. It uses SHA-256 hashing, which creates a repeatable digital fingerprint from an image, to detect identical frames.
The beat-alignment check compares each shot with the narration beat it was designed to illustrate. A beat is a small intended idea or moment in the narration. This ordering matters because a technically valid image can still be wrong for the words being spoken.
The timing check requires each shot to last from 0.4 seconds to 5.0 seconds, requires the final shot to last no more than 4.0 seconds, and requires the total shot time to be within 0.6 seconds of the audio. These checks run before upload so timing failures can be corrected before viewers see them.

#### What the measurements mean

##### shot duration bound 0.4 s to 5.0 s, final shot at or below 4.0 s, total shot duration within 0.6 s of the audio, duplicate frames detected by sha256
What was measured: Each shot must last at least 0.4 seconds and no more than 5.0 seconds. The final shot has a stricter maximum of 4.0 seconds. The sum of shot durations may differ from the audio duration by no more than 0.6 seconds. SHA-256 fingerprints are compared to find identical frames.
What it supports: The system has explicit shot-length, final-shot, audio-alignment, and duplicate-frame rules.
What it does not prove: It does not prove that the narration is factually correct, that the imagery is semantically appropriate, or that every episode passes.

##### 4 word-timing and alignment helpers exist for the beat and narration checks
What was measured: Four helper components related to word timing and alignment are present. A helper is a reusable piece of code that supports a larger check.
What it supports: The codebase contains four supporting components for timing and alignment checks.
What it does not prove: It does not prove that all four helpers are executed, correct, or sufficient for accurate alignment.

#### The honest limit
The evidence describes the checks and their thresholds but does not provide overall pass rates, false-positive rates, or failure counts. It also does not prove that every claim, visual quality issue, or beat mismatch is detected.
Current status: Production. Brief, claims and frames are checked before the episode is rendered.
- LINK: [Workflow →](/products/workflow/)

### MCP reconnect watchdog for self-healing tool servers

#### The problem this system addresses
When a local tool server stopped, the main program marked it as failed and left it stopped until a person changed a configuration file. This system prevents that specific failure from requiring manual recovery when the expected transport error is written to the log.

#### What the system does
MCP is a way for a main program to communicate with tool servers, which are smaller programs that provide specific capabilities. A watchdog is a background program that watches for a known failure signal, and here it watches the main program's log, which is a record of events and errors. When it sees the relevant transport error, it changes a restart marker in the settings for the affected server. The main program notices that setting change and starts the server again, while a 15 second cooldown prevents repeated changes during the restart.

#### How it works
First, a system service, meaning a background program managed by the operating system, follows the main program's log. Watching the log provides direct evidence that a communication failure occurred.
The watchdog waits for a line that specifically reports an MCP transport error. A transport error means that communication between the main program and the tool server failed, and using this signal avoids restarting a server merely because it is still starting.
When the matching error appears, the watchdog increases the affected server's restart marker in both relevant configuration files. A configuration file is a settings file, and the marker is a value whose change tells the main program that a restart is requested.
The main program watches its configuration and sees that the marker changed. It then stops treating the server as permanently failed and respawns it, meaning it starts a new server process.
The watchdog waits 15 seconds before allowing another marker change for the same recovery sequence. This order matters because the server may still be restarting, and repeated changes could cause restart loops or marker ping-pong.
The recovery was tested by deliberately stopping the code-search server and checking that the error appeared, the marker changed, and the server returned without a person editing the settings. This test checks the complete chain rather than only one component.

#### What the measurements mean

##### verified end to end: SIGTERM to the code-search server produced a transport error, the watchdog bumped the marker and opencode respawned the server with no human intervention
What was measured: This records one complete test. SIGTERM is an operating-system request to stop a program; the test confirmed that stopping the server caused a communication error, triggered the watchdog, changed the restart marker, and caused the main program to start the server again without a person intervening.
What it supports: This directly supports that the tested recovery sequence worked from forced server termination through automatic restart.
What it does not prove: It does not prove recovery for every possible failure, every server, repeated failures, or long-term reliability.

##### 7 of 8 servers tolerate the restart marker argument without any code change; code-search needed one patch to strip the flag before argparse
What was measured: Seven out of eight servers can receive the restart marker information without changes to their code. The code-search server required one code change to remove the extra flag before argparse, which is the Python tool that reads command-line options.
What it supports: This directly supports the stated compatibility result for eight servers and identifies the one server that needed a change.
What it does not prove: It does not prove that all eight servers recover successfully in every situation or that the required code change has no side effects.

#### The honest limit
The evidence validates one forced-stop recovery and reports compatibility for eight servers, but it does not measure recovery time, recovery success over many trials, behavior during repeated failures, or failures that do not produce the expected log line. The system depends on the main program noticing the configuration change and on the server accepting the restart information.
Current status: Verified. A transport failure was used to verify automatic recovery on code-search.
- LINK: [Inventory →](/cv/)

### Narration-driven episode analysis autopilot

#### The problem this system addresses
Planning the images for an episode used to require a person to read the narration and decide what shots were needed. This system prevents the process from silently using the same image search for every shot and prevents a mismatch between the narration timing and the written visual plan.

#### What the system does
This system starts with the spoken script and turns it into a visual plan. It transcribes the narration, meaning it converts spoken audio into written words, and divides those words into beats, where a beat is one small idea or section. It then maps each beat to shot needs and gives each need its own search questions. The builder checks that the number and timing of planned beats match the real narration before production continues.

#### How it works
First, the narration is generated. Starting with narration matters because the visuals are meant to support what is actually said.
The narration is transcribed into text. Transcription creates a written version that later programs can inspect without a person listening to the whole recording.
The text is split into beats. Each beat represents one meaningful part of the narration, making it possible to plan a visual for each idea rather than treating the whole episode as one block.
The beats are mapped to shot needs. A shot need is a request for one visual moment, such as a particular subject, action, or setting.
Each shot need receives its own query list. A query is a search request used to find possible source images. This step is essential because using identical queries for every need caused the source stage to place the same candidate set in each folder and left many needs without usable selections.
The brief is written after the narration and beat count are known. The builder refuses a mismatch between the brief timings and the narration, so this order prevents a plan based on an incorrect number of beats.

#### What the measurements mean

##### the per-need query rule was learned after a rebuild where identical queries left half the shot needs with an empty candidate set
What was measured: This records a failure observed during a rebuild: when identical search queries were used, half of the shot needs had no candidate images available for selection. The unit is half of the shot needs, not half of all episodes or images.
What it supports: It directly supports that identical queries caused a candidate-availability failure and that separate queries were needed per shot need.
What it does not prove: It does not give the total number of shot needs, the exact failure rate across all episodes, or whether the new rule always succeeds.

##### the brief must be written after the narration so the beat count matches, because the builder refuses on a mismatch
What was measured: This states a workflow rule: the written visual brief must be created after narration analysis so its beat count matches the narration. The builder is the program that checks this relationship and refuses to continue when the counts differ.
What it supports: It directly supports that the builder enforces a narration and brief count match.
What it does not prove: It does not measure how often mismatches occur, whether the beat boundaries are meaningful, or whether the final visual choices are good.

#### The honest limit
The source does not measure transcription accuracy, beat-splitting accuracy, time saved, the number of episodes planned, or the percentage of shot needs that ultimately receive suitable images. It also does not show that the system understands the narration as well as a human.
Current status: Production. Narration drives beats, shot needs and the analysis plan.
- LINK: [Workflow →](/products/workflow/)

### Reels ingestion and frame extraction pipeline

#### The problem this system addresses
Reference videos stored only in a URL list are hard to manage because the system cannot tell which items are finished and which failed. This pipeline prevents completed work from being repeated and makes an item-specific failure visible instead of silently losing it.

#### What the system does
This system reads a list of video links and processes each link through downloading, frame extraction, and JSON export. Frame extraction means saving still images from a video, while JSON is a plain text format for structured data. A SQLite database stores the status and details for each reel, and dated folders and log files keep outputs and step-by-step records organized.

#### How it works
The shell orchestrator reads the URL list. A shell orchestrator is a command script that runs several programs in a defined sequence.
Before processing an item, the system checks the master database. The database record contains the reel identifier, link, duration, download location, status, error message, and processing time.
If the database says the reel is already complete, the system skips it. This order matters because checking status before downloading avoids repeating work.
If the reel is not complete, the system downloads it. The downloaded file becomes the input for later steps.
The system extracts frames from the downloaded video and writes them to a dated folder. The date helps separate one processing run from another.
The system exports structured information as JSON and writes a log for each step. Logs are written records of what a program did, which makes troubleshooting possible when a step fails.
The database is updated with success or failure. Recording an error message makes the failure visible and lets a later run decide what needs attention.

#### What the measurements mean

##### 577 of 577 frames analysed, 23 of 23 JSON exports, 12 generations logged
What was measured: This records that 577 frames had analysis results, all 23 expected JSON exports were present, and 12 generations or processing runs were logged. The units are frames, JSON export files, and logged generations.
What it supports: It directly supports the reported completion counts for frame analysis and JSON export, plus the presence of 12 generation log records.
What it does not prove: It does not prove that the frame analysis was accurate, that every downloaded video was processed successfully, or that the 12 logged generations were all successful.

##### 23 reels tracked in the sqlite master database and 577 frame files on disk
What was measured: The database contained 23 reel records, and the frame directory contained 577 image files. The units are tracked reels and extracted frame files.
What it supports: It directly supports the observed counts of tracked reels and frame files.
What it does not prove: It does not prove that the 23 reels were unique, that every frame was useful, or that the database status matched the actual contents of every file.

#### The honest limit
The source does not measure download success rate, processing time per reel, storage use, frame quality, duplicate frames, or whether the JSON exports were later used. It also does not state whether all 23 reels were published or analyzed correctly.
Current status: Production. Reference clips move from download to frame and JSON exports with status tracking.
- LINK: [Inventory →](/cv/)

### Mullay brand media generation pipeline

#### The problem this system addresses
Brand imagery can look inconsistent when the wrong image model is used for a particular job or when prompts are based on guesswork. This system prevents one model from being used for every task and records practical rules learned from observed image failures.

#### What the system does
This system creates brand images from reference photos and produces related angle sheets and edits. It routes each job type to a chosen image model: flux-2 for creating a hero image from a reference, and gpt-image-2 for angle sheets and edits to an existing photo. Uploading a reference, creating a task, checking its progress, and downloading the result are separate steps so a failure can be located. The pipeline also records prompt and quality rules intended to improve face consistency and avoid background problems.

#### How it works
The system identifies the job type first. A job type is the purpose of the image request, such as creating a main image, making several angles, or editing an existing photo.
For a hero capture from a reference, it routes the task to flux-2. Routing means choosing a particular model according to a rule rather than choosing one arbitrarily.
For an angle sheet or an edit of an existing photo, it routes the task to gpt-image-2. Keeping these choices separate matters because the source reports different models for different uses.
The system uploads the reference or source image, creates an image task, checks the task until it is ready, and downloads the result. Separating these steps makes it possible to tell whether failure happened during upload, task creation, waiting, or download.
It uses high quality settings because lower settings produced plastic-looking skin in observed tests. This is a practical configuration based on a measured failure, not a general claim about every image.
It places the face instruction early in the prompt and uses a grey background. These choices were adopted because earlier prompt terms receive more emphasis in the observed setup and white backgrounds were reported to bleed into the image.

#### What the measurements mean

##### 475-line pipeline specification, 184-line image runner and 131-line video runner
What was measured: This counts lines in three files: 475 lines in the written pipeline specification, 184 lines in the image-running program, and 131 lines in the video-running program. The unit is a source-code or document line.
What it supports: It directly supports the recorded size of those three files at the time of measurement.
What it does not prove: It does not measure quality, maintainability, reliability, or how much of the code is actively used.

##### flux-2 image-to-image confirmed working at about 5 credits and about 30 seconds for face lock
What was measured: This records one observed flux-2 image-to-image run that was reported as working, using about 5 service credits and about 30 seconds for face lock. A credit is the service's usage unit, and face lock means preserving the reference person's facial identity in the generated result.
What it supports: It directly supports the reported cost and elapsed time for that observed run.
What it does not prove: It does not establish an average cost, average time, success rate, or consistent face preservation across many images.

#### The honest limit
The source does not measure identity consistency across a large sample, image acceptance rate, total spend, video output quality, or whether the routing rules work for every job. The reported timing and cost are from an observed case, not a broad benchmark.
Current status: Production. Image and video jobs are routed by task rather than by one preferred model.
- LINK: [Workflow →](/how/)

### OAP social-dynamics training application

#### The problem this system addresses
A training curriculum needed structured examples of social dynamics, but those examples were not available in a drillable format. The application is intended to prevent the source material from remaining an unorganised collection of videos.

#### What the system does
This application examines YouTube videos and extracts examples related to social dynamics. It uses Whisper, a speech-transcription system, to turn spoken audio into text that can be searched or processed. The extracted examples are placed into cards that a learner can review. The application also records the cost of each extraction step so the expense of processing is visible.

#### How it works
The system begins with 796 videos selected as source material. These videos are the raw input from which possible training examples are found.
It transcribes spoken content with Whisper. Transcription means converting speech in an audio or video recording into written text, which makes the content easier for later processing.
The extraction process identifies and stores examples of social dynamics. An extraction record is a stored result describing what was found from a source item.
The system seeds 1,217 examples into the training application. Seeding means inserting the prepared examples so the application can display and review them.
The examples are turned into review cards, and 1,207 cards are marked due. A due card is one the learner is currently scheduled to review.
Each extraction step writes a cost log. A cost log is a record of processing expenses, and writing it per step makes it possible to inspect where the total cost came from.
The project is recorded as built end to end but never used in a live session. This distinction matters because a completed implementation is not the same as demonstrated real-world use.

#### What the measurements mean

##### 1,217 examples seeded and 1,207 cards due, status built end to end and never used
What was measured: The application contains 1,217 inserted training examples, of which 1,207 are currently marked for review. The project status says the full build exists but has not been used in a live session.
What it supports: It proves the application was populated with a substantial set of review material and that its recorded status is unused in live training.
What it does not prove: It does not prove that the examples are accurate, useful, or effective for learning.

##### 796 YouTube videos mined for social-dynamics examples
What was measured: The extraction process examined 796 videos as source material for finding social-dynamics examples.
What it supports: It proves the stated size of the source-video collection used by the process.
What it does not prove: It does not prove that every video produced a useful example or that the extracted examples were reviewed for correctness.

##### 734 extraction records in oap_extractions.json and 3 per-step cost logs
What was measured: The stored extraction output contains 734 records, and the project has 3 separate logs that record costs for processing steps.
What it supports: It proves the project has 734 recorded extraction results and three cost-log files or streams as counted in the source.
What it does not prove: It does not prove that the records cover all 796 videos or that the cost logs contain complete or accurate financial amounts.

#### The honest limit
The application has never been used in a live session. The source does not measure learner outcomes, example quality, transcription accuracy, review completion, or total processing cost. The difference between 796 videos and 734 extraction records is not explained by the available facts.
Current status: Scaffold. The application was built end to end but has never been used in a live session.
- LINK: [Inventory →](/cv/)

### Static portfolio site generator and design system

#### The problem this system addresses
A portfolio assembled by hand can become inconsistent, difficult to update, and hard to regenerate after project information changes. This system prevents pages from drifting apart visually and prevents supported motion features from hiding content for visitors whose browsers do not support them.

#### What the system does
This system builds a static portfolio site from project README files. A static site is a collection of already generated web files that can be served without running application code for each visitor. The generator applies one shared type scale, spacing rhythm, and color palette so pages follow the same design system. It also checks reduced-motion preferences and browser support before showing certain animations, while keeping the content visible when those features are unavailable.

#### How it works
The generator reads project README files. A README is a project document containing descriptions and evidence that can be turned into page content.
It creates the site pages from that source information instead of relying on separately hand-edited pages. This order matters because one source reduces the chance that different pages tell conflicting stories.
The design system applies shared text sizes, spacing measurements, and colors. A design system is a set of repeated visual rules that keeps pages consistent.
Motion is placed behind a reduced-motion check. This check respects a visitor's request for less movement and prevents animation from being forced on that visitor.
Motion also requires an animation-timeline support check. A browser feature check asks whether the visitor's browser can perform the animation correctly.
If either check fails, the content remains visible without depending on the motion. This matters because unsupported animation should remove decoration, not the information itself.
The site is measured against performance targets for loading, interaction delay, and layout movement. These are targets, not proof that every visitor experiences those values.

#### What the measurements mean

##### 181 commits and 23 generated index pages
What was measured: This records 181 saved Git changes and 23 generated web pages named index pages. The unit is commits for the first number and generated HTML pages for the second.
What it supports: It directly supports the recorded repository history size and the number of generated index pages.
What it does not prove: It does not prove that all pages are correct, accessible, fast, or regularly updated.

##### live site returns HTTP 200 at https://iamtamilore.github.io
What was measured: This records an HTTP 200 response from the live website. HTTP 200 is a web server response meaning the requested page was successfully returned to the checking tool.
What it supports: It directly supports that the checked website responded successfully at that time.
What it does not prove: It does not prove that every page works, that the content is correct, or that visitors experience the stated performance targets.

#### The honest limit
The source does not provide measured LCP, INP, or CLS results. These are web performance measurements for loading, interaction delay, and layout movement, and only the target values are recorded. It also does not measure accessibility results, browser coverage, visitor numbers, or conversion outcomes.
Current status: Published. This site is generated from the project sources under one design system.
- LINK: [This site →](/)

### AI tooling site with a measured text-rendering test

#### The problem this system addresses
Image models often struggle to render exact words, especially when the words are long or arranged like a sign or price board. This system prevents a general opinion about text rendering from being presented as a broad fact by testing three different text situations and recording cost and time.

#### What the system does
This system builds a static site that describes AI coding and tooling workflows. It also runs a small image test using gpt-image-2-text-to-image. The test creates a short label, a sentence, and a price board layout, then stores the result, service cost, and wall-clock time, meaning the actual elapsed time from starting to finishing. The site also records model routing research so another person can repeat the reasoning.

#### How it works
The site build reads structured content and produces static web files. This keeps the published site predictable and means visitors do not need the build program running.
The test harness defines three text cases: a short label, a sentence, and a price board layout. A test harness is a small program that runs the same kind of experiment in a repeatable way.
Each case is sent through the same image model. Using one model for all three cases makes the comparison about the different text situations rather than changing the model between cases.
The system records the generated result, cost, and elapsed time for each case. Recording these values makes the test more useful than a visual opinion alone.
The results are described as a sample rather than a failure rate. Three cases can show what happened in those three cases, but they cannot establish how the model behaves on all possible text.

#### What the measurements mean

##### 3 test cases at 6 credits each, 66 to 71 seconds per image, balance 816 to 798 credits
What was measured: The test used three cases. Each case cost 6 service credits, each image took between 66 and 71 seconds, and the recorded service credit balance went from 816 to 798 credits across the run. The units are test cases, credits, seconds per image, and remaining credits.
What it supports: It directly supports the recorded number of cases, per-case cost, observed time range, and balance change.
What it does not prove: It does not prove an average time beyond that range, a general cost for other prompts, or that the balance change came only from these tests unless the surrounding account activity was controlled.

##### 3 of 3 cases exact by eye, on a sample of 3 which is a sample size and not a failure rate
What was measured: A visual review judged all three generated test cases to match the intended text exactly. The unit is three reviewed cases. The source explicitly treats three as a sample size rather than a general failure or success rate.
What it supports: It directly supports that the three tested examples were judged exact by eye.
What it does not prove: It does not prove that the model has a general 100 percent text accuracy rate or that it will work equally well on other text.

#### The honest limit
The test covers only three cases and uses visual judgment rather than a large automated text comparison. It does not measure performance on other fonts, languages, image sizes, layouts, prompts, or repeated runs. The source also does not measure whether the site attracts or helps users.
Current status: Published. A dated text-rendering test records the model, cost and wall time.
- LINK: [Inventory →](/cv/)

### Local Real-ESRGAN 4K upscaling queue

#### The problem this system addresses
Reference images needed larger versions without sending them to a hosted image service. This system prevents failed downloads or failed enlargements from disappearing silently by recording each result in a ledger.

#### What the system does
This system downloads images from a link queue and enlarges them locally using Real-ESRGAN. Real-ESRGAN is an image enlargement program that uses a trained model to create a higher-resolution version. The program uses the local graphics processor, called a GPU, and processes the image in 512-pixel tiles so large images can be handled in sections. A done ledger records success or failure, while a staging folder separates work in progress from completed output.

#### How it works
The system reads the next link from the queue and downloads the source image. Keeping downloading as its own step makes download failures different from enlargement failures.
It places the source or working file in a staging area. A staging area is a temporary location for files that are not yet complete.
Real-ESRGAN x4plus processes the image locally. The x4 setting means the intended output dimensions are four times the input dimensions in each direction, subject to the program's actual behavior.
The program uses a tile size of 512 pixels. Tiling divides a large image into smaller sections so the GPU needs less memory at one time.
When processing finishes, the system writes the enlarged image to the output area and records the result in the done ledger. If processing fails, it records FAILED rather than pretending the item is complete.
The ledger is checked on later runs so recorded work can be distinguished from work that still needs attention.

#### What the measurements mean

##### done ledger holds 4 records of which 2 are marked FAILED, and the output directory currently holds 0 files
What was measured: The ledger contains four processing records, two of which have the exact status FAILED. The output directory contains zero enlarged image files at the measurement time.
What it supports: It directly supports that four records were tracked, two were marked failed, and no output files were present in the checked directory.
What it does not prove: It does not prove why the two items failed, whether the other two records were successful, or whether output files existed elsewhere.

##### RealESRGAN_x4plus at tile size 512
What was measured: This records the configured enlargement model, RealESRGAN_x4plus, and the tile size of 512 pixels. The tile size is the maximum section size used for one local processing step.
What it supports: It directly supports the configured model and tile setting.
What it does not prove: It does not prove that the model produced usable images, completed successfully, or improved visual quality.

#### The honest limit
At the time measured, the output directory held zero files and two of four ledger records were marked FAILED. The source does not measure image quality, completion time, GPU memory use, retry success, or whether any enlarged images were ultimately delivered.
Current status: Incomplete. The outcome ledger records failures and the output directory is empty.
- LINK: [Inventory →](/cv/)

### Mobile media idea bank with a convention contract

#### The problem this system addresses
Saved clips and links can become useless when the reason for saving them is not recorded. This system prevents media ideas from becoming an unsearchable pile by giving each item a standard folder, metadata, and command-based way to find it.

#### What the system does
This system stores media ideas in a JSON index and gives every idea its own directory. JSON is a plain text format for structured information, and an index is a list that points to the stored entries. The bank tool provides separate commands to collect media, create a new entry, display an entry, and search entries. When a clip is saved, ffmpeg extracts still frames so the item can be understood without opening the full video.

#### How it works
The system creates one entry directory for each saved idea. Keeping media and its notes together makes the entry portable and reduces the chance that the explanation becomes separated from the file.
It writes the entry's identifying information into the JSON index. The index lets the tool find entries without scanning every folder manually.
The harvest command brings in saved media, while the new command creates an entry. Separating these actions makes it clear whether the system is importing existing material or starting a new record.
The show command displays an entry and the search command finds entries using their stored information. Separate commands keep each task simple for a beginner or future maintainer.
ffmpeg extracts frames from a saved clip during capture. These still images provide quick visual references and are created at the time the clip enters the bank.
A conventions document explains the required entry format. This matters because a written agreement lets another person add or search items without needing the original author's memory.

#### What the measurements mean

##### 1 entry currently indexed, id 2026-08-12-1800-test1
What was measured: The JSON index currently contains one media entry, identified by the exact recorded identifier 2026-08-12-1800-test1. The unit is one indexed entry.
What it supports: It directly supports that one entry was listed in the index at the measurement time.
What it does not prove: It does not prove that the entry contains complete metadata, useful media, extracted frames, or a representative amount of real use.

##### 1 commit: Phase 0, the idea-bank loop
What was measured: The repository history contains one Git commit, described as Phase 0, the idea-bank loop. The unit is one saved change in the repository.
What it supports: It directly supports that the repository has one recorded commit with that description.
What it does not prove: It does not prove that the tool is finished, stable, tested broadly, or used by anyone else.

#### The honest limit
The system currently has only one indexed entry and one commit, so its usefulness at larger scale is not validated. The source does not measure search accuracy, duplicate handling, backup safety, extracted frame quality, or use by people other than its author.
Current status: Scaffold. The tool and convention contract exist. Only a test entry is indexed.
- LINK: [Inventory →](/cv/)

### Multi-agent trading scan dashboard

#### The problem this system addresses
A reinforcement-learning scan produced results that needed to be viewed without running the expensive training process again. The dashboard is designed to prevent users from needing a live server or a fresh training run just to inspect the latest stored results.

#### What the system does
This is a static dashboard, meaning a collection of web files that can display information without a continuously running application server. It reads a JSON file, which is a structured text format for data, containing the latest trading results. The results cover 36 assets and use different learning agents for different asset groups. The dashboard presents risk-adjusted results based on Sharpe ratio and includes a hidden Markov model signal, which is a statistical estimate of hidden market conditions.

#### How it works
The training or scanning process produces a results file containing the latest measurements. The dashboard does not rerun that process when someone opens the page.
The page loads the JSON results file. JSON is used here as a simple, structured handoff between the process that produced the results and the page that displays them.
The system associates SAC, TD3, or PPO with each asset class. These are different reinforcement-learning methods, meaning methods that learn actions by receiving rewards from an environment.
The reward is based on Sharpe ratio. Sharpe ratio is a risk-adjusted measure that compares return with variability, so the learning objective considers both gain and risk rather than gain alone.
A hidden Markov model contributes a regime signal. This model estimates an underlying market state, such as a possible market condition, from observed data even though the state itself is not directly visible.
The browser displays the stored results as charts or tables. Because the page only reads the prepared file, it has no server dependency in the described setup.

#### What the measurements mean

##### 36 assets across the result set, with SAC, TD3 and PPO routed per asset class
What was measured: The stored results cover 36 financial assets, and the dashboard records which of the SAC, TD3, or PPO learning methods is used for each asset class.
What it supports: It proves the displayed result set has 36 assets and includes three named agent types assigned by asset class.
What it does not prove: It does not prove that the agents were evaluated fairly, that the asset data is current, or that any strategy would be profitable in live trading.

##### the dashboard is a static read of latest_v2.json with no build step and no server code
What was measured: The dashboard directly reads the file named latest_v2.json, does not require a separate compilation or packaging step, and contains no server-side application code.
What it supports: It proves the described dashboard can display stored results as a static client-side page without a running server.
What it does not prove: It does not prove the stored results are correct, recent, secure, or automatically refreshed.

#### The honest limit
The dashboard only displays the latest stored result file and does not itself validate the training results. The source does not report live trading performance, backtesting methodology, data freshness, dashboard usage, or whether the market-regime signal improves decisions. No claim about profitability is supported by these metrics.
Current status: Prototype. The dashboard routes models by asset class. It does not establish trading quality.
- LINK: [Inventory →](/cv/)

### Personal site and links hub

#### The problem this system addresses
Contact information and public profiles can be difficult to share when they are scattered across several services. This system prevents that information from depending on a single platform by placing links, a QR code, a contact file, and related assets in one static page.

#### What the system does
This system is a static links page, meaning the page is made from files that can be served directly without a running application. It includes a QR code, which is a square image that a phone can scan, a vCard contact file, which stores contact details in a format address books can import, and a wallpaper set. Git records changes to the public files over time.

#### How it works
The system stores the page and its assets as ordinary static files. This keeps the runtime simple because the visitor's browser only needs to download and display the files.
It provides a QR code that points people toward the public contact surface. This gives a quick phone-based route without requiring someone to type a long address.
It provides a vCard file for contact details. A vCard lets a visitor save the information into a contacts application rather than copying each field by hand.
It includes the wallpaper set as another downloadable public asset. Keeping these assets with the page gives the public profile one consistent home.
Git tracks changes to the repository. This creates a history of edits and makes it possible to see when the public surface changed.

#### What the measurements mean

##### 38 commits
What was measured: This counted 38 saved changes in the Git history of the links hub. The unit is repository commits.
What it supports: It directly supports that the repository contains 38 recorded commits at the measurement point.
What it does not prove: It does not prove that the page is popular, complete, secure, accessible, or currently working in every browser.

#### The honest limit
The source does not provide a live availability check, visitor count, scan count, download count, accessibility review, or evidence that the vCard imports correctly in every address book application. It also does not measure whether the public links lead to active profiles.
Current status: Published. Contact details, social identities and QR assets are published.
- LINK: [Contact →](/meet/)

### Multi-agent MCP layer across eight servers

#### The problem this system addresses
Several AI clients needed access to the same models, memory, code search, web lookup, and browser capabilities, but separate integrations could behave differently. The system prevents that integration drift by routing these capabilities through one shared tool protocol and by automatically restarting a failed server.

#### What the system does
This system is a shared MCP layer, where MCP is a standard protocol that lets an AI client call tools provided by other programs. It connects 8 servers in the project configuration and 6 servers in the global configuration. The servers provide model access, event logging, memory search, code search, browser control, media generation, local image generation, and Wikipedia lookup. A watchdog is a small monitoring program that checks whether a service is alive and restarts it when it has stopped.

#### How it works
First, the project configuration lists the 8 MCP servers needed for that project. A configuration is a set of settings that tells an AI client which external services it may call.
The global configuration lists 6 shared servers for use outside the project. Keeping a common global set reduces the chance that each client is configured differently.
The model gateway is exposed as an MCP server. A model gateway is a service that sends requests to language or media models while applying shared budgets, caching, and usage records.
The memory and event-log servers store information and tool activity in shared systems. This lets different clients use the same history and makes activity easier to inspect.
The code-search server retrieves relevant parts of the machine's indexed code, while the browser server performs web actions. Each capability remains in its own server so it can be updated or tested separately.
The Wikipedia server handles narrow factual lookups, and the media-generation servers handle remote or local generation tasks. Separating these jobs keeps specialized behavior out of the model gateway.
The watchdog checks the health of the MCP servers. When a server is terminated or otherwise stops responding, the watchdog starts it again without waiting for a person.
The AI client calls the servers through MCP rather than using a different custom integration for each client. This common route matters because budgets, caches, logs, and tool behavior can then be shared.

#### What the measurements mean

##### 8 MCP servers in the project config: unified-log, kie-ai, code-search, claude-mem, ask, comfyui, wikipedia, browser
What was measured: The project configuration lists 8 MCP servers with the names unified-log, kie-ai, code-search, claude-mem, ask, comfyui, wikipedia, and browser. Each server is a program that offers one or more callable tools through MCP.
What it supports: This directly supports the number and names of servers listed in the project configuration.
What it does not prove: It does not prove that every server was running, reachable, or successfully used.

##### 6 MCP servers in the global config: unified-log, ask, comfyui, wikipedia, browser, code-search
What was measured: The global configuration lists 6 MCP servers with the names unified-log, ask, comfyui, wikipedia, browser, and code-search.
What it supports: This directly supports the number and names of servers listed in the global configuration.
What it does not prove: It does not prove that every client loads the configuration correctly or that the servers provide complete functionality.

##### the ask MCP exposes the model gateway, so a chat reaches models through the same budget, cache and ledger as the command line
What was measured: The ask MCP server provides model access to a chat client through the same model gateway used by the command line. A budget limits usage, a cache reuses previous results when allowed, and a ledger records usage or spending.
What it supports: This directly supports that chat requests use the shared gateway mechanisms rather than a separate model route.
What it does not prove: It does not provide numerical evidence about cost savings, cache hit rate, model quality, or request volume.

##### the watchdog recovers a dead server with no human intervention, verified end to end on a SIGTERM
What was measured: A test sent SIGTERM, which is an operating-system signal asking a process to stop, and the watchdog restored the stopped server without a person restarting it.
What it supports: This directly supports that automatic recovery worked in that end-to-end test.
What it does not prove: It does not prove recovery from every failure type, that recovery is always fast, or that no requests are lost during a restart.

#### The honest limit
The inventory does not measure overall uptime, request success rate, restart time, data loss during recovery, model quality, or the number of clients actively using each server. It also does not validate that all eight project servers and all six global servers work together under sustained load.
Current status: Verified. Eight servers are configured. Recovery was verified end to end on code-search.
- LINK: [Inventory →](/cv/)

### Five-gate post-render video QA gate with on-screen caption presence and caption-to-script alignment

#### The problem this system addresses
A rendered video could pass checks on its input files and still contain visible or audible defects in the final file. This system prevents specific shipped failures, including missing or mistimed captions, long silence, missing music, wrong visual content, and repeated frames, by checking the rendered video itself.

#### What the system does
This system runs five checks on the completed episode directory and refuses the episode if any check fails. It uses audio and video inspection tools, image-pixel checks, caption timing data, and a vision-capable language model, which is a model that can inspect video and return a structured judgment. It also aligns spoken-word timings with the script so captions use the script's spelling while retaining timing information from the transcription. OCR, or optical character recognition, is used only as an advisory measurement and does not decide whether an episode passes.

#### How it works
The gate first locates the rendered video by trying the expected file name and then any MP4 file in the episode directory. This matters because a directory name and a video file name may differ.
Gate 1 checks audio and duration. It uses ffprobe, a tool that reads media properties, to compare the video duration with the voice duration plus the expected call-to-action card. It allows a 3.0 second difference. It also searches for trailing silence longer than 3.5 seconds and refuses the episode when no music bed is present.
Gate 2 checks the caption timing and text data. It compares captions with nine known phonetic transcription errors and refuses the first matching corruption. It also measures the gap between the last caption word and the end of the voice track and refuses a gap greater than 2.0 seconds.
Gate 3 checks burned-in captions in the actual rendered pixels. It samples at the midpoint of each caption word, looks for bright glyph pixels next to dark outline pixels, checks the expected accent colour, and requires at least 1200 glyph pixels on a qualifying frame. At least 80 percent of narration frames must contain a caption. This comes after the caption-track check because a correct text file does not prove that text was visibly drawn into the video.
Gate 4 sends the actual rendered video to a vision model in groups of 6 shots. The model returns a structured judgment for each shot about the subject, narration beat, and orientation. Missing judgments for any shot cause refusal. The model chain tries minimax-m3 first and gemini-3.1-pro-preview second, with different answer budgets based on observed reasoning failures.
Gate 5 checks for repeated frames. It refuses consecutive duplicate frames, any reused frame, or a repeated block where shots 1 to 16 match shots 17 to 32.
Before Gate 2, the alignment stage compares transcription tokens with script tokens using a sequence matcher. It keeps the transcription timings but replaces transcription spelling with the script spelling. If word counts differ, it distributes the original time span across the script words according to word length, and it saves the original transcription separately.

#### What the measurements mean

##### the gate runs 5 checks, refuses the episode if any one of them fails, and exits with a non-zero code so the caller cannot treat a failure as a pass
What was measured: There are five checks. One failed check is enough to refuse the episode. A non-zero exit code is a computer signal meaning the command ended in failure, which prevents a calling process from treating the result as successful.
What it supports: The gate has five refusal checks and communicates failure to the calling process.
What it does not prove: It does not prove that each check detects every possible defect or that the caller always handles the non-zero code correctly.

##### the measured thresholds are 3.5 seconds maximum trailing silence, 3.0 seconds maximum duration delta against voice plus the call to action card, and a 2.0 second maximum gap between the last caption word and the end of the audio
What was measured: The rendered video may have no more than 3.5 seconds of silence at the end. Its duration may differ from voice plus the call-to-action card by no more than 3.0 seconds. The last caption word may end no more than 2.0 seconds before the audio ends.
What it supports: These are the explicit refusal thresholds for trailing silence, total duration difference, and caption-ending gap.
What it does not prove: It does not prove that the thresholds are perceptually ideal or that shorter gaps and duration differences never indicate a defect.

##### 9 known transcription phonetic corruptions are refused by name, including Akasa for Akaza and Muzan for Muzan
What was measured: The gate lists nine named transcription mistakes that are refused. The examples show that similar-sounding or incorrectly recognized names can be blocked.
What it supports: Nine specific transcription corruption patterns are included in the refusal list.
What it does not prove: It does not prove that all possible transcription mistakes are covered.

##### 34 anachronism terms are listed as forbidden objects for the era check
What was measured: The system has a list of 34 terms representing objects considered wrong for the episode's historical setting. An anachronism is something shown in a time period where it does not belong.
What it supports: Thirty-four forbidden terms are available for the era-related visual check.
What it does not prove: It does not prove that the vision model detects every anachronism or that every listed term is found correctly.

##### run against the rendered Inosuke episode the gate returned FAIL on 2 findings: the MP4 is 39.7 seconds against an expected 44.0 seconds for voice plus call to action, and no music bed was present. The caption, on-screen caption and frame loop gates returned PASS
What was measured: One rendered episode had two failures. Its video was 39.7 seconds long instead of the expected 44.0 seconds, and no music bed file was found. The caption timing, visible-caption, and repeated-frame checks passed for that run.
What it supports: The gate detected those two defects and separately passed the three named checks in that run.
What it does not prove: It does not prove that the remaining checks passed, that the episode was fixed, or that the same findings occur in all episodes.

##### run against the rendered Rengoku episode the gate returned FAIL on the same 2 findings: the MP4 is 39.4 seconds against an expected 43.9 seconds, and no music bed was present
What was measured: A second rendered episode was 39.4 seconds instead of the expected 43.9 seconds, and it had no music bed. The two duration figures and the two expected figures are the ones the gate reported.
What it supports: The gate detected the same two categories of defect in this second run.
What it does not prove: It does not prove that other checks passed or that all episodes have these defects.

##### ffprobe confirms the duration finding is real and not a gate arithmetic error. The Rengoku MP4 is 39.366667 seconds and the voice track is 39.851125 seconds, and no music_act*.wav file exists anywhere under the zenpai episode directory. The rendered file is short by roughly the length of the call to action card, which was never appended
What was measured: An independent media inspection measured the video at 39.366667 seconds and the voice track at 39.851125 seconds. No file matching the music bed pattern was found. The result indicates that the call-to-action portion was not added to the final video.
What it supports: The duration and missing-music findings were supported by direct media inspection rather than only by gate arithmetic.
What it does not prove: It does not prove why the call-to-action append step failed or whether other episodes have the same cause.

##### the frame loop gate correctly refused a deliberately duplicated frame sequence: 4 shots on the same frame produced Duplicate frames: {'a.jpg': 4}
What was measured: A test video used the same image for four shots. The gate reported that image four times and refused the sequence.
What it supports: The frame loop gate can detect repeated use of the same frame in a controlled test.
What it does not prove: It does not prove that all kinds of visually similar but non-identical loops are detected.

##### the caption gate correctly refused a truncated caption track: a track ending at 0.5 seconds against 40.0 seconds of audio produced a gap greater than 2 seconds
What was measured: The captions stopped at 0.5 seconds while the audio lasted 40.0 seconds. The resulting gap was far above the 2.0 second limit, so the gate refused the episode.
What it supports: The caption timing gate detects a caption track that ends substantially before the audio.
What it does not prove: It does not prove that small timing errors or incorrectly worded captions are always detected.

##### the Inosuke episode has 17 shots with 17 distinct frames, which is why the frame loop gate passes on it
What was measured: The episode contains 17 shots and each shot points to a different frame. The frame loop check therefore found no reused frame in that list.
What it supports: That episode's shot list had 17 distinct frame references.
What it does not prove: It does not prove that the frames are visually appropriate, that consecutive frames are sufficiently different, or that the final video contains no repeated encoded frames.

##### the caption alignment stage rewrote 702 transcribed words into 698 script words across 4 episodes, changing 16 spans
What was measured: Across four episodes, the alignment process changed the caption word list from 702 transcription words to 698 script words and modified 16 groups of words. A span is a contiguous section of text treated as one changed region.
What it supports: The alignment stage made the stated number of word and span changes in those four episodes.
What it does not prove: It does not prove that every change was correct or that the new timings match human judgments.

##### the Genya episode is where the alignment stage earns its place: the transcription heard 'moves on' where the script says 'Muzan', heard 'Muzon' 3 times for 'Muzan', and heard 'niche-in' for 'nichirin'. All of those printed on screen before the stage ran
What was measured: Before alignment, the captions contained several transcription errors: a phrase was used instead of the name Muzan, Muzon appeared three times instead of Muzan, and niche-in appeared instead of nichirin. These errors were visible in the captions before correction.
What it supports: The alignment stage addressed concrete caption spelling errors in that episode.
What it does not prove: It does not prove that the alignment stage catches every named-entity error or that the corrected text is always semantically right.

##### the Giyu episode transcript heard 'Hashiro' for 'Hashira' and 'Sanami' for 'Sanemi', and the Rengoku episode heard 'core' for 'corps'. All three were on screen before the alignment stage ran
What was measured: Three additional transcription errors appeared in captions before alignment: Hashiro instead of Hashira, Sanami instead of Sanemi, and core instead of corps.
What it supports: The alignment stage had additional real spelling errors to correct in those episodes.
What it does not prove: It does not prove that the corrected captions were independently reviewed or that similar errors are absent elsewhere.

##### the alignment stage keeps timings monotonic and keeps every word inside the file, and writes the pre-alignment transcription to words_whisper.json so the original timings stay recoverable
What was measured: Monotonic timings mean each word starts at or after the previous word rather than moving backward. The stage keeps every word within the audio file and saves the original transcription separately for later comparison.
What it supports: The alignment implementation includes timing-order, file-boundary, and original-data preservation rules.
What it does not prove: It does not prove that the resulting word boundaries are perceptually accurate.

##### the visual gate now executes a real model call and refused the rendered Inosuke episode on shot 3. The shot carries the narration 'He taught himself his breathing style by watching how they charged', and the frame on that shot is an empty traditional Japanese interior with no character in it and no animal in it. The frame was opened and looked at, and the finding is right
What was measured: The visual check sent the episode to a model and refused shot 3 because the narration described a character learning by watching animals charge, while the image showed an empty interior with neither a character nor an animal.
What it supports: The visual gate can make a refusal based on a mismatch between spoken content and the rendered image, and this finding was manually confirmed.
What it does not prove: It does not prove that the model will reliably detect all subject, beat, or orientation problems.

##### the shots are judged in groups of 6, one model call per group, and a group whose verdicts do not cover every shot in it is a refusal rather than a pass. Asked for 17 verdicts in one call, the model returned a single summary object and used the whole 4000 token budget
What was measured: The system sends no more than six shots in one model request. It requires one result for every shot in that group. A test asking for 17 results produced only one summary and consumed all 4000 allowed output tokens, so grouping is used to reduce incomplete responses.
What it supports: The implementation has six-shot grouping and refuses incomplete model coverage.
What it does not prove: It does not prove that six is the optimal group size or that every grouped response is accurate.

##### one group of 6 shots costs 0.0054 USD at 12287 input tokens and 1468 output tokens, so a 17 shot episode costs about 0.016 USD to check
What was measured: One six-shot model request used 12,287 input tokens and 1,468 output tokens and was recorded at 0.0054 USD. Three such groups are needed for 17 shots, giving an approximate total of 0.016 USD.
What it supports: This records the measured cost and token use for one model group and an approximate cost for a 17-shot episode.
What it does not prove: It does not prove a fixed future price, because model prices, token counts, retries, and group contents can change.

##### the frame loop gate now reads the episode under test from any working directory. A probe episode with 4 shots on one frame is refused from a working directory that holds no shots.json, and the rendered Inosuke episode passes from a working directory that holds a duplicate frame shot list
What was measured: The gate uses the episode directory supplied to it instead of assuming that the current terminal directory contains the episode files. A controlled test showed that a four-shot repeated frame was refused even when launched elsewhere, and a separate run showed the rendered episode could pass while the current directory contained unrelated shot data.
What it supports: The frame loop check reads the intended episode location rather than relying on the launch directory.
What it does not prove: It does not prove that every other gate is independent of the current directory.

##### the visual gate uses minimax-m3 first, the cheapest model in the registry that declares video in its input modalities, and gemini-3.1-pro-preview second. The model the gate used before, qwen3-vl-235b, cannot take a video at all, so the file has to go through the video argument rather than the image argument
What was measured: The visual gate first tries minimax-m3 and then gemini-3.1-pro-preview. The first model is selected as the least expensive registered option that accepts video. The previously used qwen3-vl-235b model does not accept video input, so the rendered file must be sent through a video input field rather than as a still image.
What it supports: The model order and input type were chosen using declared video-input support and cost information.
What it does not prove: It does not prove that the cheapest model is the most accurate or that the fallback is always available.

##### the cheap video model still burns its answer budget on reasoning about one live call in five, even with reasoning turned off. The failed call spent the whole 4000 token budget and returned no output, and the gateway logged it as a reasoning burn. The second model in the chain exists because of that measurement
What was measured: In one out of five live calls in the measured sample, the cheaper model used all 4000 output tokens for internal reasoning and returned no usable answer, even though reasoning was disabled in the request.
What it supports: The measured sample contained a serious incomplete-response failure and motivated the fallback model.
What it does not prove: It does not establish a permanent one-in-five failure rate or explain whether the rate changes with different videos.

##### the second model needs a larger answer budget than the first. At 4000 tokens it wrote 3996 tokens and never reached the JSON array, and at 12000 tokens it returned a clean 6 object verdict array on a live call
What was measured: The fallback model failed to finish its structured answer with a 4000-token limit, using 3996 tokens before the required array. With a 12000-token limit, it returned six verdict objects as required for a six-shot group.
What it supports: The larger answer budget resolved the observed incomplete-response case for that live call.
What it does not prove: It does not prove that 12000 tokens will always produce valid output or that the extra budget improves visual accuracy.

##### the rendered file is found by one resolver used by every gate, trying the directory name first and then any mp4 in the episode folder. EP_INOSUKE lives in ep_inosuke, so the exact name never matches and the fallback is what finds the file
What was measured: A shared file resolver first tries a file name based on the episode directory and then searches for an MP4 in that directory. In the cited example, the exact name did not match, so the fallback search located the rendered video.
What it supports: All gates use a common fallback strategy for locating the rendered MP4.
What it does not prove: It does not prove that the fallback always selects the correct file when a directory contains multiple MP4 files.

##### the trailing silence check measures the rendered file now. Before the fix, ffmpeg was pointed at a path rebuilt from the directory name that did not exist, and the parser required the silence start and the silence end on one line while ffmpeg prints them on separate lines, so the value stayed at zero on every episode
What was measured: The silence check previously examined an invalid reconstructed file path and expected ffmpeg output in the wrong layout. Because of those two problems, it reported zero silence for every episode. The fix makes it inspect the actual rendered file and handle separate silence-start and silence-end lines.
What it supports: The earlier zero values were caused by file-location and output-parsing defects, and the check was changed to address them.
What it does not prove: It does not provide a measured before-and-after accuracy rate for silence detection.

##### the on-screen caption check found the defect it was built for. A copy of the Rengoku episode with the captions stripped out passes the caption track gate because words.json is untouched, and fails the on-screen caption gate with 0 of 40 narration frames captioned
What was measured: A test copy removed visible caption pixels but left the caption timing file unchanged. The text-file check passed because its input was unchanged, while the pixel check found zero captioned frames out of 40.
What it supports: The on-screen pixel check detects missing burned-in captions that a caption-track check alone cannot detect.
What it does not prove: It does not prove that the pixel check detects every styling, spelling, or partial-caption defect.

##### the on-screen caption check passes on every real render tested: 40 of 40 narration frames captioned on the Rengoku episode, 40 of 40 on the Inosuke episode, and 40 of 40 on the anime hive render
What was measured: For each of the three tested real renders, all 40 sampled narration frames met the pixel criteria for containing a visible caption.
What it supports: Those three tested renders met the measured visible-caption coverage rule.
What it does not prove: It does not prove that captions are spelled correctly, readable at every moment, or correct on untested renders.

##### the on-screen caption check was confirmed by eye as well as by the script. The Rengoku frame at 5.0 seconds shows the phrase AND HE DID with DID in yellow, the stripped copy at the same timestamp shows the black bar with no text, and the anime hive frame at the word midpoint 5.61 seconds shows MADARA in red
What was measured: Manual inspection agreed with the automated pixel check. One frame showed expected text and colour, the stripped comparison showed the empty caption background, and another channel showed its expected red caption.
What it supports: The automated result matched visual inspection for these sampled frames.
What it does not prove: It does not prove that manual inspection was performed for every frame or every episode.

##### the on-screen caption check is channel aware and refuses a cross-channel mismatch. The anime hive profile against the zenpai render reached 42 percent coverage and the zenpai profile against the anime hive render reached 0 percent, both below the 80 percent floor
What was measured: Using the wrong channel profile caused only 42 percent coverage in one direction and 0 percent in the other. Both results were below the required 80 percent coverage, so the mismatches were refused.
What it supports: The gate can distinguish the tested channel caption positions and colours and can reject a cross-channel profile.
What it does not prove: It does not prove that the profiles remain correct after future builder changes.

##### the caption band and the caption colours are measured from the builders, not guessed. The zenpai builder draws at 0.667 of the frame height with a 5 pixel black stroke, and the anime hive builder draws at 0.78 of the frame height with a 16 pixel stroke, and the rendered frames were opened and checked against those constants
What was measured: The caption band is the vertical area where captions are expected. One builder places captions at 0.667 of frame height with a 5 pixel black outline, while the other places them at 0.78 of frame height with a 16 pixel outline. Rendered frames were inspected against those settings.
What it supports: The profiles use measured builder settings rather than arbitrary guesses for the tested channels.
What it does not prove: It does not prove that all caption colours, sizes, or future builder versions are covered.

##### the OCR text match stays advisory because the measurement says so. The masked OCR containment hit rate was 73.2 percent for zenpai and 21.4 percent for the anime hive, and a tight bounding box made it worse at 65.9 percent and 11.9 percent, so a text mismatch cannot refuse an episode without producing false refusals on correct ones
What was measured: OCR matched the expected text in 73.2 percent of one channel's cases and 21.4 percent of the other's. Restricting OCR to a tighter region reduced the rates to 65.9 percent and 11.9 percent. Because correct captions were missed often, OCR is not used as a refusal rule.
What it supports: The measured OCR approach was too unreliable to serve as a hard pass or fail condition in these tests.
What it does not prove: It does not prove that a different OCR engine, image treatment, or language setting would perform the same way.

##### the gate's own docstring used to claim that the visual gate checked caption styling against the brief. No check read the caption pixels and no check looked at a banner, so the claim was false. An abstract syntax tree parse of the old gate confirmed that the caption gate and the frame loop gate never touched the MP4, and the caption-stripped copy passed the caption gate
What was measured: The old documentation claimed a visual caption-style check, but the old code did not inspect rendered pixels or the banner. A program-structure inspection confirmed that the relevant old checks did not open the MP4, and a caption-stripped test passed the old caption gate.
What it supports: The previous implementation did not enforce the caption-pixel behavior described in its documentation.
What it does not prove: It does not prove that every other old documented behavior was false or that the new implementation has no similar documentation gaps.

#### The honest limit
The five-gate system measures selected audio, caption, pixel, model, and frame-loop failures, but it does not measure every possible visual or semantic defect. OCR is intentionally advisory because its measured hit rates are weak. The vision model can fail to return complete results, and the evidence includes live-call failures and model-budget adjustments. The reported costs and pass results come from particular tests, not a universal accuracy or price guarantee. The source does not provide a complete human-labeled benchmark, recall, precision, F1 score, or independent measurement of all gate errors.
Current status: Production. Five checks refuse an episode when one check fails.
- LINK: [Workflow →](/products/workflow/)
- LINK: [See the Agent Foundations CV](/cv/)
- LINK: [Inspect the logs](/provenance/)

---

## PAGE: /case-studies/

- LINK: [index](/)
- LINK: [work](/work/)
- LINK: [cases](/case-studies/)
- LINK: [process](/process/)
- LINK: [gallery](/gallery/)
- LINK: [cv](/cv/)
- LINK: [episodes](/products/)
cases

## Case studies
Four deep cases. Each one starts with the failure it prevents, then explains the mechanism, the measured result and the limit.

### What a case study is
A case study explains one engineering decision from the problem through the mechanism, the measured result and the limit. It does not treat a working file as proof by itself. The reader should be able to check what was built, what it was compared against and what remains unproven.

### TermsGuard AI

#### The problem
Similarity alone can treat a sentence that says data is not sold in the same way as a sentence that says it is sold.

#### The decision
Rule checks run around the similarity result, and every flagged clause carries the reference material used to justify it.

#### The evidence
102 hand-labelled reference clauses
4,527 searchable reference chunks
Matching-only fallback when the model service is unavailable
- LINK: [Read the case study](/p/termsguard/)

### Smart Medical Records

#### The problem
A similarity search across many patients can return the wrong patient's note when both records use similar words.

#### The decision
The patient's identifier is applied before ranking, so other patients' notes are excluded before the model can read them.

#### The evidence
30 adversarial probes designed to retrieve another patient's note
30 of 30 passed and zero leaked
Four services on one private network
- LINK: [Read the case study](/p/clinical-rag/)

### Care Agent

#### The problem
A wrong automatic route sends a customer to a team that cannot resolve the complaint.

#### The decision
The confidence gate sends uncertain tickets to a person instead of forcing every ticket into one of five categories.

#### The evidence
210 labelled tickets, with 42 in each category
40 of 42 held-out tickets routed correctly
Confidence threshold of 0.55 before human escalation
- LINK: [Read the case study](/p/care-agent/)

### Image QA Gate

#### The problem
An image can have the correct pose while showing the wrong identity. Accepting that image is the more serious error.

#### The decision
A Siamese network compares identity features, and the threshold was selected on validation data before the sealed test was opened.

#### The evidence
90 sealed test pairs
Precision 1.00, recall 0.82 and F1 0.90
Pixel difference F1 0.59 and kNN F1 0.26 as simpler comparisons
- LINK: [Read the case study](/p/image-qa/)
- LINK: [Browse all 37 systems](/work/)
- LINK: [See the Agent Foundations CV](/cv/)

---

## PAGE: /process/

- LINK: [index](/)
- LINK: [work](/work/)
- LINK: [cases](/case-studies/)
- LINK: [process](/process/)
- LINK: [gallery](/gallery/)
- LINK: [cv](/cv/)
- LINK: [episodes](/products/)
process

## Process walkthroughs
The order of work, explained slowly. These pages show what enters each process, what changes at each step and where a check refuses the result.

### What a process walkthrough is
A process walkthrough shows the order of work. It explains what enters the process, what each step changes, where a check refuses the result and what leaves the process. A pipeline is a sequence of automated steps. A workflow also includes the decisions and handovers made by people or services.

### How I build things
This walkthrough explains the general method used across the media systems: define the failure, choose the gate, keep the evidence, and check the result before release.

#### What it shows
The order of production steps
Where human review enters
Why the order is part of correctness
- LINK: [Open the walkthrough](/how/)

### Episode production workflow
This page follows one short-form episode through source selection, frame filtering, rotation correction, model selection, cropping, verification and rendering. The order is fixed because a later check depends on an earlier correction.

#### What it shows
Each pipeline stage and its input
The quality checks that can refuse a render
Contact sheets for the selected shots
- LINK: [Open the workflow](/products/workflow/)

### Episode blueprint
This specification records the production contract: what a shot must contain, how narration becomes timed beats, which checks run before rendering and what the finished file must contain.

#### What it shows
The input and output contract
The gate sequence
The known failure modes
- LINK: [Open the blueprint](/products/blueprint.html)

### Human rating systems
The rating interfaces let a reviewer compare candidates against a fixed rubric. They are tools for recording judgements, not proof that the chosen candidate is correct.

#### What it shows
How a candidate enters the review
How a verdict is recorded
Why model agreement is not the same as validity
- LINK: [Open the first rater](/rater/)
- LINK: [Browse all 37 systems](/work/)
- LINK: [See the Agent Foundations CV](/cv/)

---

## PAGE: /gallery/

- LINK: [index](/)
- LINK: [work](/work/)
- LINK: [cases](/case-studies/)
- LINK: [process](/process/)
- LINK: [gallery](/gallery/)
- LINK: [cv](/cv/)
- LINK: [episodes](/products/)
gallery

## Evidence gallery
Diagrams, evaluation tables, episode stills, contact sheets and raw logs, grouped by the question each artefact can answer.

### What a gallery is here
This gallery groups evidence by what it proves. An architecture diagram shows how a system is separated. A confusion matrix shows which mistakes remained after a decision rule. A contact sheet shows which frames entered a video. A raw log shows that a scheduled job ran and recorded an outcome. Nothing is included only as decoration.

### Clinical architecture
Shows the API, database, model service, patient boundary and audit path used by the clinical retrieval system.
- LINK: [Open the case study](/p/clinical-rag/)

### Routing confusion matrix
Shows which ticket categories the classifier confused during the held-out evaluation.
- LINK: [Open the case study](/p/care-agent/)

### Image QA curves
Shows how the acceptance threshold changed the balance between correct acceptances and missed pairs.
- LINK: [Open the case study](/p/image-qa/)

### Contract analysis architecture
Shows the first-stage classifier, reference retrieval, model verification and visible fallback path.
- LINK: [Open the case study](/p/termsguard/)

### Episode gallery
Published episodes, production stills, narration timing and the quality-check records for the rendered files.
- LINK: [Open the episode gallery](/products/)

### Process contact sheets
The selected frames for a short-form episode, shown as a sequence so the visual rhythm and repeated-frame checks can be inspected.
- LINK: [Open the contact sheets](/products/workflow/contact-sheets.html)

### Channel gallery
The creative channels built with the production pipeline, including the visual identity and published work for each channel.
- LINK: [Open the channel gallery](/channels/)

### Provenance logs
Raw evidence that scheduled work ran, media calls were recorded and evaluation decisions were written down.
- LINK: [Open the logs](/provenance/)
- LINK: [Browse all 37 systems](/work/)
- LINK: [See the Agent Foundations CV](/cv/)

---

## PAGE: /skim/

- LINK: [index](/)
- LINK: [work](/work/)
- LINK: [cases](/case-studies/)
- LINK: [process](/process/)
- LINK: [gallery](/gallery/)
- LINK: [cv](/cv/)
- LINK: [skim](/skim/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
- LINK: [episodes](/products/)
- LINK: [channels](/channels/)
- LINK: [jobs](/jobs/)
skim  ·  60 seconds

## Four projects, what each one prevents going wrong.
Four projects, the failure mode each one defends against, the one number a recruiter
  needs. The full write-up is one click deeper on every entry. Behind them sits the
  complete index of 37 verified systems.
All 37 systems → The four case studies → How the pipelines run → The evidence gallery →
- LINK: [All 37 systems →](/work/)
- LINK: [The four case studies →](/case-studies/)
- LINK: [How the pipelines run →](/process/)
- LINK: [The evidence gallery →](/gallery/)

### TermsGuard AI
Reads the small print in a privacy policy and flags the unfair parts.
- LINK: [Try the live demo →](https://newtazer-terms-guard-ai.hf.space)
- LINK: [Full write-up →](/p/termsguard/)
- LINK: [Code →](https://github.com/iamtamilore/terms-guard-ai)

### Customer Care Process Automation
Two bots that took over two jobs I used to do by hand every morning at Huawei.
- LINK: [Full write-up →](/p/care-agent/)
- LINK: [Code →](https://github.com/iamtamilore/customer-care-automation)

### Smart Medical Records Engine
A doctor asks in plain English and gets the answer out of the patient's own file.
- LINK: [Full write-up →](/p/clinical-rag/)
- LINK: [Code →](https://github.com/iamtamilore/agentic_rag_fastapi)

### Image QA Gate
Catches the moment an AI-generated model stops being the same person.
- LINK: [Full write-up →](/p/image-qa/)
- LINK: [Code →](https://github.com/iamtamilore/campaign-image-qa)
One more system, indexed without a public write-up. RL vs Genetic Algorithm for Surge Pricing: tested on 637,976 real Boston ride
    records, GA +21.4% over flat pricing, Q-learning +18.2%, hand-written rule
    +7.9%. State space kept small enough to read. It sits in the work index with no
    case study page. Report (PDF) →
- LINK: [Report (PDF) →](/assets/docs/surge_pricing_report.pdf)

### What this page is and is not
This is: the 60-second skim. Each entry leads with what the project prevents going wrong, what that mistake costs, the headline number, and the honest limit. The full write-up is one click away.
This is not: the full write-up. The full write-ups have the architecture, the diagrams, the per-section honest limits, and the reproduction instructions. They are linked from each entry.
This is not: the complete index. The work index holds all 37 verified systems with what each one prevents and what it does not prove. This page is the 60-second slice of the four that have full write-ups.
- LINK: [The work index](/work/)
This is not: an alternative to the homepage. The homepage is the project card grid for someone choosing what to read. This page is for the recruiter who wants to read more than a card but less than a write-up.
- LINK: [← Home](/)
- LINK: [Work index](/work/)
- LINK: [CV](/cv/)

---

## PAGE: /jobs/

- LINK: [index](/)
- LINK: [cv](/cv/)
- LINK: [skim](/skim/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
- LINK: [episodes](/products/)
- LINK: [channels](/channels/)
- LINK: [jobs](/jobs/)

## Applications
Sending an application is not an outcome. Record what came back, and the rate tells you whether
      the CV is the problem or the targeting is.
A rate on fewer than 10 applications is noise, not a signal.

### Log an application

### Record what came back
This is the part the old tracker never did. A rejection, a silent no, or a screening call, logged the
      day you hear it.

### Closing soon

### Ledger
State lives in this browser only. Export before you clear it, or before switching devices.

### Open and worth a look
Researched 23 October 2026. Every row says where its date came from. A date marked unverified came from web research and the URL was reachable, which proves the page exists and not that the
      date is right. Open it before you plan around it. Deadlines shown as seen on own dashboard are the ones you
      read yourself, which is the stronger source.

### Already closed
Recorded so the same door is not knocked on twice. Four of these were good fits and are gone for
      this cycle, which is the real argument for checking the calendar rather than working from memory.

### Fit watch
Roles close without warning, and the ones that close first are often the best fit. This list is
      what your saved-and-forgotten applications looked like: gone, and gone quietly.

---

## PAGE: /p/termsguard/

- LINK: [← All work](/#termsguard)

## TermsGuard AI
8 min read
Reads the small print and flags the parts that are unfair to you, in
plain English.
Built by Taiwo Alabi. MSc Artificial Intelligence,
National College of Ireland
Live demo: https://newtazer-terms-guard-ai.hf.space Source: https://github.com/iamtamilore/terms-guard-ai
- LINK: [https://newtazer-terms-guard-ai.hf.space](https://newtazer-terms-guard-ai.hf.space)
- LINK: [https://github.com/iamtamilore/terms-guard-ai](https://github.com/iamtamilore/terms-guard-ai)
Cosine similarity alone marks "we do not sell your data" as a
violation, so the classifier proposes and a model rules. 102
hand-labelled reference clauses, a 4,527-chunk retrieval index, and up
to 15 flagged clauses sent to Claude for verification per analysis. The
retrieval index is data-governance and GDPR context rather than
regulation, so the tool shows you the passage a flag was drawn from, not
an article it claims to quote.
What this evidences: critiquing model quality and
evaluation design. The interesting problem is not detection, it is that
a purely semantic classifier gets negation exactly backwards, and what
you do about it.

#### Contents
The problem
- LINK: [The problem](#1-the-problem)
Results
- LINK: [Results](#2-results)
How it works
- LINK: [How it works](#3-how-it-works)
What it compares
against
- LINK: [What it compares
against](#4-what-it-compares-against)
Why similarity alone
is not enough
- LINK: [Why similarity alone
is not enough](#5-why-similarity-alone-is-not-enough)
The verification layer
- LINK: [The verification layer](#6-the-verification-layer)
Saying how sure it is
- LINK: [Saying how sure it is](#7-saying-how-sure-it-is)
Where it fails
- LINK: [Where it fails](#8-where-it-fails)
Unexpected finding
- LINK: [Unexpected finding](#9-unexpected-finding)
Honest limitations
- LINK: [Honest limitations](#10-honest-limitations)
Run it
- LINK: [Run it](#11-run-it)
Terms used in this
report
- LINK: [Terms used in this
report](#12-terms-used-in-this-report)
- LINK: [Try it](https://newtazer-terms-guard-ai.hf.space)
- LINK: [Read the detail pdf](/assets/docs/termsguard_writeup.pdf)
- LINK: [Check the code](https://github.com/iamtamilore/terms-guard-ai)

### 1. The problem
Reading every privacy policy an average internet user meets would
take roughly 244 hours a year. Nobody does it. So people agree to data
selling and tracking without knowing they have.
The problem is not that the documents are secret. They are published,
free, and legally binding. They are simply unreadable at the length and
density they are written, and the one clause that matters is buried
among forty that do not.

### 2. Results
The previous build reported that the model had verified each clause,
but the verifier had never actually run on the deployed service because
the Anthropic key had no credit, the except block swallowed the 400
error, and the app returned cosine scores while still reporting
llm_verification_enabled true, so a clause was labelled "Checked by the
model" when no model had looked at it. The fix added three routes for
the verifier tried in order with retry and a fallback model, and the
response now carries verification_source and verification_error so a
silent fallback is impossible, verified by a regression suite of twelve
inputs passing against the live build with the real model ruling. Two
real bugs were only found because the verifier started running: a benign
"refund policy" clause was flagged as an Art.82 violation, and a
politely worded third-party analytics clause was read as compliant
because asking permission was reasoning as lawful; the first is fixed by
the prompt stating generic commercial statements are not GDPR clauses,
and the second by the prompt stating that politeness does not change
what a clause does.

### 3. How it works
Text is split into individual clauses and de-duplicated. Each clause
is turned into a row of numbers by all-MiniLM-L6-v2 , then
compared by cosine similarity, a way of measuring how close two pieces
of text are in meaning, against labelled examples of fair and unfair
clauses. Anything that looks unfair then has GDPR context pulled for it
from a FAISS index (a fast lookup table built for exactly this kind of
search), and Claude Haiku double-checks the flag before it is shown.

### 4. What it compares against
The system carries 102 hand-labelled reference clauses: 52 examples
of fair terms and 50 examples of unfair ones. A new clause is scored by
how close it sits to each set.
Separately, a FAISS index holds 4,527 chunks of reference material on
data governance and GDPR. When a clause is flagged, retrieval pulls the
passage closest to it, so the reader can see the context the flag was
drawn from rather than taking the model's word.
That split matters. The labelled clauses and the similarity score
propose whether something might be a problem. The rule guards
and then the verifier decide. The GDPR corpus supplies why , and
it is the second half that makes a flag worth acting on.

### 5. Why similarity alone is
not enough
This is the part I would defend hardest in an interview.
Consider two sentences:
"We sell your personal data to third parties." "We do not sell your
personal data to third parties."
To a computer that only measures word patterns, these two sentences
look almost identical. They share nearly every word, the same grammar,
the same subject. So a system that judges purely by how similar the
words look will flag the second sentence, the reassurance, as a
violation , because it never actually checked which way the
sentence points.
So the pipeline carries a layer of explicit rule guards on top of the
similarity score:
Negation detection, for exactly the case above.
Protective-context detection, for clauses that describe a right
being granted rather than removed.
A children's-data check, because clauses about minors carry
obligations that generic similarity scoring does not weight
correctly.
Keyword boosting, for terms whose presence changes the reading
regardless of how the sentence embeds.
None of these are clever. They exist because I ran the
similarity-only version, read what it got wrong, and found the errors
clustered around cases where meaning is inverted by a single word.

### 6. The verification layer
When an API key is configured, Claude Haiku re-reads each flagged
clause and removes false positives before anything is shown to the
user.
The design decision worth noting is the fallback: with no key set,
the tool runs in matching-only mode rather than failing. It degrades to
a less precise version of itself instead of refusing to work, which
means the demo is always live and the tool is not hostage to a paid
dependency.
The trade-off is that a degraded mode has to announce itself, and the
earlier build did not. It returned cosine scores while still reporting
that the model had verified the clause, so a clause was labelled
"Checked by the model" when no model had looked at it. The response now
carries verification_source and verification_error , so a fallback shows up in the output
instead of hiding behind a flag that said true.

### 7. Saying how sure it is
Flags are tiered by confidence rather than presented as flat
verdicts, with thresholds at 0.55 for high and 0.45 for medium.
A document-level risk assessment then combines the proportion of
clauses flagged with the average confidence across them, so a policy
with two borderline flags is not reported the same way as one with
fifteen strong ones.
This is the same instinct that runs through my other projects: state
uncertainty rather than hide it behind a single number.

### 8. Where it fails
The retrieval corpus is mostly not regulation. Of
the 4,527 chunks, only about two percent cite a GDPR article at all. The
tool shows the passage a flag was drawn from and says it is context, but
a reader looking for a legal citation will not find one.
The rule guards are written patterns. Negation
detection, protective-context detection, the children's-data check and
keyword boosting cover inversion expressed the ways those patterns
cover. A clause that inverts meaning in a wording none of them matches
passes them.
The reference set bounds what similarity can see. A
new clause is scored against 52 fair and 50 unfair examples. An unfair
clause worded unlike all 50 scores low against both sets, and the
similarity stage does not fire at all.
Only 15 clauses reach the verifier per analysis. Anything flagged beyond that is presented on the similarity score alone,
with no model ruling behind it.
The regression suite is 12 cases. It exists to
catch the failures that were found, not to measure how much of the space
is covered.

### 9. Unexpected finding
The bugs that mattered were found by the part of the system that was
broken.
The verifier had never actually run on the deployed service, so for
as long as it was switched off, nothing checked whether the layers below
it were right. Switching it on exposed two real defects that had been
there the whole time: a benign refund-policy clause flagged as an Art.82
violation, and a politely worded third-party analytics clause read as
compliant because asking permission was being read as reasoning as
lawful.
Both were in the classifier and the prompt, not in the verifier. The
layer that was supposed to be the last word was the only thing that ever
asked the question.

### 10. Honest limitations
It is not legal advice. The page says so. It surfaces clauses worth
reading properly; it does not tell you your rights.
The 4,527 chunks in the retrieval index are reference material on
data governance and EU GDPR, of which only about two percent cite a GDPR
article at all. The retrieved passage is shown as context, not as the
article text, because most of the corpus is course material, not the
regulation.
A 12-case regression suite was measured live on 25 October 2026
against the deployed service with the real model ruling. One of the
cases ("We offer a refund policy") used to be flagged as an Art.82
violation by the cosine stage. The verifier correctly rejected it after
the fix. The remaining cases in the suite pass for reasons the
measurements cover: negation handled, French input left uncertain,
run-on sentences below the minimum length, and so on.
Politeness can read as consent. The prompt now states that the tone
of a clause does not change what it does.
This was a contributed project, not a solo build. My work was the
retrieval pipeline, the grounding, the rule guards and the latency
reduction.

### 11. Run it
Easiest is the live demo: https://newtazer-terms-guard-ai.hf.space
- LINK: [https://newtazer-terms-guard-ai.hf.space](https://newtazer-terms-guard-ai.hf.space)
Locally:
Optional, for the verification layer:
Stack: Python · Flask · sentence-transformers (MiniLM) · FAISS ·
Anthropic API · Docker

### 12. Terms used in this report
The terms below are defined the way this report uses them, for a
reader who wants to check the reasoning rather than take it on
trust.
Cosine similarity - a way of measuring how close
two pieces of text are in meaning, not just how many words they
share.
Embedding - turning a piece of text into a row of
numbers, so a computer can compare meaning mathematically instead of
just matching words.
FAISS index - a fast lookup table, built for
searching millions of embeddings for the closest match almost
instantly.
Negation - the word or phrase that flips a
sentence's meaning, like turning "we sell your data" into "we do not sell your data".
- LINK: [Smart Medical Records → wrong-patient retrieval](/p/clinical-rag/)
- LINK: [← All work](/#termsguard)
- LINK: [CV](/cv/)
- LINK: [GitHub](https://github.com/iamtamilore)
- LINK: [newalabitaiwo625@gmail.com](mailto:newalabitaiwo625@gmail.com)
- LINK: [LinkedIn](https://www.linkedin.com/in/tami-alabi/)
- LINK: [GitHub](https://github.com/iamtamilore)
- LINK: [work](/work/)
- LINK: [tracker](/jobs/)
- LINK: [bank](/bank-pwa/)

---

## PAGE: /p/clinical-rag/

- LINK: [← All work](/#clinical-rag)

## Smart Medical Records Engine
8 min read
Helps a doctor find the one thing in a patient file that matters,
before the appointment ends.
Built by Taiwo Alabi. MSc Artificial Intelligence,
National College of Ireland.
A doctor asks in plain English and gets the answer out of that
patient's own notes. The retrieval query carries the patient_id, so the
database filters by patient before it ranks by similarity, which is what
stops a different patient's note surfacing because it happens to be
worded the same way. Thirty adversarial probes designed to leak
cross-patient data, zero leaked, and the whole system runs on the
hospital's own machine so no patient record leaves it.
What this evidences: applying software architecture
principles under a hard constraint. The model is the easy part. Scoping
retrieval so the wrong patient cannot surface, and proving it, is the
system.

#### Contents
The problem
- LINK: [The problem](#1-the-problem)
What it does
- LINK: [What it does](#2-what-it-does)
How it works
- LINK: [How it works](#3-how-it-works)
The safety rail that
matters most
- LINK: [The safety rail that
matters most](#4-the-safety-rail-that-matters-most)
Who is allowed in
- LINK: [Who is allowed in](#5-who-is-allowed-in)
The data model
- LINK: [The data model](#6-the-data-model)
Why self-hosted
- LINK: [Why self-hosted](#7-why-self-hosted)
Verified:
thirty attempts to leak, zero leaks
- LINK: [Verified:
thirty attempts to leak, zero leaks](#8-verified-thirty-attempts-to-leak-zero-leaks)
Where it fails
- LINK: [Where it fails](#9-where-it-fails)
Unexpected finding
- LINK: [Unexpected finding](#10-unexpected-finding)
Honest limitations
- LINK: [Honest limitations](#11-honest-limitations)
Running it
- LINK: [Running it](#12-running-it)
Terms used in this
report
- LINK: [Terms used in this
report](#13-terms-used-in-this-report)
- LINK: [Read the detail pdf](/assets/docs/clinical_rag_writeup.pdf)
- LINK: [Check the code](https://github.com/iamtamilore/agentic_rag_fastapi)

### 1. The problem
A doctor has ten minutes with you.
Somewhere in your file, which might be three years of notes from
different visits, different doctors, different hospitals, there is a
line saying you reacted badly to a particular medicine.
Your doctor is about to prescribe you something. Do they remember
that line? Did they ever see it? Nobody reads three years of notes in
ten minutes.
That is the whole problem. Not a modelling problem, a retrieval
problem with a consequence attached.

### 2. What it does
A search box a doctor can talk to normally. They ask "has this
patient ever reacted badly to any medication?" and it answers from
that patient's own notes, showing the actual note it found the answer
in.
Three things make it trustworthy, and all three matter more than the
clever part:
It only reads one file. Not a similar patient's, not someone with
the same illness. Verified: section 8.
Records never leave the hospital. The model runs on the hospital's
own machine.
Every access is written down. If anyone asks who opened a patient's
file, there is an answer.

### 3. How it works
Four Docker Compose services on one private network. Orange marks
the controls that constrain what the system is allowed to do.
A question arrives at the service that handles requests. It passes
the login check, gets turned into a row of numbers by nomic-embed-text (so it can be compared for meaning, not
just matching words), and is used to search that one patient's notes in
the database. The matching notes are handed to a locally-running AI
model, llama3.1 , as its source material, and the answer
comes back quoting them directly.
Ingestion runs once as a separate service: it chunks the records,
embeds them, and loads them with their patient reference attached.

### 4. The safety rail that
matters most
Retrieval is scoped by patient before it ranks by
similarity.
This sounds like a detail. It is the whole design. A general vector
search over all notes would happily return another patient's record if
that record happened to be the closer semantic match, and it often
would, because two people with the same condition produce similar
notes.
So the filter is not a ranking preference applied afterwards.
Wrong-patient results are excluded from the candidate set entirely,
because the patient_id is a WHERE clause on the retrieval query rather
than a check run over the results. The column that makes it possible is
part of the schema, stored on the same row as the note it belongs to, so
a note cannot exist without one.

### 5. Who is allowed in
Doctors log in with JWT, a secure login token, and passwords are
never stored in readable form, only a scrambled version that can check a
password without keeping it.
The patient's name is substituted out of the question and the answer
before they are written to the query log, so the log holds [PATIENT_NAME] instead of the name. That redaction covers
the name only, and it runs at log time, after the model has already
answered. The notes themselves reach the model as they were
retrieved.
Every access writes an audit_log row against the doctor
who made it. A system handling medical records that cannot answer "who
looked at this, and when" is not deployable regardless of how well it
retrieves.

### 6. The data model
Notes are stored in SOAP format, subjective / objective / assessment
/ plan, because that is how clinicians already write them. Matching the
existing format matters more than choosing a neater one: it means
records can be ingested as they are.
Each note carries a vector(768) embedding on the same
row as its patient_id , so the scoping constraint and the
searchable content cannot drift apart.

### 7. Why self-hosted
Every model in this system runs locally through Ollama. No API calls,
no data sent out.
That decision costs accuracy. A hosted frontier model would answer
better. But patient records leaving a hospital network is not a
trade-off a hospital can make, so the ceiling on model quality is fixed
by the constraint, not the other way round.
The whole stack, API, database and language model, runs across four
Docker Compose services on one machine.

### 8. Verified:
thirty attempts to leak, zero leaks
The claim in section 4 is now tested rather than asserted. I made
thirty attempts to trick the live application into leaking another
patient's data, through the real path: signed in as a physician, asking
questions designed to pull another patient's notes into the answer.
Near-verbatim copies of a decoy patient's most distinctive lines.
Semantic twins of the same clinical facts. Broad fishing questions.
Queries naming the wrong patient outright.
Each attempt included a check to make sure it was a fair test: before
counting it, I ran the same search without the patient filter. In 30 out
of 30 attempts the wrong patient's note came back as the top result, so
every probe was one that would have failed without the scoping. With
scoping on, none of the thirty attempts leaked anything.
What this is not: a penetration test. No auth bypass was attempted,
no injection, no infrastructure attacks. It verifies the scoping design
through the application's own query path, which is the design this
system stands or falls on.
Reproduce:

### 9. Where it fails
Scoping trusts the caller. The query scopes on the
patient_id the request carries. The endpoint requires a valid doctor
token, but nothing checks that this doctor is entitled to that patient's
file. What the design guarantees is that one query cannot mix two
patients, not that a doctor can only reach their own patients.
Redaction covers the name, and it runs late. The
name substitution applies to the question and the answer as they are
written to the query log. The retrieved notes reach the model as they
were stored.
The leakage test covers one path. Thirty probes
through the retrieval path, as section 8 says. A different route into
the same data was not tested.
Answer quality is unmeasured. There is no labelled
benchmark, so the system proves it does not leak and does not yet prove
it answers well.

### 10. Unexpected finding
The part I did not expect was that the measurement that made the
claim credible came from the broken configuration.
"Zero leaks across thirty probes" is a weak sentence on its own,
because weak probes also produce zero leaks. So each probe was run
twice, once without the patient filter, to confirm it was a probe that
could actually leak. The unscoped baseline came back 30 out of 30, the
wrong patient's note on top every time. The scoped system returned none
of them. The number that carried the evidence was the one from the
system with the rail removed, not the one from the system with it in
place.

### 11. Honest limitations
It has not been tested with real clinicians. The retrieval works;
whether the interface fits a ten-minute consultation is unproven, and
that is the claim that matters.
The data is synthetic. Real notes are messier: abbreviations,
inconsistent formatting, scanned documents.
A local llama3.1 is weaker than a hosted model.
Accepted deliberately, but it means answers on complex questions are
less reliable than the retrieval underneath them.
No formal evaluation set. Leakage was the priority, and it is
measured in section 8: zero leaks across thirty attempts to trick it.
Answer quality against a labelled benchmark remains unmeasured.

### 12. Running it
Ollama pulls nomic-embed-text and llama3.1 on first run. Ingestion loads the records and builds the embeddings.
Nothing reaches the internet after the model pull.
Stack: Python · FastAPI · PostgreSQL + pgvector · Ollama (llama3.1) ·
Docker Compose · JWT

### 13. Terms used in this report
The terms below are defined the way this report uses them, for a
reader who wants to check the reasoning rather than take it on
trust.
Embedding - turning a patient's note into a row of
numbers, so a computer can search by meaning instead of just matching
words.
JWT - a secure login token a doctor gets after
signing in, checked on every request.
PII - personal details like a name or address that
could identify someone.
Retrieval - the step of finding and pulling in the
right piece of information before answering a question, rather than the
AI guessing from memory.
Scoping - restricting a search to one patient's own
records before it even starts, rather than searching everyone and
filtering afterwards.
- LINK: [← TermsGuard AI grounding against hallucination](/p/termsguard/)
- LINK: [Care Agent → the confidence gate](/p/care-agent/)
- LINK: [← All work](/#clinical-rag)
- LINK: [CV](/cv/)
- LINK: [GitHub](https://github.com/iamtamilore)
- LINK: [newalabitaiwo625@gmail.com](mailto:newalabitaiwo625@gmail.com)
- LINK: [LinkedIn](https://www.linkedin.com/in/tami-alabi/)
- LINK: [GitHub](https://github.com/iamtamilore)
- LINK: [work](/work/)
- LINK: [tracker](/jobs/)
- LINK: [bank](/bank-pwa/)

---

## PAGE: /p/care-agent/

- LINK: [← All work](/#care-agent)

## Customer Care Process
Automation
8 min read
Two bots built to replace two manual back-office jobs, with a rule
about when not to decide.
Built by Taiwo Alabi. MSc Artificial Intelligence,
National College of Ireland.
One bot validates records against rules with known right answers, the
other reads complaints and routes them to one of five back-end teams.
TF-IDF and Naive Bayes reach 95.2% on 42 held-out tickets, and below
0.55 confidence the ticket goes to a human instead of being forced
through. Forty-two tickets is a thin evaluation, and the 0.55 threshold
was set by judgement about the cost of a needless escalation rather than
swept.
What this evidences: critiquing model quality and
evaluation design. A headline accuracy is not the result. What the agent
does with the tickets it is unsure about is.
The model section is 5, the escalation decision is 6, where it fails
is 8, and the unexpected finding is 9.

#### Contents
The problem
- LINK: [The problem](#1-the-problem)
Results
- LINK: [Results](#2-results)
The process, before
- LINK: [The process, before](#3-the-process-before)
The process, after
- LINK: [The process, after](#4-the-process-after)
How the triage agent
works
- LINK: [How the triage agent
works](#5-how-the-triage-agent-works)
The
decision that matters: when not to decide
- LINK: [The
decision that matters: when not to decide](#6-the-decision-that-matters-when-not-to-decide)
The second bot:
rule-based validation
- LINK: [The second bot:
rule-based validation](#7-the-second-bot-rule-based-validation)
Where it fails
- LINK: [Where it fails](#8-where-it-fails)
Unexpected finding
- LINK: [Unexpected finding](#9-unexpected-finding)
Honest limitations
- LINK: [Honest limitations](#10-honest-limitations)
Running it
- LINK: [Running it](#11-running-it)
Terms used in this
report
- LINK: [Terms used in this
report](#12-terms-used-in-this-report)
- LINK: [Read the detail pdf](/assets/docs/care_agent_writeup.pdf)
- LINK: [Check the code](https://github.com/iamtamilore/customer-care-automation)

### 1. The problem
Hundreds of customer complaints sorted by hand every morning, on a
Nigerian mobile network. A person reads each one and decides which
back-end team it belongs to: SIM activation, network, refunds, payment
and billing, or general.
Two things go wrong. People misroute tickets, because after the
sixtieth complaint they all start to read the same. And the customer
waits while their ticket finds the right desk, then waits again once it
gets there.
A misroute is not a small error. It costs the customer days, and the
business a second handling pass on work it already paid for once.

### 2. Results
The accuracy number is the least interesting thing here. What matters
is what the agent does with the tickets it is not confident about, which
is section 6.

### 3. The process, before
I mapped out the existing process as a flowchart, using BPMN 2.0 (a
standard way of drawing business processes), before writing any code.
That order was deliberate: it meant the automation replaced a process I
actually understood, rather than my assumption of one, and the process
model is what made the manual touchpoints explicit enough to decide
which were worth automating.

### 4. The process, after
The redesign splits the work by the kind of decision each part
requires. Field validation has known correct answers, so it goes to
rules. Reading a complaint and inferring intent does not, so it goes to
a classifier. The confidence gate sits between the classifier and the
outcome.

### 5. How the triage agent works
Ticket text is turned into numbers with TF-IDF, a way of scoring each
word by how much it tells you about the topic, then sorted into one of
the five routing categories by Naive Bayes, a simple, fast classifier
built on word probabilities.
Naive Bayes is a deliberate choice rather than a default. The corpus
is 210 tickets, which is small, and Naive Bayes is reliable at that
size. I did not benchmark a heavier model against it, so this choice is
argued from the corpus size and from inspectability, not from a measured
comparison. It is also inspectable: I can see which words drive a
routing decision, which matters when somebody asks why a ticket went
where it did.
Per-class precision, recall and F1: precision is how often a
category the model picked was actually right, recall is how many of the
true cases for that category it actually caught, and F1 blends the two
into one number.
Reported per category rather than as a single figure, because a
router that is strong on common categories and weak on rare ones is a
different system from one that is evenly good, and an average hides that
difference.
Where the classifier confuses one team with another.
The matrix shows where errors concentrate. Confusion between
neighbouring categories is a routing problem worth fixing; errors
scattered evenly would suggest the features themselves are too weak, and
that is not the pattern.

### 6. The decision
that matters: when not to decide
A classifier will always return an answer. Asked to route a ticket it
has never seen anything like, it will still pick the closest of the five
categories and report a number. That is the failure mode worth designing
against.
So the agent does not have to answer. Any ticket scoring below 0.55
confidence is flagged needs_human_review and escalated
instead of routed.
The economics justify it. A needless escalation costs an agent about
five minutes. A confident misroute costs the customer days. When one
error is two orders of magnitude more expensive than the other, the
correct system is one that escalates freely, and I would rather
report a lower automation rate than a higher misroute rate .
The 0.55 is a design setting, not a tuned one. It was chosen from
that cost asymmetry and held fixed, because sweeping it without real
escalation costs would only produce a number that looks measured without
being measured.

### 7. The second bot:
rule-based validation
The validator checking each record against its
requirements.
The second automation produces the daily customer creation report: it
reads the customer records, validates each field, writes the clean
report to Excel and Word, and writes everything that failed validation
to a separate exceptions file.
This half is deliberately not machine learning. These are hard
business rules with known correct answers, so a classifier would
introduce uncertainty where none needs to exist. Choosing not to use ML
is as much a design decision as choosing to.
Outputs: routed_tickets.csv , validation_exceptions.csv , and the daily report in both .xlsx and .docx .

### 8. Where it fails
Neighbouring categories swap. The confusion matrix
shows two errors, both between P_BILL and REFUND. Billing and refund
complaints share vocabulary, and the model picked the wrong one of the
two in each case. Every other prediction landed on the diagonal.
The gate moves uncertainty, it does not remove it. A ticket below 0.55 is not answered more accurately, it is handed to a
person. The cost shifts from a misroute to an escalation, and the
accuracy figure stops counting it either way.
The rule bot only catches the rules it was written
with. Five checks are implemented, so a record that breaks
something outside them, a well-formed value that belongs to the wrong
segment, passes through clean.
The evaluation is 42 tickets. 95.2% is 40 of 42, so
one ticket moves the figure by more than two points. The error pattern
is the finding here; the percentage is not.

### 9. Unexpected finding
The part I did not expect was how much one half of the project
resisted machine learning. I went in planning to automate two jobs with
models. Mapping the first one as a process, before writing any code,
made its manual touchpoints explicit, and what that showed was that the
daily customer report has known correct answers. A classifier there
would add uncertainty where none is needed, so that half became rules
with named exceptions instead.
The useful output of the process model was not the diagram. It was
the decision to leave machine learning out of one of the two jobs.

### 10. Honest limitations
The corpus is small and synthetic. 210 generated tickets across five
categories. Real complaints are messier: code-switching, abbreviations,
several issues in one message. The generator was written to be
realistic, but it is still a generator.
42 test tickets is a thin evaluation. 95.2% means 40 of 42, so a
single ticket moves the figure by more than two points. The pattern of
errors is more informative than the headline number.
Five categories is a simplification. A real network has more teams
and less clean boundaries between them.
The confidence threshold was set by judgement, not swept. 0.55
reflects the cost asymmetry described above, but a proper sweep against
real escalation costs would be the honest way to fix it.

### 11. Running it
Seeded, so results reproduce on every run.
Stack: Python · scikit-learn (TF-IDF, Naive Bayes) · pandas · BPMN
2.0 · openpyxl · python-docx

### 12. Terms used in this report
The terms below are defined the way this report uses them, for a
reader who wants to check the reasoning rather than take it on
trust.
Precision - of the tickets the model sent to a
category, how many actually belonged there. Low precision means it's
wrong a lot when it says "this one".
Recall - of the tickets that truly belonged to a
category, how many the model actually caught. Low recall means it misses
real cases.
F1 score - one number that blends precision and
recall, so a model can't look good by being great at only one of
them.
TF-IDF - a way of scoring each word in a ticket by
how much it tells you about the topic, turning text into numbers a model
can use.
Naive Bayes - a simple, fast classifier that
guesses a category based on which words showed up in similar tickets
before.
BPMN 2.0 - a standard way of drawing a business
process as a flowchart, before automating any of it.
- LINK: [← Smart Medical Records wrong-patient retrieval](/p/clinical-rag/)
- LINK: [Image QA Gate → which error to make](/p/image-qa/)
- LINK: [← All work](/#care-agent)
- LINK: [CV](/cv/)
- LINK: [GitHub](https://github.com/iamtamilore)
- LINK: [newalabitaiwo625@gmail.com](mailto:newalabitaiwo625@gmail.com)
- LINK: [LinkedIn](https://www.linkedin.com/in/tami-alabi/)
- LINK: [GitHub](https://github.com/iamtamilore)
- LINK: [work](/work/)
- LINK: [tracker](/jobs/)
- LINK: [bank](/bank-pwa/)

---

## PAGE: /p/image-qa/

- LINK: [← All work](/#image-qa)

## Automated
QA Gate for AI-Generated Campaign Imagery
9 min read
Catching identity drift and colour drift in generated fashion
photography, before a client sees it.
Built by Taiwo Alabi. MSc Artificial Intelligence,
National College of Ireland · July to August 2026
A quality gate that flags good images gets switched off inside a
week, so the target was precision, not coverage: every image it called
"same person" had to be the same person. A Siamese network over frozen
ResNet50 features reached F1 0.90 at precision 1.00 on 90 sealed test
pairs, against pixel difference at 0.59 and kNN at 0.26. Ninety pairs is
too few to rule out luck as the explanation for the gap, and McNemar's
test is underpowered to settle it.
What this evidences: critiquing model quality and
evaluation design. A score with no baseline beside it is decoration, so
this one carries two.

#### Contents
The problem
- LINK: [The problem](#1-the-problem)
Results
- LINK: [Results](#2-results)
How the system works
- LINK: [How the system works](#3-how-the-system-works)
The identity check
- LINK: [The identity check](#4-the-identity-check)
The colour check
- LINK: [The colour check](#5-the-colour-check)
Where it fails
- LINK: [Where it fails](#6-where-it-fails)
Unexpected finding
- LINK: [Unexpected finding](#7-unexpected-finding)
Honest limitations
- LINK: [Honest limitations](#8-honest-limitations)
Reproduce it
- LINK: [Reproduce it](#9-reproduce-it)
Terms used in this
report
- LINK: [Terms used in this
report](#10-terms-used-in-this-report)
- LINK: [Read the detail pdf](/assets/docs/image_qa_writeup.pdf)
- LINK: [Check the code](https://github.com/iamtamilore/campaign-image-qa)

### 1. The problem
A fashion brand needs thirty photographs of one model in one outfit,
shot from several angles. The images are generated rather than
photographed, and they come back looking almost right.
Then you look properly. In shot four the jaw is slightly different.
By shot twenty it is a different woman wearing the same jacket. The
lighting drifts the same way, warm in one frame and cold in the next, as
though the shoot ran over three days instead of three minutes.
No single image looks wrong. The set does not match, and a set that
does not match cannot ship. Checking by eye works for thirty images. It
does not work for three hundred a day, and it is exactly the kind of
repetitive comparison a person gets worse at the longer they do it.
Two distinct faults, so two distinct checks:
Identity drift. The generated person stops being the contracted
subject.
Grade drift. The colour and lighting wander off the approved
look.
The obvious off-the-shelf fix failed first. The face_recognition library is built for real photographs, and
its distance rule does not transfer to the smoothed skin texture of a
generated face. That failure is what made this a project rather than a
library call.

### 2. Results
Measured on a sealed set of 90 image pairs, never touched during
training or tuning.
Quick read on the columns: precision is how often the gate was right
when it said "same person"; recall is how many of the true same-person
pairs it actually caught; F1 blends the two; ROC-AUC scores how well the
model separates the two classes overall, 1.00 is perfect, 0.5 is a coin
flip.
The first row is the honest headline: precision 1.00 at the threshold
the model shipped with, 0.5, which is just the sigmoid default. Every
time the gate said "same person", it was right. It never once passed the
wrong subject through the gate. Under the cost model for this problem
that is the expensive error, and the system made none of it.
Pixel difference also reaches precision 1.00. So the gate is not
unique in never passing the wrong subject through; the gain over that
baseline is recall, 0.82 against 0.42. That is the number worth putting
next to it, because a router that is right when it speaks and silent
when it is not is a different system from one that catches most of the
true pairs.
kNN is the other useful comparison. It reads the identical
fingerprints as the proposed model and still scores worst of the three,
because it weighs all 128 dimensions equally, so background tint votes
as loudly as jaw shape. Same information, no learning, and the score
collapses. That gap is the argument for the design.
The ROC curve on the held-out test set. Only the proposed model
and the random diagonal are plotted here; the baseline scores are in the
table above. A curve this close to the corner says the two classes are
separable on this data; it does not say the margin would survive 90 more
pairs from a third subject.

### 3. How the system works
One image comes in. It is prepared once, then scored twice, and it
passes only if both checks clear. The two faults are independent: an
image can be exactly the right person in exactly the wrong light.
The gate fails in the cheaper direction on purpose. A good image
wrongly rejected costs one regeneration. A bad image wrongly accepted
reaches the client.

### 4. The identity check
You cannot ask a computer "is this the same woman". So each
photograph becomes a list of numbers, a fingerprint, and the question
becomes whether two fingerprints sit close together.
Making good fingerprints needs a network that already knows how to
look at pictures, and learning that takes about a million photographs. I
have 106. So I borrow: ResNet50, pretrained on ImageNet, kept frozen. My
600 pairs cannot improve on a million images, and freezing keeps the
remaining job small.
A Siamese network is two identical copies of that frozen network side
by side. Photo A down one arm, photo B down the other, through the same
weights, so it is one ruler measuring both things. Subtract the two
fingerprints, drop the minus signs, and a single trainable layer reads
the 128 differences and returns a confidence between 0 and 1.
That final layer is where the design earns its keep. It holds one
weight per dimension, so it can learn that jaw shape matters and
background tint does not. kNN cannot: it has nothing that learns.

### 5. The colour check
The problem here is that no bad examples exist. The pipeline never
saved its rejects, so supervised classification is not available.
An autoencoder solves this by only ever seeing good work. It is
handed an image, made to squash it down to almost nothing, then asked to
redraw it from what survived. Each image carries 49,152 numbers and all
of it has to pass through a gap 64 numbers wide. Describing a painting
in eight words, then having someone repaint it from those eight words,
is the same exercise. Memorising is impossible, so only the general
character of the image survives, which is exactly the colour and
lighting I care about.
Feed it an image with the wrong colours and the redraw comes out
badly wrong. The size of that failure is the alarm. It detects bad
images without ever having seen one.
These are deliberately damaged inputs, not drift caught in a real
campaign. The face never changes in this figure, only the grade does,
and real drift is likely subtler than the shifts applied here, which is
why the catch rate below is optimistic.
Good images reconstruct at 0.00374 mean squared error. Damaged ones
at 0.00865, a factor of 2.3. Where the rejection line sits is a business
decision, not a technical one:
I report the whole curve rather than pick one, because the right
answer changes per campaign. Worth stating plainly: 62% is not a solved
problem. This is a filter that flags images for a human, not a gate that
rejects them unattended.

### 6. Where it fails
The honest read is that 90 pairs is too few to claim the gap to
the baselines is not luck.
Every single error is the same error. All eight are same-subject
pairs the model scored as different, and in every one the second image
is a profile or back view while the first is frontal or near-frontal,
the angles where least of the face is visible. The model was not
confused about the face. It could not see the face.
When all your errors share one shape, you know what to fix.

### 7. Unexpected finding
The biggest single improvement came from a number nobody chose.
The network outputs a score from 0 to 1, and anything above 0.5 was
being called "same person". That 0.5 is just the sigmoid default, and it
is the threshold the shipped gate still uses. Tuned on the validation
set only, never the sealed test set, the right value is 0.4821. Applied
to the same 90 sealed pairs, that one change recovered all 8 misses and
created no new false positives, lifting F1 from 0.90 to 1.00. That is
the second row of the results table, and it is a result on the test set,
not on the data the threshold was chosen on.
The best result in the project came from questioning a setting that
was never a decision in the first place.

### 8. Honest limitations
The dataset is small. 106 images, two subjects, 90 test pairs. Two
subjects cannot tell me whether this generalises to a third, and that is
the ceiling on every claim here.
The advantage is not statistically proven. McNemar's test, a
statistical check for whether two models really differ or just got lucky
on this data, returned p = 0.19 against pixel difference, which does not
clear the usual bar for "definitely not luck". The gap between 0.90 and
0.59 is large, but 90 pairs is too little evidence to rule out chance.
That is a shortage of data, not a null result, and I would rather report
it than omit it.
The off-grade images are damaged by me on purpose. Real drift is
likely subtler than a 60 degree hue shift, so 62% is probably
optimistic.

### 9. Reproduce it
Runs in about a minute and regenerates every metric, confusion matrix
and the ROC curve. Seeded with seed=42 , so the numbers are
identical on every run. Verified across four consecutive runs while
writing this up.
Per-image gate latency is 133 ms on CPU, roughly 450 images a minute,
against a person managing a few hundred a day.
Stack: Python · TensorFlow/Keras · ResNet50 · scikit-learn · NumPy ·
Matplotlib

### 10. Terms used in this report
The terms below are defined the way this report uses them, for a
reader who wants to check the reasoning rather than take it on
trust.
Precision - of the images the gate called "same
person", how many actually were. This is the number I optimised for: a
wrongly-accepted image reaches a client.
Recall - of the images that truly were the same
person, how many the gate actually caught.
F1 score - one number blending precision and
recall, so a model can't look good by being great at only one.
ROC-AUC - a single score for how well a model
separates two classes overall. 1.00 is perfect, 0.5 is a coin flip.
Siamese network - two identical copies of the same
model, run side by side on two images, then compared, so it's one ruler
measuring both things.
Autoencoder - a model that learns to compress an
image down to almost nothing, then rebuild it. Feed it something it's
never seen the shape of, and the rebuild comes out visibly wrong. That
failure is the alarm.
McNemar's test - a statistical check for whether
two models genuinely differ, or just got lucky on this particular set of
test images.
- LINK: [← Care Agent the confidence gate](/p/care-agent/)
- LINK: [CV → the short version](/cv/)
- LINK: [← All work](/#image-qa)
- LINK: [CV](/cv/)
- LINK: [GitHub](https://github.com/iamtamilore)
- LINK: [newalabitaiwo625@gmail.com](mailto:newalabitaiwo625@gmail.com)
- LINK: [LinkedIn](https://www.linkedin.com/in/tami-alabi/)
- LINK: [GitHub](https://github.com/iamtamilore)
- LINK: [work](/work/)
- LINK: [tracker](/jobs/)
- LINK: [bank](/bank-pwa/)

---

## PAGE: /404.html

- LINK: [index](/)
- LINK: [work](/work/)
- LINK: [cases](/case-studies/)
- LINK: [process](/process/)
- LINK: [gallery](/gallery/)
- LINK: [cv](/cv/)
- LINK: [episodes](/products/)
404

## That page is not here.
The complete engineering index and the published case studies are both available.
- LINK: [Browse all work](/work/)
- LINK: [View the Agent Foundations CV](/cv/)

### Published case studies
TermsGuard AI shows the passage a flag came from, not an article it claims to quote
- LINK: [TermsGuard AI](/p/termsguard/)
Smart Medical Records per patient before ranking, not filtered after. Tried 30 ways to leak data, 0 worked
- LINK: [Smart Medical Records](/p/clinical-rag/)
Care Agent below 0.55 a human decides. 95.2% on the 40 of 42 it routed
- LINK: [Care Agent](/p/care-agent/)
Image QA Gate against pixel difference at F1 0.59 and kNN at 0.26. Reached 0.90
- LINK: [Image QA Gate](/p/image-qa/)

---

## PAGE: /atoms/

- LINK: [Home](/)
- LINK: [CV](/cv/)
- LINK: [Work](/work/)
- LINK: [Jobs](/jobs/)
- LINK: [Atoms](/atoms/)
- LINK: [OAP](/oap/)
- LINK: [Bank](/bank/)
No atoms match your filters

### Atom Comparison

### 📊 Statistics Dashboard

### Batch Edit Tags
Leave fields blank to skip. Changes apply to in-memory display only.

### ⌨️ Keyboard Shortcuts

---

## PAGE: /bank-pwa/


## Bank it
Something you liked. Save it here, sort it later.

---

## PAGE: /bank/

- LINK: [Home](/)
- LINK: [CV](/cv/)
- LINK: [Work](/work/)
- LINK: [Jobs](/jobs/)
- LINK: [Atoms](/atoms/)
- LINK: [OAP](/oap/)
- LINK: [Bank](/bank/)

## Idea Bank
Private. Your captures live in the iamtamilore/idea_bank GitHub
  repo. Paste the same access token you use in bank-pwa - it's stored only
  on this device (localStorage), never sent anywhere but the GitHub API.
- LINK: [bank-pwa](/bank-pwa/)

## Idea Bank
New captures land in inbox/ from bank-pwa . This page is
    read-only - to turn an inbox capture into a card, run python3 tools/bank.py against the repo on your own machine.
- LINK: [bank-pwa](/bank-pwa/)

---

## PAGE: /channels/

- LINK: [index](/)
- LINK: [cv](/cv/)
- LINK: [skim](/skim/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
- LINK: [episodes](/products/)
- LINK: [channels](/channels/)
- LINK: [jobs](/jobs/)

## Channels
Five channels. One five-stage pipeline. Every episode is auditable end to end, the brief, the frames, the gate, the post. Three are live. Two are test-beds where the format is the work.

### Watch the channels
Dark history. The events, regimes and people history skipped over.
The first episode kept 65.3% of viewers past the midpoint on Musashi's duel with Kojirō. Retention is the format signal.
LIVE · EP_MUSASHI · 40.1s · 876 first-day views
- LINK: [View the 19-shot breakdown →](/products/forgotten-fronts/ep_musashi.html)
Tested objects. Watches, engines, instruments. Everything claims it works. We put it through the test.
Episode one is built, gated, and ready to upload . The QA gate ran 9 of 9 frames against the reference bank at vs-seed and vs-hero.
READY · EP_SPEEDMASTER · 40.0s · 23 shots, 148 words
- LINK: [View the breakdown →](/products/ep_speedmaster/)
Demon Slayer lore, vertical narration-driven. Hard cuts on beat boundaries, not the blur-whip.
13 episodes built and gated , proof the pipeline can ship a single franchise to format. Subject ratios measured against the channel median: Tengen 3.77x, Sanemi 1.91x, Upper Moons 1.47x.
READY · EP_OBANAI · 40.0s · 13 episodes built, awaiting a YouTube channel
Format research. 3.00-second grid, blur-whip transitions, one red word at 140px. The opposite of Zenpai, on purpose.
4 episode folders (Gojo, Madara, Sukuna, Ben 10), the format itself is the experiment. No subject catalogue yet ; building it is the next move.
R&D · EP_GOJO · 48.0s · 4 experimental episodes
Money, economy, companies that failed. Money/economy measured 0.09x against the channel median, this needs its own scrape before it ships.
Not started. The pipeline is ready. The subject list is the work.
EMPTY · Awaiting scrape + subject list

### The pipeline every channel runs on
Plan, select, build, gate, post. Every episode on every channel goes through these five stages. The gate is the load-bearing one, that's why it carries the only warm colour in the diagram.

#### What the gate actually measures
The gate runs ResNet50 cosine similarity at three frame positions per scene, then asks a vision model for a modern/anachronism check. The pass/fail criterion is calibrated against the reverse-engineered luxury episode:
The numbers are vs-seed / vs-hero. The third scene has the lowest scores and that is correct, a character walking away should diverge from the reference. The gate flags catastrophic divergence, not stylistic movement.

#### The six rules the pipeline enforces
Each rule closes one class of failure that cost real time or money. Every rule is documented, fileable, and automatic, not convention.
Narrate first, brief against the audio. Estimated beats never match the TTS pauses. Plan after the audio, not before.
Five queries per need. Identical queries put the same 50 jpgs in every folder; the selector dedups globally, so half the needs see nothing.
Every NEVER names its beat. "No Kanao" rejected the very need whose line is "Then he met Kanao." Constraints are per-beat, not global.
UNPARSEABLE means transport, not model failure. A timeout reads as a model fault unless the selector logs transport separately.
Pixel review at full 1080×1920. Six frames passed at 640px and failed at full resolution. Confirm by opening the source PNG.
Every claim matches the source verbatim. Two claims dropped from Musashi for being unsourced; one added to Speedmaster because it was sourced.
- LINK: [See the worked example](/products/)
- LINK: [Workflow blueprint](/products/workflow/)
- LINK: [How I make an episode](/how/)

---

## PAGE: /corpus/

TAIWO ALABI · MSC ARTIFICIAL INTELLIGENCE, NCI DUBLIN

## TermsGuard corpus
The TermsGuard engine pointed at a real, ongoing data-collection problem.
      Each company's privacy policy is fetched on the schedule below, scored by
      the same GDPR-cosine pipeline that powers the live demo, and stored
      versioned with the diff between snapshots. The corpus is the proof
      that the engine works on documents it has never seen before.

### How to read this
The score is the mean cosine confidence of the flagged clauses, range 0 to 1.
    Risk labels (Low / Medium / High / Unknown) come from fixed score bands, not a learned model.
    A diff is computed between the current snapshot and the previous one for the same company;
    companies with only one snapshot have no diff to show.
Flagged = matches the unfair reference set Cleared = matches the fair reference set Uncertain = no confident match

### Latest scores
All 20 companies with a successful fetch. Score is the mean cosine
      confidence of the policy's flagged (non-ethical) clauses, range
      0-1. Higher means more concerning clauses with higher model
      confidence. Last fetched 2026-10-29.
- LINK: [Google](https://policies.google.com/privacy)
- LINK: [Apple](https://www.apple.com/legal/privacy/)
- LINK: [Microsoft](https://privacy.microsoft.com/privacystatement)
- LINK: [Amazon](https://www.amazon.com/gp/help/customer/display.html?nodeId=201909010)
- LINK: [TikTok](https://www.tiktok.com/legal/privacy-policy?lang=en)
- LINK: [Deutsche Bank](https://www.db.com/legal-resources/privacy-notice?language_id=1)
- LINK: [UniCredit](https://www.unicredit.eu/privacy)
- LINK: [Rabobank](https://www.rabobank.com/privacy)
- LINK: [Allianz](https://www.allianz.com/en/privacy-statement.html)
- LINK: [AXA](https://www.axa.com/en/privacy-policy)
- LINK: [IKEA](https://www.ikea.com/global/en/legal/privacy-cookie-statement/)
- LINK: [Inditex](https://www.inditex.com/itxcomweb/es/legal/privacy-policy)
- LINK: [Decathlon](https://www.decathlon.com/policies/privacy-policy)
- LINK: [SAP](https://www.sap.com/about/legal/privacy.html)
- LINK: [Spotify](https://www.spotify.com/legal/privacy-policy/)
- LINK: [Deutsche Telekom](https://www.telekom.com/en/general/data-protection-information)
- LINK: [Vodafone](https://www.vodafone.com/site-services/privacy-and-cookies)
- LINK: [Booking.com](https://www.booking.com/content/privacy.html)
- LINK: [Telefónica](https://www.telefonica.com/en/privacy-policy)
- LINK: [Adyen](https://www.adyen.com/privacy-policy)

### Per-company detail

#### Google Big Tech
policy source
- LINK: [policy source](https://policies.google.com/privacy)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium risk policy with purpose limitation concerns, cookie and consent issues, and disputed claims about international transfers and territorial scope. The dominant matches are Article 5(1)(b) Purpose Limitation, with 53 flagged clauses, followed by no basis match in 43 clauses and ePrivacy Directive combinations with Article 5(1)(b) or Article 7 Conditions for Consent. The engine also flags Article 44 International Transfers and Article 3 Territorial Scope.

##### How this was scored
How this was scored: 481 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 173 flagged clauses
      , most of them under Art.5(1)(b) Purpose Limitation violation .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 173 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
We don’t share information that personally identifies you with advertisers, such as your name or email, unless you ask us to.
Art.5(1)(b) Purpose Limitation confidence 0.72
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
Data protection laws vary among countries, with some providing more protection than others.
Art.44 International Transfers confidence 0.72
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...
This Privacy Policy doesn’t apply to services that have separate privacy policies that do not incorporate this Privacy Policy.
Art.3 Territorial Scope unlawful claim confidence 0.72
Retrieved context: [GDPR Art. 3] Territorial scope 1. This Regulation applies to the processing of personal data in the context of the activities of an establishment of a controller or a processor in the Union, regardless of whether the processing takes place in the Union or not. 2. This Regulation applies to the proc...
For example, we use cookies to analyze how people interact with our services.
ePrivacy Directive violation + Art.7 Consent confidence 0.72
Retrieved context: [GDPR Recital 58] The Principle of Transparency 1. The principle of transparency requires that any information addressed to the public or to the data subject be concise, easily accessible and easy to understand, and that clear and plain language and, additionally, where appropriate, visualisation be...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 84 by confidence. These are the clauses the engine read as GDPR-compliant.
To delete your information, you can:
Art.17 Right to Erasure confidence 0.77
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
And some data we retain for longer periods of time when necessary for legitimate business or legal purposes, such as security, fraud and abuse prevention, or financial record-keeping.
Art.5(1)(e) Storage Limitation confidence 0.76
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
However, some website features or services may not function properly without cookies.
ePrivacy Directive + Art.5(1)(b) confidence 0.76
Retrieved context: [GDPR Recital 64] Identity Verification 1. The controller should use all reasonable measures to verify the identity of a data subject who requests access, in particular in the context of online services and online identifiers. 2. A controller should not retain personal data for the sole purpose of b...
We change this Privacy Policy from time to time.
Art.7 Conditions for Consent + Art.13 confidence 0.74
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...

##### Overall analysis
Of 481 clauses analysed, 173 were flagged and 84 were cleared, so the policy contains valid privacy controls alongside a larger set of detected concerns. The flagged examples cover advertiser sharing, cookie analytics, a statement that data protection varies between countries, and exclusion of services with separate privacy policies. The cleared examples cover deletion requests, longer retention for stated business or legal purposes, cookie-related service limits

##### Notes and caveats
224 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Meta Big Tech
policy source
- LINK: [policy source](https://www.facebook.com/help/325807682359234)
No snapshot yet.

#### Apple Big Tech
policy source
- LINK: [policy source](https://www.apple.com/legal/privacy/)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This policy presents a medium risk of consent and access compliance problems. The engine flagged a general privacy commitment under Article 7 Conditions for Consent and an instruction to visit Manage your Apple account under Article 15 Right of Access. The flagged clauses have a mean confidence of 0.58.

##### How this was scored
How this was scored: 7 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 2 flagged clauses
      , most of them under Art.7 Conditions for Consent violation .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 2 of 2 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
Apple is committed to your privacy.
Art.7 Conditions for Consent confidence 0.59
Retrieved context: [GDPR Art. 7] Conditions for consent It shall be as easy to withdraw as to give consent. 8. When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the proc...
To access and manage your Apple data please visit Manage your Apple account.
Art.15 Right of Access confidence 0.58
Retrieved context: [GDPR Art. 15] Right of access by the data subject 1. The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information:...

##### Cleared clauses · what TermsGuard reads as protective
Top 1 of 1 by confidence. These are the clauses the engine read as GDPR-compliant.
For corrections or general enquiries, please Contact Privacy.
Art.15 Right of Access confidence 0.49
Retrieved context: [GDPR Art. 15] Right of access by the data subject 1. The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information:...

##### Overall analysis
Of seven clauses analysed, two were flagged and one was cleared. The flagged set covers one clause under Article 7 and one under Article 15, while the cleared clause also concerns Article 15 and directs users to Contact Privacy for corrections or general enquiries. This shows mixed treatment of access-related language, with the account-management instruction flagged and the contact instruction cleared. Four analysed clauses are not represented in the supplied flagged or cleared lists.

##### Notes and caveats
4 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Microsoft Big Tech
policy source
- LINK: [policy source](https://privacy.microsoft.com/privacystatement)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium-risk policy with data-use, cookie-consent, purpose-limitation, and international-transfer concerns. The engine most often flagged Article 5(1)(b) Purpose Limitation, followed by no basis matches, and also identified ePrivacy Directive and Article 7 Conditions for Consent issues. It also flagged an Article 44 International Transfers clause, with a mean confidence of 0.52 across flagged clauses.

##### How this was scored
How this was scored: 1462 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 286 flagged clauses
      , most of them under Art.5(1)(b) Purpose Limitation violation .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 286 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
Browsing activity includes your browse history, favourites, usage data, and web content.
ePrivacy Directive violation + Art.5(1)(b) confidence 0.79
Retrieved context: [GDPR Recital 18] Not Applicable to Personal or Household Activities 1. This Regulation does not apply to the processing of personal data by a natural person in the course of a purely personal or household activity and thus with no connection to a professional or commercial activity. 2. Personal or ...
We transfer personal data from the country of origin to other countries, including those that may not offer the same level of data protection as determined by the European Commission or your local data protection authority.
Art.44 International Transfers confidence 0.78
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...
We use cookies to store your preferences and settings, help with sign-in, provide personalised ads and analyse site operations.
ePrivacy Directive violation + Art.7 Consent confidence 0.77
Retrieved context: [GDPR Recital 30] Online Identifiers for Profiling and Identification 1. Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identi...
We use cookies and similar technologies to store and honour your preferences and settings, enable you to sign-in, provide personalised advertising, combat fraud, analyse how our products perform, and fulfil other legitimate purposes described below.
ePrivacy Directive violation + Art.7 Consent confidence 0.76
Retrieved context: [GDPR Recital 64] Identity Verification 1. The controller should use all reasonable measures to verify the identity of a data subject who requests access, in particular in the context of online services and online identifiers. 2. A controller should not retain personal data for the sole purpose of b...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 372 by confidence. These are the clauses the engine read as GDPR-compliant.
Because these needs can vary for different data types and the context of our interactions with you or your use of our products, actual retention periods can vary significantly.
Art.5(1)(e) Storage Limitation + Art.13 confidence 0.77
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
You provide some of this data directly, and we get other data by collecting information about your interactions, use, and experiences with our products.
Art.5(1)(a) Transparency confidence 0.75
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
Parents can change or revoke consent at any time.
Art.7(3) Right to Withdraw Consent confidence 0.74
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...
Parents or guardians (“parents”) can change or revoke consent at any time.
Art.7(3) Right to Withdraw Consent confidence 0.74
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...

##### Overall analysis
Of 1,462 clauses analysed, 286 were flagged and 372 were cleared. The flagged examples describe browsing activity collection, cookies used for settings, sign-in, personalised advertising, fraud prevention, and analysis, plus transfers to countries that may not provide the same level of protection. The cleared examples describe variable retention periods, data provided directly or collected from product interactions, and parents' ability to change or revoke consent. The shape is mixed: the policy contains provisions the engine reads as transparent or consent-supporting, alongside broader data-use and transfer language that contributes to the medium score.

##### Notes and caveats
804 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Amazon Big Tech
policy source
- LINK: [policy source](https://www.amazon.com/gp/help/customer/display.html?nodeId=201909010)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This policy presents a medium risk of purpose limitation and consent problems, especially around cookies, identifiers, browsing history, legal compliance, and third-party providers. The flagged set is dominated by Article 5(1)(b) Purpose Limitation, ePrivacy Directive violations, and Article 7 Consent, with one Article 5(1)(a) Transparency violation and five clauses with no basis match.

##### How this was scored
How this was scored: 54 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 14 flagged clauses
      .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 14 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
You can edit Your Browsing History, as well.
ePrivacy Directive violation + Art.5(1)(b) confidence 0.65
Retrieved context: [GDPR Recital 66] Right to be Forgotten 1. To strengthen the right to be forgotten in the online environment, the right to erasure should also be extended in such a way that a controller who has made the personal data public should be obliged to inform the controllers which are processing such perso...
Amazon Services, we use cookies and other identifiers.
ePrivacy Directive violation + Art.7 Consent confidence 0.63
Retrieved context: [GDPR Recital 30] Online Identifiers for Profiling and Identification 1. Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identi...
In certain cases, we collect and use your personal information to comply with laws.
Art.5(1)(b) Purpose Limitation confidence 0.59
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
Third-Party Service Providers: We employ other companies and individuals to perform functions on our behalf.
Art.5(1)(b) Purpose Limitation confidence 0.48
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (6) processed in a manner that ensures appropriate security of the personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organ...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 15 by confidence. These are the clauses the engine read as GDPR-compliant.
Information from Other Sources: We might receive information about you from other sources.
Art.15 Right of Access confidence 0.68
Retrieved context: [GDPR Art. 15] Right of access by the data subject 1. The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information:...
You provide information to us when you:
Art.15 Right of Access confidence 0.68
Retrieved context: [GDPR Art. 15] Right of access by the data subject 1. The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information:...
See examples of information we collect or receive.
Art.5(1)(a) Transparency confidence 0.61
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
You may adjust your personalized advertising preferences by visiting Your Ads Privacy Choices.
Art.25 Privacy by Design & Default confidence 0.59
Retrieved context: [GDPR Art. 25] Data protection by design and by default The controller shall implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed. 2. That obligation applies to the ...

##### Overall analysis
The engine flagged 14 of 54 analysed clauses and cleared 15. Flagged clauses describe editing browsing history, using cookies and other identifiers, collecting information to comply with laws, and using third-party service providers; cleared clauses describe information sources, user-provided information, collection examples, and advertising preference controls. The cleared set therefore covers access, transparency, and preference controls, while the flagged set concentrates on processing purposes and consent. The score is 0.48, based on the mean confidence of flagged clauses.

##### Notes and caveats
25 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### TikTok Big Tech
policy source
- LINK: [policy source](https://www.tiktok.com/legal/privacy-policy?lang=en)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium risk profile centered on tracking, consent, and broad information sharing. The dominant signal is Article 5(1)(b) Purpose Limitation, including clauses also mapped to Article 28, with additional flags for Article 7 Conditions for Consent and the ePrivacy Directive. The engine reads the policy as allowing collection through the in-app browser and cookies, and sharing information with service providers, partners, and other third parties.

##### How this was scored
How this was scored: 268 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 78 flagged clauses
      , most of them under Art.5(1)(b) Purpose Limitation violation .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 78 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
We also collect information about your interactions with websites when you use our in-app browser.
ePrivacy Directive violation + Art.5(1)(b) confidence 0.76
Retrieved context: [GDPR Recital 71] Profiling Automated decision-making and profiling based on special categories of personal data should be allowed only under specific conditions. * This title is an unofficial description....
We use cookies and similar tracking technologies to operate and provide the Platform.
ePrivacy Directive violation + Art.7 Consent confidence 0.73
Retrieved context: [GDPR Recital 30] Online Identifiers for Profiling and Identification 1. Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identi...
We share “What Information We Collect” with service providers, partners and other third party entities, as described in “How We Share Your Information”.
Art.5(1)(b) Purpose Limitation + Art.28 confidence 0.72
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
We share Information You Provide, Automatically Collected Information, and Information From Other Sources with these service providers as necessary to enable them to provide their services.
Art.5(1)(b) Purpose Limitation + Art.28 confidence 0.69
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 54 by confidence. These are the clauses the engine read as GDPR-compliant.
Your rights: Whenever we use your information based on your consent, you can withdraw your consent at any time.
Art.7(3) Right to Withdraw Consent confidence 0.84
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...
However, your withdrawal of consent will not affect the lawfulness of processing your information based on your consent prior to your withdrawal of consent.
Art.7(3) Right to Withdraw Consent confidence 0.77
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...
You can delete or ask us to delete your information.
Art.17 Right to Erasure confidence 0.77
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
The retention periods will be different depending on the type of information and the purposes for which we use the information.
Art.5(1)(e) Storage Limitation + Art.13 confidence 0.77
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...

##### Overall analysis
The flagged clauses describe collection and sharing practices, while the cleared clauses describe consent withdrawal, erasure, and retention periods. Of 268 clauses analysed, 78 were flagged and 54 were cleared, with a mean flagged-clause confidence of 0.53. The policy therefore combines stated user rights and retention disclosures with clauses the engine associates with purpose limitation, consent, and tracking concerns.
[auto-filed as T-0038 - pass --task next time to group it]

##### Notes and caveats
136 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Deutsche Bank Banking
policy source
- LINK: [policy source](https://www.db.com/legal-resources/privacy-notice?language_id=1)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium-risk privacy policy with potential consent, cookie purpose, and data security concerns. The engine primarily flags ePrivacy Directive requirements and GDPR Article 7 Consent, followed by Article 5(1)(b) Purpose Limitation and one clause linked to Article 32 and Article 5(1)(f). It reads the policy as describing cookies that activate on visits and persist after browsing, while leaving questions about how information is retained, protected, and used.

##### How this was scored
How this was scored: 73 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 12 flagged clauses
      , most of them under ePrivacy Directive violation + Art.7 Consent .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 12 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
Some cookies allow you to take full advantage of the functionality of our website.
ePrivacy Directive violation + Art.7 Consent confidence 0.74
Retrieved context: [GDPR Recital 64] Identity Verification 1. The controller should use all reasonable measures to verify the identity of a data subject who requests access, in particular in the context of online services and online identifiers. 2. A controller should not retain personal data for the sole purpose of b...
They are activated each time you visit the website that created that particular cookie.
ePrivacy Directive violation + Art.7 Consent confidence 0.61
Retrieved context: [GDPR Recital 30] Online Identifiers for Profiling and Identification 1. Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identi...
How is information retained, protected, and used?
Art.32 + Art.5(1)(f) confidence 0.60
Retrieved context: [GDPR Art. 32] Security of processing (1) the pseudonymisation and encryption of personal data; (2) the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services; (3) the ability to restore the availability and access to personal data in...
So-called “persistent cookies” remain on your device even after you close your internet browser.
ePrivacy Directive violation + Art.7 Consent confidence 0.60
Retrieved context: [GDPR Recital 66] Right to be Forgotten 1. To strengthen the right to be forgotten in the online environment, the right to erasure should also be extended in such a way that a controller who has made the personal data public should be obliged to inform the controllers which are processing such perso...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 20 by confidence. These are the clauses the engine read as GDPR-compliant.
You can set your web browser to disable cookies.
ePrivacy Directive + Art.5(1)(b) confidence 0.71
Retrieved context: [GDPR Recital 64] Identity Verification 1. The controller should use all reasonable measures to verify the identity of a data subject who requests access, in particular in the context of online services and online identifiers. 2. A controller should not retain personal data for the sole purpose of b...
What information is collected and how is it used?
Art.5(1)(a) Transparency confidence 0.67
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
Marketing cookies and other cookies requiring your consent are not used on this site.
ePrivacy Directive + Art.5(1)(b) confidence 0.67
Retrieved context: [GDPR Recital 42] Burden of Proof and Requirements for Consent Consent should not be regarded as freely given if the data subject has no genuine or free choice or is unable to refuse or withdraw consent without detriment. <div...
Please note that if you disable cookies in this way, you will not be able to set new cookies.
ePrivacy Directive + Art.5(1)(b) confidence 0.65
Retrieved context: [GDPR Recital 66] Right to be Forgotten 1. To strengthen the right to be forgotten in the online environment, the right to erasure should also be extended in such a way that a controller who has made the personal data public should be obliged to inform the controllers which are processing such perso...

##### Overall analysis
The policy contains 12 flagged clauses and 20 cleared clauses among 73 analysed, with a mean flagged-clause confidence of 0.55. The flagged clauses describe cookies used for website functionality, activation on visits, and persistence after the browser closes; the cleared clauses describe browser controls, transparency about collection and use, and the stated absence of marketing cookies requiring consent. This gives the policy a mixed profile, with cookie and information-handling language triggering concerns while several disclosure and control statements are read as compliant.

##### Notes and caveats
41 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### ING Banking
policy source
- LINK: [policy source](https://www.ing.com/Privacy-Statement.htm)
No snapshot yet.

#### UniCredit Banking
policy source
- LINK: [policy source](https://www.unicredit.eu/privacy)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This policy presents a medium consent and cookie compliance risk, centered on profiling cookies, third-party cookies, and advertising based on user preferences. The dominant basis is the ePrivacy Directive and Article 7 Consent, with two flagged clauses stating that profiling cookie installation requires prior consent. A separate purpose statement received no basis match.

##### How this was scored
How this was scored: 13 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 3 flagged clauses
      , most of them under ePrivacy Directive violation + Art.7 Consent .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 3 of 3 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
This website uses technical, analytics and profiling Cookies, also installed by third parties (so called Third-Party Cookies).
ePrivacy Directive violation + Art.7 Consent confidence 0.63
Retrieved context: [GDPR Recital 30] Online Identifiers for Profiling and Identification 1. Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identi...
Profiling Cookies are used in order to offer you advertising messages in line with your preferences; their installation requires your prior consent.
ePrivacy Directive violation + Art.7 Consent confidence 0.62
Retrieved context: [GDPR Art. 4] Definitions ‘profiling’ means any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning that natural person’s performance at work, ec...
Our purpose is to empower communities to progress, delivering the best-in-class for all stakeholders, unlocking the potential of our clients and our people across Europe.
no basis match confidence 0.43
Retrieved context: ...

##### Cleared clauses · what TermsGuard reads as protective
Top 2 of 2 by confidence. These are the clauses the engine read as GDPR-compliant.
If you want to know more or refuse consent click on the link below.
Art.7(3) Right to Withdraw Consent confidence 0.63
Retrieved context: [GDPR Art. 7] Conditions for consent It shall be as easy to withdraw as to give consent. 8. When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the proc...
By clicking on the X at the top right, your navigation will continue without profiling cookies.
ePrivacy Directive + Art.5(1)(b) confidence 0.62
Retrieved context: [GDPR Recital 72] Guidance of the European Data Protection Board Regarding Profiling 1. Profiling is subject to the rules of this Regulation governing the processing of personal data, such as the legal grounds for processing or data protection principles. 2. The European Data Protection Board establ...

##### Overall analysis
The engine flagged three clauses and cleared two of the 13 analysed clauses. The flagged set describes technical, analytics, and profiling cookies, profiling-based advertising, and a broad stakeholder purpose statement. The cleared clauses describe refusing consent through a link and continuing navigation without profiling cookies by clicking the X. This pattern shows that the policy contains stated consent and refusal mechanisms, while the cookie and profiling language still triggered the main risk signals.

##### Notes and caveats
8 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Rabobank Banking
policy source
- LINK: [policy source](https://www.rabobank.com/privacy)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This policy presents a medium risk of broad or insufficiently bounded data use and sharing. The engine primarily identified Article 5(1)(b) Purpose Limitation violations, including disclosures to external parties, direct transfers, and use based on legitimate interest, with additional matches involving Article 7 Conditions for Consent, Article 28, and Articles 44 and 13 Right to be Informed.

##### How this was scored
How this was scored: 159 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 36 flagged clauses
      , most of them under Art.5(1)(b) Purpose Limitation violation .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 36 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
If you ask us to transfer data directly to another party, we will only be able to do this if it is technically feasible.
Art.5(1)(b) Purpose Limitation confidence 0.71
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
Additionally, we might share your data with parties outside of Rabobank Group, such as the Government/Regulatory bodies or third parties who assist us in the provision of services and where we are legally obliged to do so.
Art.5(1)(b) Purpose Limitation confidence 0.69
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
In that case, we may also use your data based on legitimate interest.
Art.5(1)(b) Purpose Limitation confidence 0.65
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
Who do we share your personal data with?
Art.5(1)(b) Purpose Limitation confidence 0.65
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 35 by confidence. These are the clauses the engine read as GDPR-compliant.
We do not sell your personal data.
Art.5(1)(b) Purpose Limitation confidence 0.83
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
We process your data for various purposes.
Art.5(1)(a) Transparency confidence 0.73
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
For example, we may receive your data from:
Art.15(3) Right of Access confidence 0.69
Retrieved context: [GDPR Art. 15] Right of access by the data subject 1. The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information:...
You may request that we erase data concerning yourself that we have recorded.
Art.17 Right to Erasure confidence 0.69
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...

##### Overall analysis
The engine flagged 36 of 159 analysed clauses and cleared 35, with a mean flagged-clause confidence of 0.53. The flagged set is led by 15 Article 5(1)(b) Purpose Limitation violations and includes 9 clauses with no basis match. The cleared clauses state that Rabobank does not sell personal data and describe processing purposes, data sources, and erasure requests. The policy therefore contains both clear rights and transparency language and clauses that the engine reads as leaving data-sharing purposes or legal grounds insufficiently bounded.
[auto-filed as T-0039 - pass --task next time to group it]

##### Notes and caveats
88 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Allianz Insurance
policy source
- LINK: [policy source](https://www.allianz.com/en/privacy-statement.html)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium-risk policy with a mixed compliance profile involving tracking controls, purpose limitation, retention, international transfers, and controller liability. The engine most often flags ePrivacy Directive issues paired with Article 5(1)(b) Purpose Limitation, along with clauses with no basis match. It also identifies Article 44 to 49 International Transfers, Article 82 Controller Liability, Article 5(1)(e) Storage Limitation, and Article 17 Right to Erasure concerns.

##### How this was scored
How this was scored: 99 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 20 flagged clauses
      , most of them under ePrivacy Directive violation + Art.5(1)(b) .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 20 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
We will not retain your personal data for longer than is necessary and we will hold it only for the purposes for which it was obtained.
Art.5(1)(e) Storage Limitation + Art.17 confidence 0.79
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
In many cases you can also control tracking technologies using your browser.
ePrivacy Directive violation + Art.5(1)(b) confidence 0.66
Retrieved context: [GDPR Recital 24] Applicable to Controllers/Processors Not Established in the Union if Data Subjects Within the Union are Profiled 1. The processing of personal data of data subjects who are in the Union by a controller or processor not established in the Union should also be subject to this Regulat...
For the stated purposes, we may also share your personal data with the following parties who operate as data processors under our instruction:
Art.5(1)(b) Purpose Limitation confidence 0.66
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
Even if both sender and receiver are located in the same country, information sent via the Internet may be transmitted across international borders and be forwarded to a country with a lower data protection level than in your country of residence.
Art.44-49 International Transfers confidence 0.64
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 20 by confidence. These are the clauses the engine read as GDPR-compliant.
Delete your personal data from our records if it is no longer needed for the purposes indicated above;
Art.17 Right to Erasure confidence 0.81
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
Withdraw your consent at any time where your personal data is processed with your consent;
Art.7(3) Right to Withdraw Consent confidence 0.80
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...
We will not disclose your personal data to parties who are not authorized to process them.
Art.5(1)(b) Purpose Limitation confidence 0.74
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
What are your rights in respect of your personal data?
Art.17 Right to Erasure confidence 0.73
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...

##### Overall analysis
Among 99 clauses analysed, 20 were flagged and 20 were cleared, with a mean flagged-clause confidence of 0.53. The flagged set covers retention language, browser-based tracking controls, processor sharing, and the possibility that internet transfers cross borders to countries with lower protection. The cleared set includes deletion when data is no longer needed, withdrawal of consent, limits on
[auto-filed as T-0040 - pass --task next time to group it]

##### Notes and caveats
59 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### AXA Insurance
policy source
- LINK: [policy source](https://www.axa.com/en/privacy-policy)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium-risk policy with a concentrated governance and consent-related risk pattern. The engine flagged joint-controller language under Article 5(1)(b) Purpose Limitation and Article 28, AI principles under Article 7(4) Conditional consent prohibition, and a CNIL contact clause with no matched basis.

##### How this was scored
How this was scored: 23 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 3 flagged clauses
      , most of them under Art.5(1)(b) Purpose Limitation + Art.28 .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 3 of 3 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
In some cases, GIE AXA and AXA SA (excluding these subsidiaries) a Société Anonyme, organized under French laws, having its registered office at 25 Avenue Matignon, 75008 Paris, registered with the Registry of Commerce and Companies of Paris under number 572 093 920, act as joint data controllers in the context of the processing of your personal data (i.e., they jointly determine the purposes and means of the processing of your information).
Art.5(1)(b) Purpose Limitation + Art.28 confidence 0.47
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (6) processed in a manner that ensures appropriate security of the personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organ...
When we use artificial intelligence (AI), we are committed to comply with the following principles, which are intended to help ensure that artificial intelligence is trustworthy and ethically sound (see Responsible Usage of Artificial Intelligence): purpose; technical robustness and safety; non-discrimination and fairness; transparency and interpretability; human agency and accountability; privacy and data governance; sustainability.
Art.7(4) Conditional consent prohibition confidence 0.45
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...
In France, the data protection authority is the Commission Nationale de l'Informatique et des Libertés, or “CNIL” whose postal address is 3 place de Fontenoy - TSA 80715 – 75334 Paris CEDEX 07.
no basis match confidence 0.41
Retrieved context: ...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 5 by confidence. These are the clauses the engine read as GDPR-compliant.
Based on the legal basis for the processing of your personal data, you have also the right to:
Art.17 Right to Erasure confidence 0.69
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
If you wish to know more about the processing of your personal data and you are:
Art.5(1)(a) Transparency confidence 0.65
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
These systems, based on objectives, analyse the data they receive to deduce the best way to produce results such as predictions, recommendations, or content, which can influence physical or virtual environments.
Art.5(1)(a) Transparency confidence 0.55
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (3) adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed (‘data minimisation’); (4) accurate and, where necessary, kept up to date; every reasonable step must be taken to ensure t...
Request the limitation of the processing of your personal data, you have the right to ask AXA to limit the processing of your personal data.
Art.5(1)(c) Data Minimisation confidence 0.53
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...

##### Overall analysis
Of 23 clauses analysed, 3 were flagged and 5 were cleared, with a mean flagged-clause confidence of 0.44. The flagged clauses concern controller roles, AI governance principles, and regulatory contact information. The cleared clauses cover erasure rights, transparency, descriptions of AI systems, and limits on processing. The policy therefore contains both targeted flagged provisions and clauses that the engine read as addressing transparency and data subject rights.
[auto-filed as T-0041 - pass --task next time to group it]

##### Notes and caveats
15 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### IKEA Retail
policy source
- LINK: [policy source](https://www.ikea.com/global/en/legal/privacy-cookie-statement/)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium-risk policy with signals of broad-purpose data sharing, tracking through cookies, and retention tied to account activity rather than a stated end point. The dominant issues concern Article 5(1)(b) Purpose Limitation, Article 7 Consent, and Article 17 Right to Erasure, with the flagged set also including Article 28 processor provisions. Of 421 clauses analysed, 73 were flagged, with a mean flagged-clause confidence of 0.55.

##### How this was scored
How this was scored: 421 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 73 flagged clauses
      , most of them under Art.5(1)(b) Purpose Limitation violation .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 73 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
To provide our services to you, we may share your data with third parties providing services to us.
Art.5(1)(b) Purpose Limitation confidence 0.78
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
Together with our partners, we use these cookies to collect information about how you interact with our websites—such as time spent, pages visited, geolocation, audience size,  usage patterns, and video usage .
ePrivacy Directive violation + Art.7 Consent confidence 0.76
Retrieved context: [GDPR Recital 30] Online Identifiers for Profiling and Identification 1. Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identi...
Your account data is kept as long as your profile is active.
Art.5(1)(e) Storage Limitation + Art.17 confidence 0.76
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
When you visit our websites (cookie statement)
ePrivacy Directive violation + Art.7 Consent confidence 0.73
Retrieved context: [GDPR Recital 64] Identity Verification 1. The controller should use all reasonable measures to verify the identity of a data subject who requests access, in particular in the context of online services and online identifiers. 2. A controller should not retain personal data for the sole purpose of b...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 63 by confidence. These are the clauses the engine read as GDPR-compliant.
You can withdraw your consent at any time.
Art.7(3) Right to Withdraw Consent confidence 0.98
Retrieved context: [GDPR Art. 7] Conditions for consent It shall be as easy to withdraw as to give consent. 8. When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the proc...
You may withdraw your consent at any time.
Art.7(3) Right to Withdraw Consent confidence 0.96
Retrieved context: [GDPR Art. 7] Conditions for consent It shall be as easy to withdraw as to give consent. 8. When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the proc...
When your personal data is needed for us, for example to meet legal obligations or to perform an agreement with you, we cannot erase your data.
Art.17 Right to Erasure confidence 0.84
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
You can ask us whether we process your personal information and if so receive a copy of such data.
Art.15 Right of Access confidence 0.82
Retrieved context: [GDPR Art. 15] Right of access by the data subject 1. The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information:...

##### Overall analysis
The highest-confidence flags concern sharing data with service providers, cookie-based tracking, active-profile retention, and a cookie statement. The 63 cleared clauses cover consent withdrawal, limits on erasure where legal or contractual needs apply, and access requests. The shape of the results shows a policy that states several individual rights clearly while still drawing flags for data use, tracking, consent, and retention practices

##### Notes and caveats
285 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### H&M Retail
policy source
- LINK: [policy source](https://hmgroup.com/data-privacy-notice)
No snapshot yet.

#### Inditex Retail
policy source
- LINK: [policy source](https://www.inditex.com/itxcomweb/es/legal/privacy-policy)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium, low-specificity privacy risk centered on vague, non-operational language rather than a stated processing practice. The only flagged text is a community-oriented slogan, and the flagged set has no GDPR basis match, including no identified Article 6 Lawfulness of processing basis.

##### How this was scored
How this was scored: 7 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 1 flagged clauses
      .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 1 of 1 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
A company can make things—but it takes a community to change things.
no basis match confidence 0.37
Retrieved context: ...

##### Cleared clauses · what TermsGuard reads as protective
Top 0 of 0 by confidence. These are the clauses the engine read as GDPR-compliant.
No clauses were cleared.

##### Overall analysis
Seven clauses were analysed, with one flagged and none cleared. The policy record therefore provides one flagged example and no cleared comparison set. The 0.37 score is the mean confidence of that single flagged clause.

##### Notes and caveats
6 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
No clauses were cleared. The corpus has no clauses that read as GDPR-compliant by the reference comparison.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Decathlon Retail
policy source
- LINK: [policy source](https://www.decathlon.com/policies/privacy-policy)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium-risk policy with a concentration of purpose limitation concerns around marketing and promotional use, partner use under their own notices, and collection through cookies and similar technologies. The dominant finding is Article 5(1)(b) Purpose Limitation, with 20 flagged clauses and five combined with Article 28, alongside Article 44 International Transfers, the ePrivacy Directive with Article 7 Conditions for Consent, and Article 82 Controller Liability. The flagged material concerns expanded use, processing by partners, international processing, and consent-related collection.

##### How this was scored
How this was scored: 88 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 33 flagged clauses
      , most of them under Art.5(1)(b) Purpose Limitation violation .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 33 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
We use your personal information for marketing and promotional purposes, such as to send marketing, advertising and promotional communications by email, text message or postal mail, and to show you online advertisements for products or services on the Services or other websites, including based on items you previously have purchased or added to your cart and other activity on the Services.
Art.5(1)(b) Purpose Limitation confidence 0.76
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
Our business and marketing partners will use your information in accordance with their own privacy notices.
Art.5(1)(b) Purpose Limitation + Art.28 confidence 0.69
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
Please note that we may transfer, store and process your personal information outside the country you live in.
Art.44 International Transfers confidence 0.68
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...
Automatically through the Services including from your device when you use our products or services or visit our websites, and through the use of cookies and similar technologies;
ePrivacy Directive violation + Art.7 Consent confidence 0.67
Retrieved context: [GDPR Recital 30] Online Identifiers for Profiling and Identification 1. Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identi...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 18 by confidence. These are the clauses the engine read as GDPR-compliant.
You may have a right to request that we delete personal information we maintain about you.
Art.17 Right to Erasure confidence 0.79
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
Other than the Global Privacy Control, we do not recognize other "Do Not Track" signals that may be sent from your web browser or device.
Art.5(1)(b) Purpose Limitation + ePrivacy Directive confidence 0.73
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
We will post the revised Privacy Policy on this website, update the "Last updated" date and provide notice as required by applicable law.
Art.7 Conditions for Consent + Art.13 confidence 0.71
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...
Please read this Privacy Policy carefully.
Art.7 Conditions for Consent + Art.13 confidence 0.69
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...

##### Overall analysis
Of 88 clauses analysed, 33 were flagged and 18 were cleared, with a mean flagged-clause confidence of 0.59. The cleared examples cover the right to request erasure, treatment of Do Not Track signals, notice of policy changes, and a general instruction to read the policy. This contrast shows that the engine did not flag every rights or notice provision

##### Notes and caveats
37 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### SAP Tech & SaaS
policy source
- LINK: [policy source](https://www.sap.com/about/legal/privacy.html)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium-risk policy with compliance risk focused on international data transfers and use of personal data beyond clearly matched purposes. The engine flagged Article 44 International Transfers violations, Article 5(1)(b) Purpose Limitation violations, Article 82 Controller Liability violations, and clauses with no basis match. It also identified combined Article 5(1)(b) and Article 28 concerns.

##### How this was scored
How this was scored: 316 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 72 flagged clauses
      .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 72 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
Your personal data may be processed globally.
Art.44 International Transfers confidence 0.77
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...
In conducting our international business operations, we may transfer your Personal Data to countries outside of Malaysia for the purposes described in this Privacy Statement.
Art.44 International Transfers confidence 0.74
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...
In conducting our international business operations, we may transfer your Personal Data to countries outside of Thailand for the purposes described in this Privacy Statement.
Art.44 International Transfers confidence 0.72
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...
Your Personal Data may be stored and processed by the SAP Group in countries outside your jurisdiction for general business purposes.
Art.44 International Transfers confidence 0.69
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 74 by confidence. These are the clauses the engine read as GDPR-compliant.
Request for the deletion of your Personal Data, under certain lawful circumstances.
Art.17 Right to Erasure confidence 0.81
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
To the extent provided by applicable data protection laws, you have the right to:
Art.7 Conditions for Consent confidence 0.75
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...
Withdraw your consent for the processing of your Personal Data at any time.
Art.17 Right to Erasure confidence 0.75
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
Delete your personal data we hold about you.
Art.17 Right to Erasure confidence 0.74
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...

##### Overall analysis
The policy contains 72 flagged clauses and 74 cleared clauses out of 316 analysed, so its text presents both risk signals and recognised rights language. The flagged examples permit global processing and transfers or storage outside Malaysia, Thailand, or the reader's jurisdiction. The cleared examples state rights to deletion and erasure, and to withdraw consent. The score of 0.54 is the mean confidence of the flagged clauses, while the cleared set is not empty.

##### Notes and caveats
170 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Spotify Tech & SaaS
policy source
- LINK: [policy source](https://www.spotify.com/legal/privacy-policy/)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium privacy compliance risk centered on secondary use and retention of personal data, tailored advertising and profiling of minors, international transfers, and consent conditions. The dominant signals are Article 5(1)(b) Purpose Limitation, Article 8 and Article 22 protections concerning profiling of minors, Article 44 International Transfers, and Article 7 Conditions for Consent. It also flags Article 5(1)(e) Storage Limitation and Article 17 Right to Erasure where data may be retained after account deletion.

##### How this was scored
How this was scored: 279 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 86 flagged clauses
      .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 86 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
After your account is deleted, we keep some data for a longer time period but for very limited purposes.
Art.5(1)(e) Storage Limitation + Art.17 confidence 0.89
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
Our partners may also combine the personal data we share with them with other data they collect about you, e.g. your use of their services.
Art.5(1)(b) Purpose Limitation confidence 0.80
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
Appropriate age for tailored advertising:
Art.8 + Art.22 profiling of minors (+ likely COPPA exposure) confidence 0.72
Retrieved context: [GDPR Art. 8] Conditions applicable to child's consent in relation to information society services 1. Where point (a) of Article 6(1) applies, in relation to the offer of information society services directly to a child, the processing of the personal data of a child shall be lawful where the child ...
You will not be able to 'opt-in' to Tailored Ads if you are under the appropriate age.
Art.8 + Art.22 profiling of minors (+ likely COPPA exposure) confidence 0.72
Retrieved context: [GDPR Art. 8] Conditions applicable to child's consent in relation to information society services 1. Where point (a) of Article 6(1) applies, in relation to the offer of information society services directly to a child, the processing of the personal data of a child shall be lawful where the child ...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 55 by confidence. These are the clauses the engine read as GDPR-compliant.
To withdraw your consent, you can:
Art.7(3) Right to Withdraw Consent confidence 0.92
Retrieved context: [GDPR Art. 7] Conditions for consent It shall be as easy to withdraw as to give consent. 8. When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the proc...
It's your right to request that we delete certain of your personal data.
Art.17 Right to Erasure confidence 0.89
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
Request that we erase certain of your personal data.
Art.17 Right to Erasure confidence 0.79
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
You’ll always have the option to change your mind and withdraw your consent at any time.
Art.7(3) Right to Withdraw Consent confidence 0.78
Retrieved context: [GDPR Art. 7] Conditions for consent It shall be as easy to withdraw as to give consent. 8. When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the proc...

##### Overall analysis
Across 279 clauses, 86 were flagged and 55 were cleared, with a mean flagged-clause confidence of 0.52. The highest-confidence flags describe retention after deletion and partners combining shared data with data from their services, while other flags address tailored ads for users under the appropriate age. The cleared clauses state that users can withdraw consent and request erasure, so the policy contains rights language alongside clauses the engine reads as purpose, retention, and profiling concerns.

##### Notes and caveats
138 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Deutsche Telekom Telecom
policy source
- LINK: [policy source](https://www.telekom.com/en/general/data-protection-information)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium-risk policy with a compliance pattern centered on purpose expansion and secondary use, international transfers, and cookie or analytics consent. The dominant flagged bases are Article 5(1)(b) Purpose Limitation, the ePrivacy Directive with Article 7 Consent, and Article 44 International Transfers, with additional flags touching storage limitation and Article 17 erasure.

##### How this was scored
How this was scored: 175 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 51 flagged clauses
      , most of them under Art.5(1)(b) Purpose Limitation violation .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 51 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
The data can be used for the partners’ advertising purposes, processed further and combined with data from other sources.
Art.5(1)(b) Purpose Limitation confidence 0.84
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
In some cases, your data may also be processed in countries outside the European Union (so-called third countries), currently including:
Art.44 International Transfers confidence 0.75
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...
We use cookies and analytics technologies to get a better understanding of how our digital service is used.
ePrivacy Directive violation + Art.7 Consent confidence 0.70
Retrieved context: [GDPR Recital 30] Online Identifiers for Profiling and Identification 1. Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identi...
This data is not used to create individual user profiles, nor is it shared with third parties, and it is deleted after a maximum of seven days.
Art.5(1)(e) Storage Limitation + Art.17 confidence 0.69
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 30 by confidence. These are the clauses the engine read as GDPR-compliant.
We want you to know what personal data we collect, how it is used, and what choices you have in the process.
Art.5(1)(a) Transparency confidence 0.72
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
The respective service provider will inform you about how your personal data is processed.
Art.5(1)(a) Transparency confidence 0.71
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
What data is collected and for what purpose is it processed?
Art.5(1)(a) Transparency confidence 0.68
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
Where is my data processed?
Art.5(1)(a) Transparency confidence 0.68
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (3) adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed (‘data minimisation’); (4) accurate and, where necessary, kept up to date; every reasonable step must be taken to ensure t...

##### Overall analysis
Of 175 clauses analysed, 51 were flagged and 30 were cleared. The flagged clauses describe partner advertising, further processing and data combination, processing outside the European Union, cookie and analytics use, and a deletion statement assessed under storage limitation and erasure. The cleared clauses mainly provide transparency about collected data, processing purposes, choices, service providers, and processing locations, so the policy explains its practices while the engine identifies concerns in how those practices are used and governed.

##### Notes and caveats
94 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Vodafone Telecom
policy source
- LINK: [policy source](https://www.vodafone.com/site-services/privacy-and-cookies)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This policy presents a medium privacy and consent risk centered on using customer data for marketing, advertising, and personalised recommendations. The engine primarily flagged Article 5(1)(b) Purpose Limitation, Article 7(4) Conditional consent prohibition, and Article 7 Conditions for Consent issues, alongside ePrivacy Directive consent concerns.

##### How this was scored
How this was scored: 82 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 16 flagged clauses
      , most of them under Art.5(1)(b) Purpose Limitation violation .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 16 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
With customer permission, we will use customer data to market our products and services and for advertising to provide more accurate recommendations.
Art.5(1)(b) Purpose Limitation confidence 0.71
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
In order to provide these services, we need to use our customers’ personal information.
Art.5(1)(b) Purpose Limitation confidence 0.70
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
We can provide personalised advertisements you see online, if you have consented to cookies.
ePrivacy Directive violation + Art.7 Consent confidence 0.69
Retrieved context: [GDPR Recital 58] The Principle of Transparency 1. The principle of transparency requires that any information addressed to the public or to the data subject be concise, easily accessible and easy to understand, and that clear and plain language and, additionally, where appropriate, visualisation be...
Visit our Data Privacy and Cookie Policy for more information.
ePrivacy Directive violation + Art.7 Consent confidence 0.67
Retrieved context: [GDPR Recital 6] Ensuring a High Level of Data Protection Despite the Increased Exchange of Data 1. Rapid technological developments and globalisation have brought new challenges for the protection of personal data. 2. The scale of the collection and sharing of personal data has increased significan...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 26 by confidence. These are the clauses the engine read as GDPR-compliant.
We do not sell individual data to third-parties.
Art.5(1)(b) Purpose Limitation confidence 0.95
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
For example, customers can express their opt-in consent to the use of their communications metadata for marketing purposes or for receiving third party marketing messages, or they can opt-out from marketing entirely.
Art.7 Conditions for Consent confidence 0.74
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...
All permissions can be revoked and choices can be changed at any time.
Art.7(3) Right to Withdraw Consent confidence 0.71
Retrieved context: [GDPR Art. 7] Conditions for consent It shall be as easy to withdraw as to give consent. 8. When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the proc...
We do not share customers’ personal data otherwise, unless required by law or with the consent of the customer.
Art.7 Conditions for Consent confidence 0.69
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...

##### Overall analysis
The policy contains 16 flagged clauses and 26 cleared clauses among 82 analysed, with a mean flagged-clause confidence of 0.56. The flagged text permits marketing and personalised advertising based on customer data and cookie consent; the cleared text states that individual data is not sold, consent can be opted in or out, permissions can be revoked, and sharing is limited absent law or customer consent. The shape of the results is mixed. The engine saw specific concerns about purpose and consent conditions alongside stated limits and user controls.

##### Notes and caveats
40 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Booking.com Travel
policy source
- LINK: [policy source](https://www.booking.com/content/privacy.html)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a medium risk policy centered on purpose limitation, tracking, and disclosure of personal data. The engine flagged cross-session and cross-device linking, broad sharing with third parties and business partners, and sharing with advertising partners. The dominant basis is Article 5(1)(b) Purpose Limitation, alongside ePrivacy Directive findings, Article 28 findings, and Article 44 International Transfers findings.

##### How this was scored
How this was scored: 460 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 131 flagged clauses
      .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 131 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
If you have an account on our platform, we link your browsing activity across different sessions and devices to give you a continuous experience.
ePrivacy Directive violation + Art.5(1)(b) confidence 0.77
Retrieved context: [GDPR Recital 18] Not Applicable to Personal or Household Activities 1. This Regulation does not apply to the processing of personal data by a natural person in the course of a purely personal or household activity and thus with no connection to a professional or commercial activity. 2. Personal or ...
In certain circumstances, we’ll share your personal data with third parties.
Art.5(1)(b) Purpose Limitation confidence 0.77
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...
We may share some of your personal data (such as identifiers) with advertising partners, as part of the marketing of our trip services through third parties (to ensure that relevant advertisements are shown to the right audience and to measure the effectiveness of different marketing activities).
Art.5(1)(b) Purpose Limitation confidence 0.74
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
We may share personal data in other instances with other business partners.
Art.5(1)(b) Purpose Limitation confidence 0.74
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 72 by confidence. These are the clauses the engine read as GDPR-compliant.
You can ask us for a copy of the personal data we hold about you.
Art.15 Right of Access confidence 0.89
Retrieved context: [GDPR Art. 15] Right of access by the data subject 1. The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information:...
You can ask us to erase the personal data we hold about you when, for example, it is no longer needed or we have asked for your consent and you later withdraw it.
Art.17 Right to Erasure confidence 0.80
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
Where we have collected and processed your personal data on the basis of your consent, you can withdraw that consent at any time, subject to applicable law.
Art.7(3) Right to Withdraw Consent confidence 0.80
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...
We use retention practices to keep and, where possible under applicable law, dispose of personal data.
Art.5(1)(e) Storage Limitation confidence 0.74
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...

##### Overall analysis
The flagged set contains 131 clauses, including 46 with no basis match and 38 marked as Article 5(1)(b) Purpose Limitation violations. The cleared set contains 72 clauses covering access, erasure, consent withdrawal, and storage limitation. The policy therefore combines stated data subject rights and retention practices with broader tracking and sharing provisions that the engine treats as insufficiently limited.

##### Notes and caveats
257 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Telefónica Telecom
policy source
- LINK: [policy source](https://www.telefonica.com/en/privacy-policy)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This is a low, targeted international transfer compliance risk. The engine flags questions about recipients, transfers outside the EEA, and safeguards for those transfers, primarily under Article 44 International Transfers and Articles 44 to 49 International Transfers. Additional flagged clauses concern Article 5(1)(b) Purpose Limitation with Article 28, and Article 7 Conditions for Consent.

##### How this was scored
How this was scored: 87 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 12 flagged clauses
      , most of them under Art.44 International Transfers violation .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 12 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
Who is the recipient of the data? are there any international transfers of data?
Art.44 International Transfers confidence 0.78
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...
In general, we will avoid international transfers of data and your data will be processed within the European Economic Area.
Art.44-49 International Transfers confidence 0.71
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...
However, in the event that such international transfers are necessary, we will take the necessary organisational, technical and contractual measures to ensure the protection and security of your data, such as, for example, signing the European Commission’s Standard Contractual Clauses with the authorised subcontractor or third party recipient, carrying out impact assessments on the relevant international transfer to assess the risk and adopt measures to mitigate it, encryption of data in transit or at rest, pseudonymisation of the data transferred, the possibility for the data subject to claim damages directly against the authorised subcontractor or third party recipient, etc.
Art.44-49 International Transfers confidence 0.69
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...
Where authorised subcontractors acting on behalf of Telefónica or such recipients are located or process your data outside the European Economic Area, we will be making an international transfer of your data in accordance with applicable data protection legislation.
Art.44 International Transfers confidence 0.63
Retrieved context: [GDPR Art. 44] General principle for transfers 1. Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if, subject to the other provisions of this Regulation, the condi...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 35 by confidence. These are the clauses the engine read as GDPR-compliant.
This is your right to ask us for details of the data we hold about you and how we process it, and to obtain a copy of it.
Art.15 Right of Access confidence 0.82
Retrieved context: [GDPR Art. 15] Right of access by the data subject 1. The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information:...
This is your right to request deletion or suppression of your data and information in certain circumstances.
Art.17 Right to Erasure confidence 0.79
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
We are 100% transparent with you about the data we collect and/or process about you and explain why we use it and for what purposes.
Art.5(1)(a) Transparency + Art.13 Right to be Informed confidence 0.74
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
How long is the data retained?
Art.5(1)(e) Storage Limitation confidence 0.70
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (5) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data wi...

##### Overall analysis
The flagged clauses describe conditional transfers and related processing arrangements, while the cleared clauses recognise access, erasure, transparency, and storage limitation rights. Of 87 clauses analysed, 12 were flagged and 35 were cleared, with a mean flagged-clause confidence of 0.57. The policy therefore shows concentrated transfer concerns alongside clear statements about several individual rights and information duties.
[auto-filed as T-0042 - pass --task next time to group it]

##### Notes and caveats
40 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

#### Orange Telecom
policy source
- LINK: [policy source](https://www.orange.com/en/privacy-policy)
No snapshot yet.

#### Adyen Payments
policy source
- LINK: [policy source](https://www.adyen.com/privacy-policy)
Last fetched 2026-10-29 · first snapshot

##### Analyst summary
TermsGuard's reading: This policy presents a medium compliance risk centered on broad disclosure and data-sharing practices. The engine primarily flags Article 5(1)(b) Purpose Limitation and Article 28 Processor concerns, with additional Article 7 Consent, Article 5(1)(a) Transparency, and Article 82 Controller Liability issues. It reads the policy as permitting sharing with third parties, service providers, advisers, and group companies without consistently limiting or explaining the purposes.

##### How this was scored
How this was scored: 92 clauses were extracted from the
      policy and matched against the 102 hand-labelled reference clauses
      ( 52 fair, 50 unfair). The top match for each
      clause was checked against the 550 -chunk reference index of the actual GDPR text
      ( 99 articles + 173 recitals), and the matching
      article was attached to the flag. The score is the mean confidence of the 28 flagged clauses
      , most of them under Art.5(1)(b) Purpose Limitation + Art.28 .
      No model verification on this run; cosine + GDPR retrieval only.

##### Flagged clauses · what TermsGuard thinks you should read
Top 4 of 28 by confidence. Each clause shows the matched GDPR article and the passage the engine used.
If you would like further details on any of the third parties your personal data is “sold” to or “shared” with, would like to know the purpose of their data processing, the manner in which data is processed, or how you can communicate with such third party to exercise your data privacy rights, please contact dpo@adyen.com, or lgpd@adyen.com if you are located in Brazil.
Art.5(1)(b) Purpose Limitation confidence 0.67
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...
If you have enabled the Global Privacy Control mechanism on your browser, device, or platform, you will automatically be opted out of any “sharing” when you use our website.
Art.7 Consent + Art.5(1)(a) Transparency confidence 0.62
Retrieved context: [GDPR Art. 7] Conditions for consent It shall be as easy to withdraw as to give consent. 8. When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the proc...
Where necessary, we will disclose your information to our service providers and professional advisers (e.g.
Art.5(1)(b) Purpose Limitation + Art.28 confidence 0.62
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data (6) processed in a manner that ensures appropriate security of the personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organ...
We may also disclose information with your permission (such as if we wish to disclose your details with another group company for their recruitment purposes).
Art.5(1)(b) Purpose Limitation + Art.28 confidence 0.61
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...

##### Cleared clauses · what TermsGuard reads as protective
Top 4 of 14 by confidence. These are the clauses the engine read as GDPR-compliant.
Right to deletion: You may be entitled to request that we delete the personal data that we have collected from you.
Art.17 Right to Erasure confidence 0.83
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
You may have the following rights regarding your personal data, subject to to certain exceptions:
Art.17 Right to Erasure confidence 0.76
Retrieved context: [GDPR Art. 17] Right to erasure (‘right to be forgotten’) (4) the personal data have been unlawfully processed; (5) the personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject; (6) the personal data have been collected in...
In addition, where you have given your consent for us to process personal data, you can withdraw this consent at any time.
Art.7(3) Right to Withdraw Consent confidence 0.76
Retrieved context: [GDPR Art. 7] Conditions for consent 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. 1. If the data subject’s consent is given in the context of a written declaration which also concer...
The table below provides a summary of the categories of personal data that we collect and disclose to service providers and other third parties.
Art.5(1)(a) Transparency confidence 0.63
Retrieved context: [GDPR Art. 5] Principles relating to processing of personal data 1. Personal data shall be: (1) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’); (2) collected for specified, explicit and legitimate purposes and not furt...

##### Overall analysis
The engine analysed 92 clauses, flagged 28, and cleared 14, with a mean flagged-clause confidence of 0.51. The flagged clauses focus on third-party sharing, processing purposes, service providers, professional advisers, and recruitment disclosures. The cleared clauses cover deletion rights, consent withdrawal, and a table summarising data categories disclosed to service providers and third parties. The policy therefore states several data subject rights and disclosure categories, while the flagged set concentrates on the scope and conditions of those disclosures.
[auto-filed as T-0043 - pass --task next time to group it]

##### Notes and caveats
50 clauses were left uncertain. They sit between the fair and unfair reference sets and the engine did not commit.
The verification model is not configured for this corpus run. Cosine similarity + GDPR-article retrieval are the only signals.
This is a measurement of the published policy text, not the company's actual data-handling practice. The policy can be more or less protective than the practice.
Latest diff
No diff yet (first snapshot).

### What this is and is not
This page is a record of TermsGuard's measurement of the consumer-facing
      privacy policy each company publishes. It is not a legal audit. It is
      not a comparison (each company's score is independent). It is not a
      guarantee of freshness. Companies change their policies without
      notice. The numbers reflect the policy as it was on the date shown.
The corpus is fetched on a weekly cadence via GitHub Actions.
      Source: terms-guard-ai on GitHub. The live demo this corpus powers: newtazer-terms-guard-ai.hf.space .
- LINK: [terms-guard-ai](https://github.com/iamtamilore/terms-guard-ai)
- LINK: [newtazer-terms-guard-ai.hf.space](https://newtazer-terms-guard-ai.hf.space)

### How to read this
The score is a measurement of one document at one point in time, not a verdict.
    Treat it like a temperature reading: useful as a signal, not a diagnosis.
    The flagged-clause list is the engine's best read of where a privacy-aware reader would push back, not a legal determination.
    The cleared-clause list is the engine's best read of where the policy is committing to user protection.
    The diff between two snapshots is a literal text diff; the prose around it is the engine's interpretation of what changed.
    None of this replaces legal review.
- LINK: [Taiwo Alabi](/)
- LINK: [CV](/cv/)
- LINK: [TermsGuard write-up](/p/termsguard/)

---

## PAGE: /how/

- LINK: [index](/)
- LINK: [cv](/cv/)
- LINK: [skim](/skim/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
- LINK: [episodes](/products/)
- LINK: [channels](/channels/)
- LINK: [jobs](/jobs/)

## I can show you every step, not just the result
Here is one short video I made, from an empty folder to a finished file. The script, the timings,
    the pictures, the ones I threw away, and the cost of each step are all left in. You do not have
    to take my word for any of it.
- LINK: [Watch the full short →](https://www.youtube.com/watch?v=9zhPG7aJQy8)

### If you are here to hire someone, this is the part for you
The anime is the example. The thing worth looking at is how it was made.
I built the machine that runs this, and I kept every log it produced. Search, scoring,
      selection, generation, assembly, and a check that catches what the other steps miss.
      A model narrows the options. I decide. On this run I threw out roughly half the
      pictures I had already picked, because looking at them properly showed they were wrong.
That habit is the whole pitch. I am not showing you that I can make a video. I am showing you
      that I check my own work, throw away what does not pass, and leave the evidence where you
      can audit it. Same rule on the four AI systems on my home page: every one names the failure
      it defends against before the feature it adds.
See the CV See the raw logs
- LINK: [See the CV](/cv/)
- LINK: [See the raw logs](/provenance/)

### If you are a brand looking to commission this
Short video is cheap to make and expensive to trust. Most suppliers send you the finished
      file and ask you to believe the rest. This page does the opposite. You get every input, every
      picture that was rejected, and every timing decision.
You get the same log I keep for myself. That is the difference between a supplier
      telling you the work is good and being able to check that it is.
Real channel numbers, for calibration: 347 subscribers, 4 videos, best one 1,200 views.
      Small, and stated rather than dressed up. The pipeline is what scales.
Email me Full run log
- LINK: [Email me](mailto:newalabitaiwo625@gmail.com)
- LINK: [Full run log](/provenance/)

---

## PAGE: /meet/

- LINK: [Skip to main content](#main)

## An AI systems engineer who ships measured product, runs a measured channel pipeline, and verifies every claim against the actual measurement.
Found a reporting gap that had been sending the wrong subscriber numbers upstream for months, and fixed it. Currently a part-time Receptionist at Temple Bar Townhouse, finishing an MSc in Artificial Intelligence at NCI Dublin.
Taiwo Alabi · MSc AI, NCI Dublin

### The one that ships
- LINK: [01 TermsGuard AI Reads privacy policies and flags risky clauses, grounded in the exact rule text. A pure cosine classifier gets negation backwards, so the classifier proposes and a model rules. 102 Reference clauses (52 fair, 50 unfair) 4,527 Chunks in retrieval index 15 Clauses routed to model per analysis Live demo ↗](/p/termsguard/)

#### TermsGuard AI
Reads privacy policies and flags risky clauses, grounded in the exact rule text. A pure cosine classifier gets negation backwards, so the classifier proposes and a model rules.

### A weekly privacy audit run, scored live
- LINK: [Last run 2026-10-29 · 14 of 17 fetched · 101 seconds Weekly run across EU banks, retailers, telecoms, and Big Tech Each week the corpus tracker re-pulls the privacy policies of the indexed companies, runs the latest TermsGuard build against the fetched text, and writes the per-company score, risk label, and flagged-clause count to a dated snapshot. The corpus page renders the score table, per-company detail cards, and the change-since-last-run diff. 953 Flagged clauses this run 0.54 Median score across 14 working companies 14 Companies at Medium risk this run Live corpus ↗](/corpus/)

#### Weekly run across EU banks, retailers, telecoms, and Big Tech
Each week the corpus tracker re-pulls the privacy policies of the indexed companies, runs the latest TermsGuard build against the fetched text, and writes the per-company score, risk label, and flagged-clause count to a dated snapshot. The corpus page renders the score table, per-company detail cards, and the change-since-last-run diff.

### AI-driven creative production, measured end to end

#### Super Zenpai
Hard-cut short-form, 18-25 shots per episode. Subject selection measured against a real 366-video reference census.
- LINK: [Forgotten Fronts Reverse-engineered history shorts built from primary sources. Each episode ships with the contact sheet, the source-vs-claim audit, and the drift-bug fix if one was needed. 19 shots EP_MUSASHI contact sheet 40.1s EP_MUSASHI duration, 1080x1920 33 / 16 Claims confirmed / dropped by audit 876 24h YouTube views, EP_MUSASHI](/products/forgotten-fronts/)

#### Forgotten Fronts
Reverse-engineered history shorts built from primary sources. Each episode ships with the contact sheet, the source-vs-claim audit, and the drift-bug fix if one was needed.

### ask.py blueprint recipes I actually run

#### Generate a 60-second short-form anime episode
qwen3-vl-235b (select) / qwen-image (stills) / gpt-audio (narration) / ffmpeg (assembly)
Source 50 candidate frames per shot-need from kie.ai, scoped per beat
Score each candidate with qwen3-vl against the brief's NEVER rules
Pick top 12-14 stills per episode, crop to 1080x1920
Generate narration via gpt-audio, time-stamp against the beat structure
Assemble with ffmpeg, hard-cuts on narration, one yellow word per shot
~ 1.50 USD inbound, 0.5 credits outbound per episode

#### Capture a hero image from a real reference
flux-2/pro-image-to-image
Pass the reference as the only input_url, no other text
Prompt for natural skin texture, visible pores, no retouching
Set resolution 1K, nsfw_checker false, aspect_ratio 3:4
Generate best-of-5, pick the lock, never the prettiest
Verify EMB_SIM against the reference (target above 0.98)
~ 5 credits per capture, EMB_SIM 0.9906 vs 0.9802 on the benchmark

#### Edit a product photo on a reference
gpt-image-2-image-to-image, quality high
Subject ref first, garment or product ref second, plain prompt
No cropped detail ref, no colour swatch, no colour-naming
Set aspect_ratio to target surface, 3:4 for cards, 1:1 for thumbnails
Keep negatives light, aggressive negatives cause drift on this model
Best-of-5, verify text and product match by eye, OCR lies
~ 6 credits per edit, text-in-image and complex multi-ref both clean

#### Score a contact sheet of stills
qwen3-vl-235b via OpenRouter
Compose 16-22 stills into one contact sheet at 768px wide
Send image plus brief's per-frame rules in the same prompt
Ask for one-line verdict per frame plus a single overall verdict
Reject if "NO VERDICTS" returned, usually means per-need queries were identical
Keep verdicts as text, never rely on the model's confidence score
0 USD per call on OpenRouter, rate-limit the only real constraint

### Find the work
- LINK: [iamtamilore.github.io site](/)
- LINK: [linkedin.com/in/tami-alabi linkedin](https://www.linkedin.com/in/tami-alabi/)
- LINK: [github.com/iamtamilore github](https://github.com/iamtamilore)
- LINK: [TermsGuard live demo hf space](https://newtazer-terms-guard-ai.hf.space)
- LINK: [Privacy corpus tracker weekly](/corpus/)

### If you'd like
- LINK: [View full CV](/cv/)
- LINK: [Email me](mailto:newalabitaiwo625@gmail.com)
- LINK: [Download wallpaper](/meet/wallpaper.png)
This page routes to a single QR on a phone lock screen. Scannable at 60cm, in event light, with no zoom. Every number on this page traces to a measurement in a project README or a dated journey observation. Departures from the site design system are recorded in DESIGN.md .

---

## PAGE: /oap/

- LINK: [Home](/)
- LINK: [CV](/cv/)
- LINK: [Work](/work/)
- LINK: [Jobs](/jobs/)
- LINK: [Atoms](/atoms/)
- LINK: [OAP](/oap/)
- LINK: [Bank](/bank/)

## O.A.P. Trainer
Social Dynamics Lab
Newtazer
Loading...

### Good evening, Newtazer
Ready for today's training session?
5
of 1,217 total
-
Total practiced
- /10
Across all scored sessions
Not built yet
/api/stats has no streak field

#### Start SRS Training
Review due cards

#### Practice Scenarios
AI-generated Dublin scenarios

#### Browse Library
1,217 O.A.P. examples

#### Training Activity

#### Recent Sessions
Loading recent activity...

### SRS Card Review
Spaced repetition training session
Context
You're at a coffee shop in Dublin, and you notice a girl reading a book you've read recently...
👁 OBSERVE
She's reading "The Secret History" - a sign of intellectual curiosity. She's alone, relaxed body language, occasionally looking up.
🔧 ASSEMBLE
Use the book as a natural conversation starter. Reference something specific about it. Keep energy light and curious.
✨ PLAYFUL STATEMENT
"Oh no, you're reading that? I hope you're prepared for the emotional damage  -  I had to take a week off after finishing it."
How well did you know this?

#### Session Complete!
Great work on today's review
5
Cards Reviewed
3:24
Time Spent
80%
Good or Better

### Scenario Practice
AI-generated Dublin scenarios with real-time feedback
You're at a friend's house party in Dublin 2. The music is loud, people are mingling. You spot a girl standing near the kitchen island, looking at her phone occasionally but clearly not deeply engaged. She makes brief eye contact with you and gives a small smile before looking back at her phone. Your friend is nowhere to be seen.
STRENGTHS
Good natural opener that references the environment. The playful tone works well for this context. You're showing social awareness by not being too direct.
IMPROVEMENTS
Consider adding more specificity to make it memorable. The energy could be slightly higher to match the party vibe. Try to leave an open loop for her to respond to.
WHY IT WORKS
This approach works because it's low-pressure, shows you're socially calibrated to the environment, and creates a natural hook for conversation without being needy.
"Haha yeah, it's been a long week. I needed to get out of the house. Are you friends with the host?"
Excellent follow-up! You maintained the playful energy while showing genuine interest. The callback to your opener creates continuity, and asking about her creates a natural exchange. Great social calibration.

#### Practice Session Complete!
Here's how you did across 3 scenarios
3
Scenarios
7.8
Avg Score
6
Responses
8:42
Duration

### Example Library
Browse and search all 1,217 O.A.P. examples

### Analytics
Track your progress and identify areas for improvement

#### Average Score Over Time

#### Branch Distribution

#### Areas for Improvement

#### Training Volume (Last 30 Days)

#### Detailed Statistics
342
Total SRS Reviews
47
Scenarios Completed
24h
Total Training Time
89%
Retention Rate

### Settings
Configure your training environment

#### API Configuration

#### Training Configuration

#### Appearance
Dark Mode
Easier on the eyes for night practice

#### Data Management

#### Example Details

---

## PAGE: /products/ep_speedmaster/

- LINK: [← How I make an episode](/how/)
- LINK: [All episodes →](/products/)

## EP_SPEEDMASTER, the reverse-engineered episode
A 3-scene vertical anime episode, deconstructed so a brand can see exactly what they're paying for. Three shots, one QA gate per shot, one full frame extraction set per shot.

### 1. The shape of the work
This episode shipped 4 July 2026 as the first end-to-end run of the seed blueprint (this page) that became the luxury blueprint (see the blueprint page ). Three scenes, each with three frames extracted at t=0%, t=50%, t=98% of duration. One QA gate per scene. ~3 minute total runtime. One writer, one QA system, one set of kie.ai generation calls, visible below.
- LINK: [blueprint page](/products/blueprint.html)
Output: 3 MP4 scenes (s1_establish, s2_deepen, s3_exit), 9 frames total (3 per scene), 1 QA JSON file with all 9 vs-seed and vs-hero similarity scores.
Source files: products/ep_speedmaster/

### Scene 1: s1_establish , 9.2s
Establishes the setting: empty street, rain beginning, character mid-stride. Sets the visual baseline for the rest of the episode.

### Scene 2: s2_deepen , 7.6s
Deepens the rain and the character's posture. The most dramatic frame in the episode.

### Scene 3: s3_exit , 8.0s
The character leaves the frame. Lowest similarity scores of the three scenes, that's correct: exit means departing from the reference, not staying close to it.

### The QA gate that ran
Every scene was measured against two reference images using the same gate that runs on every frame in every batch, qa_selector.py (ResNet50 cosine similarity, threshold M16.8, 16.9 calibrated on a reference bank held out from the active training run).
The pass/fail criterion is: both vs-seed and vs-hero stay within the calibrated band for the scene type. Catastrophic divergence triggers an automatic regenerate; stylistic drift within tolerance does not. See the blueprint page for the full gate logic, the regeneration budget, and the calibrated thresholds.
- LINK: [blueprint page](/products/blueprint.html)

#### Raw QA JSON

### What the brand sees vs what the agent does
The brand receives three video files and a single QA report. They do not see the prompts, the regeneration logic, or the threshold tuning. That's the whole point of the gate, the brand signs off on "the character looks like the character", not on the mechanism that ensures it.
For brands that want to see the mechanism, to verify the work is auditable, not just trusted, this page is the entry. The full production system is documented in the blueprint ; the higher-end version (the luxury tier that adds a four-ward expert routing panel, an AIDM Thompson-sampling credit allocator, and an EEAI leakage audit) is on the same blueprint at the luxury tier.
- LINK: [blueprint](/products/blueprint.html)
- LINK: [All episodes](/products/)
- LINK: [See the blueprint](/products/blueprint.html)
- LINK: [How I make an episode](/how/)

---

## PAGE: /products/forgotten-fronts/

- LINK: [← All products](/products/)
- LINK: [EP_MUSASHI reverse-engineered →](/products/forgotten-fronts/ep_musashi.html)

## Forgotten Fronts
One of three channels run by Taiwo Alabi. This is the live one. Two episodes shipped in 24 hours: EP_MUSASHI (2026-10-27, 876 first-day views, 65.3% retention) and EP_BOOK_OF_FIVE_RINGS (built, ready to ship).

### What the channel is
Dark history. The events, regimes and people history skipped over - the kind with a story that took decades to come out. Episodes weekly, shorts three times a week, long-form once a month. Every claim is traceable to a Wikipedia article, Britannica entry, or the primary document the article cites.

#### Identity
Display name: Forgotten Fronts YouTube / Instagram / TikTok / Facebook handle: @forgottenfronts0 Tagline: "What they buried. Why it broke. The history they didn't teach you."

#### First 24h measurement
EP_MUSASHI: 876 views , 65.3% retention, 21 likes, 21 comments. EP_BOOK_OF_FIVE_RINGS: 6 views (built, awaiting upload). Studio aggregate: 984 views, 0 new subscribers . Two readings, can't separate signal from lag yet - subscriber attribution on a brand-new channel is always slow.

#### Format
Vertical narration-driven Short, ~40 seconds, 1080x1920, 19 shots. Hard cuts on beat boundaries (no blur whip). 2-4 word captions, white with exactly one yellow word. Single narrator, episode length locked to the narration.

### The two episodes

#### EP_MUSASHI - shipped 2026-10-27
Miyamoto Musashi defeats Sasaki Kojiro at Ganryu Island with a wooden bokken instead of steel, by arriving late to unbalance Kojiro's composure. 40.1 seconds, 19 shots, 136 words. First-day: 876 views, 65.3% retention, 21 likes, 21 comments. QA gate: 15 confirmed, 2 dropped.
- LINK: [View the breakdown](/products/forgotten-fronts/ep_musashi.html)

#### EP_BOOK_OF_FIVE_RINGS - built, ready to ship
The closing promise of EP_MUSASHI. The Book of Five Rings written by Musashi after his duelling days. EP_BOOK_OF_FIVE_RINGS.mp4 (14.2 MB), built and gated, closing-caption pointing at the next subject (the duel series continues).

#### EP_CANNAE - planned, not built
The named next subject after Book of Five Rings: 216 BC, Hannibal crosses the Alps with elephants and defeats Rome at the Battle of Cannae. The named-next from the source-channel insights: war/military subject ratio is 3.35x per channel on n=266.

### The pattern this episode proves
EP_MUSASHI took 40.1 seconds to ship a real fact-checked history episode with 65% retention. That's the whole proof: dark history as a subject carries, the format holds attention, and the gate catches defects without blocking the build. Next 10-20 episodes test whether subscribers convert.
- LINK: [See the full breakdown](/products/forgotten-fronts/ep_musashi.html)
- LINK: [Workflow blueprint](/products/workflow/)
- LINK: [All products](/products/)

---

## PAGE: /products/

- LINK: [index](/)
- LINK: [cv](/cv/)
- LINK: [skim](/skim/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
- LINK: [episodes](/products/)
- LINK: [channels](/channels/)
- LINK: [jobs](/jobs/)

## Episodes
The worked example, the workflow blueprint, and the three channels behind them. Every episode on the channels runs through the same five-stage pipeline with the same six hard-won rules.

#### The worked example: EP_SPEEDMASTER (Proof Tested)
A 24.8-second vertical episode on the Omega Speedmaster surviving NASA’s worst missions. Three scenes, nine frames extracted at t=0%/50%/98%, one QA gate per scene. 9/9 frames passed against the reference bank at vs-seed and vs-hero. Every measurement is shown on the page, what passed, what drifted within tolerance, what the gate’s pass/fail criterion is, and why the lowest scores are still a pass. The Speedmaster episode is built, gated, and ready to upload.
- LINK: [View the breakdown →](/products/ep_speedmaster/)
- LINK: [Watch s1 (8.8s)](/products/ep_speedmaster/s1_establish.mp4)
- LINK: [Watch s2 (7.8s)](/products/ep_speedmaster/s2_deepen.mp4)
- LINK: [Watch s3 (8.2s)](/products/ep_speedmaster/s3_exit.mp4)
- LINK: [All channels →](/channels/)

#### The QA gate, separately: EP_MUSASHI
A second worked example on the QA gate, applied to a different shipped episode. 19 frames extracted from one Wikipedia article, every frame gated against a hero reference, every claim cross-checked against the source. EP_MUSASHI shipped live on YouTube and TikTok on 2026-10-27 and kept 65.3% of viewers past the midpoint.
- LINK: [View the breakdown →](/products/forgotten-fronts/ep_musashi.html)
- LINK: [19-shot contact sheet](/products/forgotten-fronts/ep_musashi.html#contact-sheet)
- LINK: [Watch the MP4](/products/channels/forgotten_fronts/ep_musashi.mp4)

#### The workflow blueprint
The five-stage pipeline (plan, select, build, gate, post) plus the six hard-won rules the pipeline enforces automatically. One rule per failure that cost real time or money to learn. Every rule is documented with its measured cost, and the production code that enforces it is named and fileable. A brand can audit this end-to-end without any agent involvement.
- LINK: [Read the blueprint](/products/blueprint.html)

### The channels behind the work
Three channels ship on the same five-stage pipeline. Each has its own measured subject catalog. Click a thumbnail to see the channel breakdown; the handle links to the real platform channel.
- LINK: [@forgottenfronts0](https://www.youtube.com/@forgottenfronts0)
Status: LIVE. EP_MUSASHI shipped 2026-10-27 with 65.3% retention. Next: EP_CANN AE (216 BC, the named next subject).
- LINK: [View breakdown →](/products/forgotten-fronts/)
- LINK: [Watch EP_MUSASHI](/products/channels/forgotten_fronts/ep_musashi.mp4)
- LINK: [All channels →](/channels/)
- LINK: [@prooftested0](https://www.youtube.com/@prooftested0)
Status: EPISODE 1 BUILT AND GATED. EP_SPEEDMASTER (24.8s, 3 scenes, 9 frames, every claim verified against Wikipedia). Awaiting upload. Next: EP_APOLLO13.
- LINK: [View worked example →](/products/ep_speedmaster/)
- LINK: [Watch EP_SPEEDMASTER](/products/channels/luxury_archive/ep_speedmaster.mp4)
- LINK: [All channels →](/channels/)
- LINK: [@zenpaitv_](https://www.tiktok.com/@zenpaitv_)
Status: FORMAT BUILT, 13 EPISODES SHIPPED INTERNALLY. Proof the pipeline ships Demon Slayer lore. Subject ratios measured: Tengen 3.77x, Sanemi 1.91x, Upper Moons 1.47x.
- LINK: [Watch EP_OBANAI](/products/channels/zenpai/ep_obanai.mp4)
- LINK: [All channels →](/channels/)
Status: TEST-BED. anime_hive is the format R&D playground (4 experimental episodes). capital_postmortem is empty, needs its own subject scrape before launch.
- LINK: [Watch EP_GOJO](/products/channels/anime_hive/ep_gojo.mp4)
- LINK: [All channels →](/channels/)

### What the brand sees
The brand signs off on "the character looks like the character", not on the mechanism. The blueprint is the proof that the work is auditable : every claim traces to a Wikipedia source, every frame is gated against a reference, every NEVER rule has a name and a beat it applies to, and every failure mode is documented with the cost it took to learn it.
The pipeline is in ~/repos/zenpai-pipeline (mirrored from /mnt/2b ). The 6 hard-won rules in _LESSONS_HARD_WON.md are the operating manual. The worked example here (EP_SPEEDMASTER) is one of 3 shipped luxury_archive episodes, but it's the one that shows the QA gate's actual measurements end-to-end so a brand can verify the work without taking anyone's word for it.

---

## PAGE: /products/workflow/

- LINK: [← All products](/products/)
- LINK: [Contact sheets →](/products/workflow/contact-sheets.html)

## Workflow blueprint
The five-stage pipeline that runs every channel. Plus six rules the pipeline enforces automatically - one per failure that cost real time or money to learn.

### The pipeline
Plan, select, build, gate, post. Every episode on every channel goes through these five stages. The gate is the load-bearing one - that's why it carries the only warm colour in the diagram.

### The six rules
Each rule closes one class of failure. The cost is the proof - real time, real money, or real defects that would otherwise have shipped.
Estimated beats never match the TTS pauses. Plan after the audio, not before.
Identical queries put the same 50 jpgs in every folder; the selector dedups globally, so half the needs see nothing.
"No Kanao" rejected the very need whose line is "Then he met Kanao." Constraints are per-beat, not global.
A timeout reads as a model fault unless the selector logs transport separately. The selector never silently swallows stderr.
Six frames passed at 640px and failed at full resolution. Confirm any "wrong character" call by opening the source PNG.
A claim only goes in if the source states it. Two claims dropped from Musashi for being unsourced; one added to Speedmaster because it was sourced.

### The QA gate that actually runs
The gate runs ResNet50 cosine similarity at three frame positions per scene, then asks a vision model for a modern/anachronism check. The pass/fail criterion is calibrated against the reverse-engineered luxury episode:
The numbers are vs-seed / vs-hero. The third scene has the lowest scores and that is correct - a character walking away should diverge from the reference. The gate flags catastrophic divergence, not stylistic movement.

### What the workflow proves to a brand
A brand evaluating this work signs off on "the character looks like the character" - not on the mechanism. The blueprint is the proof that the work is auditable end to end: every claim traces to a source, every frame is gated against a reference, every rule has a name and a measured cost, and every failure mode is documented.
- LINK: [See Stage 2 (contact sheets)](/products/workflow/contact-sheets.html)
- LINK: [Forgotten Fronts channel](/products/forgotten-fronts/)
- LINK: [EP_MUSASHI breakdown](/products/forgotten-fronts/ep_musashi.html)

---

## PAGE: /provenance/

- LINK: [index](/)
- LINK: [cv](/cv/)
- LINK: [skim](/skim/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
- LINK: [episodes](/products/)
- LINK: [channels](/channels/)
- LINK: [jobs](/jobs/)

## Every image shows its own receipt
This is the raw record behind every published short on the channel: each generation call, the model
    that made it, the prompt, the references, the credits, how long it took, and what was kept or thrown
    away. It is the part of the work most projects leave out.

### First, the honest numbers
I wanted to publish this as a museum of my most viral episodes. I cannot, because the numbers do
      not say that. Here is what the channel actually is, measured, not estimated.
A thousand views is a start, not a success, and calling it a hit would be the same mistake as
      putting a role on a CV that was never held. So this page leads with the study and the record
      instead, which is the part that is genuinely unusual.

### What a receipt contains
Four records joined by a single task id: what was requested, what came back, what I decided, and
    what the quality gate measured. If any of those are missing for a call, the row says so rather than
    showing a zero.

### The pictures, and the receipt behind each one
Every thumbnail below is the actual file that call produced, not a stand in. Tap any one to
    see the prompt that made it, what it cost, how long it took, and what the quality gate measured.
    A receipt with nothing attached is a claim. This is the evidence.
Sourced from the study's own append-only run log. Nothing here was summarised by hand. See the tooling · Back to the portfolio
- LINK: [See the tooling](/tools/)
- LINK: [Back to the portfolio](/)

---

## PAGE: /rater/

- LINK: [portfolio](/)
- LINK: [tools](/tools/)
- LINK: [corpus](/corpus/)
- LINK: [home](/)
You are judging what a generated garment image actually shows, not whether it
      looks good. 85 images, one at a time. Nobody will see your answers and nobody will
      grade you.

#### Judge the picture, not the garment
Ignore the fabric, the colour, the lighting and the styling. You are looking at construction:
          the hood, the collar, the small metal hardware.

#### Count exactly
If you can see three toggles, say three. Binning counts into ranges hides exactly the
          variation this study is measuring.

#### Say when you cannot tell
"Cannot determine" is a real answer and is treated as one. It is kept off the other scales on
          purpose, because a guess is worse than a gap.

#### Zoom in
Eyelets and cord toggles are small. Use the + control and scroll or drag to look closely
          before you answer.

#### Question 1 comes first, and it is a real gate
If the collar area is too obscured or too small to judge, answer no and the rest is
        skipped. That is not giving up. It is the most useful thing you can do, because a study that records
        a judgement where there was no evidence is worse than one that records the gap.
Your progress saves in this browser as you go. Bookmark this page, because it carries your
        reference and is how you come back. When you finish all 80 , click Download my ratings and send the file back.

## Judge what the picture shows
85 garment images, one at a time. Answer only what you can see in this frame.
      Describe the construction, not whether you like it.
If no , the rest is skipped and only the note below is asked.
up is raised around or behind the head with a visible face opening , a cavity you could put a head through. down is folded behind the neck, or a stand collar band with no cavity. A thick roll of fabric at the back of the neck is down . Apply it literally.
Presence only. Counting is not required here.
Count the toggles only. Not the cord, not the eyelets. Exact numbers, no grouping.
If other colour , name the colour in the note below.
5 to 25 words. Only what is in the picture. If something stopped you judging reliably, say what.
        For example: clear face opening, cord ends hanging at chest . Not useful: looks fine .
Visibility answered no , so the detail questions are skipped for this item.
        Add the note below and lock it.
Everything stays in this browser. Nothing is sent anywhere until you download the file.
      Bookmark this page: it carries your rater id and is how you return to where you stopped.
Garment construction detail study. Conditions, item order and filenames are masked from this interface. About the tooling
- LINK: [About the tooling](/tools/)

---

## PAGE: /rater_v2_live/

- LINK: [portfolio](/)
- LINK: [tools](/tools/)
- LINK: [corpus](/corpus/)
- LINK: [home](/)
You are judging the geometry of a generated serpentine zip, not whether the garment looks good. 80 images, one at a time. Nobody will see your answers and nobody will grade you.

#### Count curves exactly
A serpentine zip has S-shaped waves. Count each full S-curve (one left-to-right-to-left oscillation) as one.
          If you see three waves, say three. Exact numbers, no bins.

#### Measure the swing
Does the zip path lean left, lean right, or stay centred? Pick the dominant direction of the overall path.

#### Say when you cannot tell
"Cannot determine" is a real answer. A guess is worse than a gap.

#### Zoom in
The zip teeth and curves are small. Use + and scroll or drag to look closely before you answer.

#### Question 3 is the visibility gate
If the zip region is too obscured or too small to judge, answer no and the rest is skipped.
        That is not giving up. It is the most useful thing you can do.
Your progress saves in this browser as you go. Bookmark this page, because it carries your
        reference and is how you come back. When you finish all 80 , click Download my ratings and send the file back.

## Judge the serpentine zip geometry
80 zip crops, one at a time. Answer only what you can see in this frame.
      Describe the construction, not whether you like it.
One full S-shape = one curve. Count exactly, no grouping.
left the zip path curves predominantly toward the wearer's left (viewer's right). centre the path stays roughly centred on the centre-front seam. right the path curves predominantly toward the wearer's right (viewer's left). Judge the dominant tendency of the whole visible path.
If no , the rest is skipped and only the note below is asked.
5 to 25 words. Only what is in the picture. If something stopped you judging reliably, say what.
        For example: three clear waves, gentle right lean . Not useful: looks fine .
Visibility answered no , so the curve and swing questions are skipped for this item.
        Add the note below and lock it.
Everything stays in this browser. Nothing is sent anywhere until you download the file.
      Bookmark this page: it carries your rater id and is how you return to where you stopped.
Serpentine zip geometry study. Conditions, item order and filenames are masked from this interface. About the tooling
- LINK: [About the tooling](/tools/)

---

## PAGE: /tools/

- LINK: [index](/)
- LINK: [cv](/cv/)
- LINK: [skim](/skim/)
- LINK: [how](/how/)
- LINK: [logs](/provenance/)
- LINK: [tools](/tools/)
- LINK: [episodes](/products/)
- LINK: [channels](/channels/)
- LINK: [jobs](/jobs/)

## Tools
The tools behind the work. Each one is something you can click right now to see the engineering, not read about it.

### The CV Static · github.io
Full CV with project write-ups, the framing grammar, and every code repo linked out.
- LINK: [Open CV](/cv/)
- LINK: [Download PDF](/Alabi_Taiwo_CV.pdf)

### TermsGuard AI Live · HuggingFace
Reads the small print in a privacy policy and flags the unfair parts.
Cosine similarity alone marks "we do not sell your data" as a violation, so a model verifier sits on top and rules on what is left. 102 reference clauses. 12-case regression suite runs against the deployed service, not a notebook.
- LINK: [Try the live demo](https://newtazer-terms-guard-ai.hf.space)
- LINK: [Case study](/p/termsguard/)
- LINK: [Code](https://github.com/iamtamilore/terms-guard-ai)

### Privacy Corpus Weekly · github.io
Watches 14 EU + Big Tech companies' privacy policies, scored weekly, with diffs.
Same GDPR-cosine engine as TermsGuard, pointed at a curated list. Each company's score is independent, dated, and reproducible. Companies whose sites bot-block automated fetches show up as 'no snapshot yet' until the protection lifts.
- LINK: [Open corpus](/corpus/)
- LINK: [Case study](/p/termsguard/)
- LINK: [Code](https://github.com/iamtamilore/terms-guard-ai)

### Portfolio Static · github.io
The main personal site. Project write-ups, the four-systems grid, the channel work, every repo linked out.
- LINK: [Open portfolio](/)
- LINK: [Episodes & channels](/products/)
- LINK: [Every call log](/provenance/)

### OCR Rater UI Static · github.io
Rater UI for the image-generation study. Eighty garments, four conditions, human-rated, blind.
Per-rater URLs carry a token so each rater's progress lives in their browser. Export is a single JSON file the rater emails back. No backend, no account, no tracking.
- LINK: [Open rater UI](/rater/)
- LINK: [mint.py (CLI)](/rater/mint.py)

### Image Generator (Mohit's UI) Live · Tailscale funnel
Flask app for the image-generation study. Four conditions, gallery of generated images, OCR accuracy feed.
Used by the second author of the study to run the four conditions end to end and inspect outputs without leaving the experiment folder.
- LINK: [Open generator](https://newtazer.tail1075c4.ts.net/)
Built as part of the dissertation tool chain. Hub regenerates from site-build/tools/index.html ; no build step.