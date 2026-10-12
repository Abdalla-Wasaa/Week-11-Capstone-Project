# Presentation outline (10 slides for Week 12 Monday)

## 1. Problem and user

- AfyaPlus Module 4 Capstone: integrated health operations demo.
- Clinic operations teams need traceable lookup and structured requests.
- Teaching scope: synthetic routing and clinic stock, not patient diagnosis.

## 2. Path chosen and why

- FastAPI API path with deterministic service orchestration.
- Offline stub mode makes the minimum product reproducible without paid keys.
- One request combines routing, grounded lookup, and stock-tool dispatch.

## 3. Architecture diagram with module boundaries

- Client -> FastAPI -> optional API key -> handle_message -> email redaction.
- Redacted text -> config router and local clinic retrieval -> JSON with citations.
- Logistics route -> MCP tools/call stub -> check_stock -> synthetic clinic data.
- See the Mermaid diagram in docs/architecture.md; no network MCP transport.

## 4. Skill coverage (which skills, where in repo)

- Week 6 API: services/triage/app.py; Week 7 tools: agents/tools/mcp_stub.py.
- Week 8 pin: services/triage/prompts/pin.json; Week 9 security: smoke suite.
- Week 11 tests/eval: tests/unit and evals/golden.jsonl; docs pack linked in README.
- Multimodal image analysis is optional and deferred.

## 5. Live demo (or 60-second recording backup)

- Run bash scripts/demo.sh from the active virtual environment.
- Show healthy API, then authenticated ORS delivery request.
- Point to logistics_lookup, synthetic stock 25, citation, and tool_result.
- Script stops its server on exit. Recording backup is planned, not recorded.

## 6. Testing evidence (pytest line, security smoke, eval score)

- Default pytest: 313 passed, 1 integration test deselected.
- Security smoke: 4 passed; live HTTP integration: 1 passed; Ruff passes.
- Golden set: 3/3 = 1.00; fixture diagnosis: all 300 rows agree.
- perf_stub.json: 10 successful requests, measured p95 0.0209 seconds.
- Three gold cases are a smoke metric, not a production-quality claim.

## 7. Security and compliance choices

- Synthetic data only; incoming messages are not persisted.
- Emails redacted before routing/retrieval; other PII redaction is not implemented.
- TRIAGE_API_KEY enforces X-Api-Key when configured; health remains public.
- Security smoke checks tracked .env, live-looking keys, redaction, and auth.
- No production compliance certification is claimed.

## 8. Cost table with assumptions

- Stub tests: zero paid calls, $0 model/API charges.
- Current demo: about 10 local requests, $0 model/API charges.
- Future live option: about 10 calls within a ~$1 planning allowance.
- Provider rates unverified; no live inference or billing cap implemented.
- Local compute costs excluded; see docs/cost_analysis.md.

## 9. What works vs deferred

- Works: API, routing, synthetic grounded answer, local MCP stock stub.
- Works: 300-row fixture, diagnosis drill, CI steps, docs and demo script.
- Deferred: live model, network MCP server, cloud deployment, image analysis.
- Grounding currently uses clinic stock records, not clinical guidance documents.

## 10. Process (PR, peer review outcome, next steps)

- Deliberately mislabeled T-002; tests failed; correct label restored.
- Reviewer: Abdalla Wasaa (Abdalla-Wasaa); classmate PR URL pending.
- No classmate PR comment or completed review is claimed.
- Next: complete assigned peer review, capture backup recording, rehearse deck.
- Keep main changes subject to checklist review before merge.
