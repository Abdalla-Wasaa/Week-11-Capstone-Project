# Cost analysis

| Call type | Calls (n) | Unit cost | Total | Assumptions |
| --- | --- | --- | --- | --- |
| Stub tests | 0 paid calls | $0 | $0 | CI never calls a live model; local tests still execute service and tool functions |
| Thursday demo (current stub) | ~10 local requests | $0 model/API charge | $0 model/API charge | Deterministic fixture lookup and local tool dispatch; no hosted service |
| Thursday demo (future live option) | ~10 planned live calls | teaching estimate: ~$0.10/call | ~$1 budget cap | Planning allowance, not provider pricing or measured spend; live inference is not implemented |

The current implementation incurs no paid model calls. Local compute and internet
costs are excluded from this teaching estimate. Performance results measure latency,
not spending. No cloud deployment costs have been measured.

Before a live demo, choose a provider and model, verify current pricing, estimate
input/output tokens, and enforce a request/token budget within the approximately $1
allowance. If live calls cannot stay within that allowance, use the local stub.
Live agent loops remain deferred; there is no implemented billing cap today.
