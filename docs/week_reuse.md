# Weeks 1–10 reuse evidence

Source artifacts below were inspected during the packet audit on 2026-10-12.
They live in the surrounding course workspace, not in the submission repository.
Only the listed capstone targets are shipped; these references document design reuse,
not claims that every earlier feature was copied or is running in this capstone.

| Week | Inspected course artifact | Capstone target | Reuse and limits |
| --- | --- | --- | --- |
| 1 | venv/wk1/thur/lab13_structured.py | services/triage/app.py | Structured JSON/input-validation pattern; no patient example copied |
| 2 | venv/wk2/lab11_rag.py | services/triage/rag.py | Context-only answers and unmatched fallback; local keyword retrieval replaces paid embeddings |
| 3 | venv/wk3/tuesday/cost_tracker.py | docs/cost_analysis.md | Separate counts, cost and assumptions; current stub makes no paid calls |
| 4 | venv/wk4/afyaplus-finetune/venv/data_prep.py | scripts/make_fixture.py | Offline JSONL data preparation; no model fine-tuning reused |
| 5 | venv/wk5/wk5_capstone/router.py | agents/router.py | Explicit dispatch boundaries; text routing replaces uploaded multimodal files |
| 6 | venv/wk6_capstone_project/README.md and mcp_server/server.py | services/triage/app.py and agents/tools/mcp_stub.py | Health/auth service and stock-tool interface adapted into a local stub |
| 7 | venv/wk7/monday/cost_model.py | docs/cost_analysis.md | Teaching cost assumptions; historical provider price constants were not copied |
| 8 | Week_8_Capstone_Project/prompts/pin.json | services/triage/prompts/pin.json | Prompt file/version/hash retained; explicit stub-local model field added |
| 9 | Week_9_capstone_project/redact_then_hash.py | services/triage/redact.py and tests/test_security_smoke.py | Email-redaction pattern and real smoke checks; full earlier audit/RBAC stack not reused |
| 10 | Week_10_Capstone_Project/check_mismatch.py | docs/build_checkpoint.md | Optional catalog gold-check lane inspected; image analysis remains deferred |

The course uses several MCP examples across weeks. The actual inspected stock-server
source is the Week 6 capstone; Week 7 evidence here concerns cost modelling.
