# Build checkpoint

## Works now
- GitHub repository published with main and feature/capstone-setup history; hosted CI run 38279899422 passed all gates.
- Ten-slide `docs/presentation.pdf` and filled outline prepared; authenticated `scripts/demo.sh` verified on port 8081 because 8080 was occupied.
- `proposal.md`: AfyaPlus Module 4 Capstone, API path with integrated stub lookup and tools.
- `skill_matrix.md`: required skill paths mapped; optional multimodal lane explicitly deferred.
- Five filled documentation templates linked from README; supplied checker prints `doc links OK`.
- Security smoke present in `tests/test_security_smoke.py`: 4 passed.
- Default suite: 313 passed, 1 integration test deselected; Ruff passes.
- Live HTTP health integration: 1 passed against localhost:8080.
- Stub service connects routing, grounded synthetic clinic lookup with citations, and an in-process MCP stock-tool stub.
- Fixture generated offline: 300 valid JSONL records; diagnosis reports all routes agree.
- Golden-set evaluation: 3/3 = 1.00.
- Script-generated perf_stub.json: 10 successful health requests; caption is "laptop teaching stub; not a production SLA".

## Incident note
What broke: T-002 was temporarily mislabeled as triage instead of logistics_lookup.
How found: fixture-backed pytest assertions reported logistics_lookup != triage for T-002.
Fix: restored logistics_lookup, retained the tests, and reran diagnosis and the full suite successfully.

## Deferred
- Assigned classmate PR review/comment and completed reviewer outcome; reviewer Abdalla Wasaa (Abdalla-Wasaa), awaiting an accessible assigned PR URL; supplied CLASSMATE/REPOSITORY URL could not be resolved.
- Backup recording and Week 12 presentation delivery.
- Live cloud deployment: local runbook and future steps documented only; not executed live.
- Live LLM agent loops beyond the approximately $1 demo allowance. Current paid model spend is $0.
- Live model inference and a network MCP server; current MCP tools/call dispatch runs locally in stub mode.
- Retrieval currently uses synthetic clinic stock records, not clinical guidance or a vector database.
- Catalog mismatch handling routes the intent but does not perform image analysis.
