[![CI](https://github.com/Abdalla-Wasaa/Week-11-Capstone-Project/actions/workflows/ci.yml/badge.svg)](https://github.com/Abdalla-Wasaa/Week-11-Capstone-Project/actions/workflows/ci.yml)

# Module 4 Capstone: AfyaPlus

## Overview
AfyaPlus is a local FastAPI capstone demo combining config-driven intent routing,
email redaction, grounded synthetic clinic lookup, and a stock tool in MCP stub mode.
The API path runs without a model key; tests, fixture diagnosis, evaluation, and
performance measurement provide build evidence. Live inference and deployment are deferred.

## Quick start

Clone `https://github.com/Abdalla-Wasaa/Week-11-Capstone-Project.git` and run commands
from its repository root. References to `module4-capstone` below describe the local
course folder; the published repository contains those files directly at its root.

From `module4-capstone`, with your virtual environment active:

```bash
pip install -r requirements.txt
pytest -q
```

## Docs
- [Architecture](docs/architecture.md)
- [Deployment](docs/deployment.md)
- [Cost analysis](docs/cost_analysis.md)
- [User guide](docs/user_guide.md)
- [Build checkpoint](docs/build_checkpoint.md)

## Demo
Start the API in one terminal:

```bash
uvicorn services.triage.app:app --host 127.0.0.1 --port 8080
```

In a second terminal (for a server with no API key configured):

```bash
curl -f http://localhost:8080/health
curl -f http://localhost:8080/triage -H 'Content-Type: application/json' -d '{"text":"track delivery of ors sachets"}'
```

See the user guide for authenticated requests.

## Presentation
[Ten-slide draft deck](docs/presentation.pdf) and [filled outline](docs/presentation_outline_filled.md) are ready for rehearsal. Week 12 delivery and backup recording are pending.

## Peer review
- review_log.md entry
- checklist: docs/peer_review_checklist.md

## Lab 1 testing

From `module4-capstone`, install dependencies with `pip install -r requirements.txt`.

- `pytest -q`: run units and security smoke without live services; integration and perf are excluded.
- `pytest tests/test_security_smoke.py -q`: run the security smoke checks explicitly.
- `ruff check .`: run the lint gate used in CI.
- `SERVICE_UP=1 pytest -q -m integration`: run integration tests with the service running at localhost:8080.
- `pytest -q -m perf`: select perf tests (none are currently defined).

Start the service with `uvicorn services.triage.app:app --port 8080`.
`GET /health` returns the health status. `POST /triage` accepts `{"text": "track delivery"}`
and calls the real service function in stub mode, redacting email addresses and routing the message.
The pin uses `model_id: stub-local` and prompt version `1.2.0`; no live model is implemented.
Choose and pin an actual model before adding live inference.

Set `TRIAGE_API_KEY` to enable the teaching auth stub, and send its value in `X-Api-Key`.
Without that variable the local stub endpoint permits requests without authentication.
The security smoke suite checks missing, incorrect, and valid keys with auth enabled.

## Lab 2 workflow

The stub `/triage` response now includes a deterministic grounded answer and source citations.
Logistics intents additionally invoke the stock tool through an in-process MCP `tools/call`
stub. The default stock item is `ors_sachets`; provide `item` in the JSON body to change it.
This is offline stub wiring, with no network MCP server or model inference.

```bash
python -m services.triage.rag_smoke
python scripts/make_fixture.py --rows 300 --out fixtures/triage_messages_sample.jsonl
python scripts/diagnose_fixture.py fixtures/triage_messages_sample.jsonl
python evals/run_eval.py evals/golden.jsonl
```

With the API running on port 8080 in another terminal:

```bash
SERVICE_UP=1 pytest -q -m integration
python scripts/measure_perf.py --url http://localhost:8080/health --n 10 --out perf_stub.json
pytest -q && test -f perf_stub.json && echo OK
```

Fixture tests check all 300 labels, plus explicit delivery and listing-photo gold cases.
The completed bad-label drill and repair are documented in `docs/build_checkpoint.md`.

## Peer review and scripted demo

Use [the review checklist](docs/peer_review_checklist.md) and
[PR template](docs/PR_TEMPLATE.md). [Review log](review_log.md) records preparation;
the assigned classmate review and PR comment are pending an accessible assigned PR URL.
A [review draft](docs/peer_review_draft.md) records the unavailable target and evidence needed.

With the virtual environment active, run `bash scripts/demo.sh`. It starts an authenticated
stub API, checks health, sends a grounded stock message, and stops its own server.
Leave port 8080 free, or run `DEMO_PORT=8081 bash scripts/demo.sh` to use another port.
This port override applies to the demo only; the integration test still expects 8080.

## Project path

- [x] AfyaPlus Module 4 Capstone (recommended): local API and health-operations teaching demo.
- [ ] Domain / field alternative.

## Week reuse (open these)

[Weeks 1–10 source audit](docs/week_reuse.md) lists inspected course artifacts and reuse limits.

- Weeks 1–5: structured JSON, grounded fallback, cost tracking, JSONL preparation, routing.
- Week 6: `services/triage/app.py`, `agents/tools/mcp_stub.py`, `agents/tools/logistics.py`.
- Week 7: `docs/cost_analysis.md`, teaching assumptions without copied historical prices.
- Week 8: `services/triage/prompts/pin.json` and the versioned prompt file.
- Week 9: `services/triage/redact.py`, `tests/test_security_smoke.py`.
- Week 10: optional catalog lane inspected and deferred; no implemented image analysis claimed.

## Dataset

`fixtures/triage_messages_sample.jsonl`: 300 synthetic routing rows, within the
200–500 target. `fixtures/clinics.json`: separate synthetic clinic-stock records.
No production scrape, live patient data, or mixed clinical/catalog PII.

## Saved testing and demo evidence

- [Unit/security output](docs/evidence/pytest.txt): **313 passed, 1 deselected**.
- [Evaluation output](docs/evidence/eval.txt): **3/3 = 1.00**.
- [Actual demo transcript](docs/evidence/demo_transcript.txt): authenticated stub flow on port 8081.
- CI workflow is published to GitHub; check the badge above for current hosted status.
- [Presentation timing and rehearsal](docs/presentation_runbook.md): 7-minute talk, 3-minute demo, 3-minute questions.

## Fallbacks declared

- [x] No live model key: deterministic routing and stub response generation.
- [x] No Docker required: local Uvicorn plus pytest/httpx.
- [x] No cloud deployment executed: documented future steps only.
- [ ] Solo reviewer: not established; assigned classmate review remains pending.

## Submission checklist

- [x] Proposal, skill matrix and map validated locally.
- [x] Five filled docs linked.
- [x] Slides PDF and one-command demo with saved transcript.
- [ ] Completed classmate peer review and posted comment.
- [x] Feature-branch commits and GitHub repository published.
- [ ] Confirm passing hosted CI.
- [ ] Portal upload and Week 12 live presentation.

See [the complete packet audit](docs/submission_audit.md) for remaining requirements.

## Repository history

Published repository: https://github.com/Abdalla-Wasaa/Week-11-Capstone-Project.
The initial configuration and complete implementation were committed on
`feature/capstone-setup`, then fast-forwarded to `main` for the first publication.
Both branches are preserved remotely. This bootstrap publication does not constitute
classmate review or establish branch-protection rules. Future changes should use
feature branches and checklist review before merging.
