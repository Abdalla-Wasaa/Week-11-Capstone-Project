# Skill coverage matrix

| Skill | Week resource to open | My module / file | Required / Optional |
| --- | --- | --- | --- |
| API or agent path | Week 6 triage API lab | services/triage | Required |
| Cost / MCP tools | Week 6 stock MCP / Week 7 cost modelling | agents/tools/mcp_stub.py and agents/tools/logistics.py | Required |
| Pin / versioning | Week 8 pin.json | services/triage/prompts/pin.json | Required |
| Security hygiene | Week 9 security smoke | tests/test_security_smoke.py | Required |
| Eval / test | Week 11 Tuesday pyramid + golden set | tests/unit/, evals/golden.jsonl | Required |
| Docs | Prior READMEs + Week 11 docs | docs/ | Required |
| Optional multimodal | Week 10 mismatch detection lane | Deferred: services/catalog/mismatch.py not implemented | Optional |

## Weeks 1–10 coverage

The inspected source paths, target files, and reuse limits for every programme week
are recorded in [week_reuse.md](docs/week_reuse.md). Weeks 1–5 contribute structured
output, grounded fallback, cost/data preparation and routing patterns; Weeks 6–9
map to the required API/tool/pin/security capabilities. Week 10 is optional and deferred.
The required cost/tool row uses the Week 6 stock-server implementation and Week 7
cost-model exercises; it does not claim a Week 7 stock-server file was inspected.
