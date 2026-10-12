# Capstone packet audit — 2026-10-12

This is a local audit against the supplied capstone packet, not a claim of completed
peer review, hosted CI, upload, or live presentation.

| Deliverable | Status | Evidence / remaining action |
| --- | --- | --- |
| Proposal with explicit path, scope, scale and milestones | Ready | proposal.md; proposal checker passes |
| Skill matrix and Weeks 1–10 references | Ready with declared limits | skill_matrix.md and docs/week_reuse.md; design references, not ten live subsystems |
| Integration map with existing paths | Ready | Map checker passes; optional catalog points to its documented deferral |
| Unit-default pytest and markers | Ready | pytest.ini |
| Router, gold fixture, real service stub and pin tests | Ready | docs/evidence/pytest.txt: 313 passed, 1 deselected |
| Security smoke and real email redaction | Ready | tests/test_security_smoke.py; configured-key auth covered |
| Measured performance artifact | Ready | perf_stub.json: 10 successful HTTP calls, teaching caption |
| CI workflow present and green | Partially ready | Workflow published and local gates pass; hosted CI confirmation pending |
| Broken-fixture diagnosis | Ready | Three-line incident note in docs/build_checkpoint.md; fixture tests retained |
| One-command end-to-end flow | Ready | bash scripts/demo.sh; optional DEMO_PORT override |
| Transcript or recording | Ready | docs/evidence/demo_transcript.txt captures actual authenticated HTTP demo |
| Minimum product: auth, RAG, MCP stub, pin, eval, fixture | Ready in declared stub scope | Local clinic facts with citations, in-process tools/call stub; no clinical document corpus or network MCP server |
| Five linked docs and cost/runbook detail | Ready | README links and doc checker pass |
| Synthetic fixture scale and no-scrape rule | Ready | 300 JSONL rows; fixtures/README.md |
| Visible feature-branch history | Ready | Configuration and implementation committed on feature/capstone-setup; branch pushed and main fast-forwarded for initial publication |
| Review checklist | Ready | Eight items; supplied checker passes |
| Completed peer review and posted PR comment | Incomplete | Supplied placeholder PR unavailable; actual assigned URL required |
| Optional sprint board | Optional, absent | Not required for submission |
| 8–10 slide PDF and filled outline | Ready as draft | docs/presentation.pdf has ten slides; outline filled |
| 7-minute talk, 3-minute demo, 3-minute questions | Planned, not delivered | docs/presentation_runbook.md |
| Single GitHub repository and visible eval in CI | Incomplete | Published to Abdalla-Wasaa/Week-11-Capstone-Project; hosted CI confirmation pending |
| Programme portal submission and Week 12 presentation | Pending user action | Deadline follows mentor instructions; no upload or in-class delivery claimed |

## Finish before submission

1. Inspect the diff and confirm the intended submission files. Keep .env, virtual
   environments, caches, logs and the starter-pack archive out of the submission.
2. Feature commits and the initial publication are complete; keep future changes on reviewed feature branches.
3. Both main and feature/capstone-setup are published. Use PRs for subsequent changes; no completed classmate review is claimed.
4. Obtain the actual assigned classmate PR URL. Abdalla Wasaa is the reviewer;
   posting authorization is already recorded. Update the log only after review.
5. Confirm GitHub CI passes and link the actual run in README; local green results
   do not establish hosted CI status.
6. Rehearse the ten slides, upload the packet including PDF and evidence, and
   deliver the live presentation. Keep the current deferrals visible.

The solo-cohort self-review fallback is available only if that is the actual cohort
arrangement; it is not used here to replace the pending assigned classmate review.
