# Presentation runbook

## Seven-minute talk

- Slides 1–2: problem, chosen API path and teaching scope (1 minute).
- Slides 3–4: architecture and week reuse (1.5 minutes).
- Slide 5: explain the upcoming demonstration (0.5 minute).
- Slides 6–8: tests, security boundaries and cost assumptions (2 minutes).
- Slides 9–10: works/deferred, diagnosis, peer-review status and next steps (2 minutes).

## Three-minute live demo

Activate the virtual environment and run from module4-capstone. Leave port 8080
free, or select a free demo port explicitly:

```bash
DEMO_PORT=8081 bash scripts/demo.sh
```

Show health, authenticated response, logistics route, synthetic stock 25 and its
source citation. The script stops its own server. Explain that no paid model or
network MCP server participates. If local tooling fails, show the saved actual
transcript at docs/evidence/demo_transcript.txt; no backup recording is claimed.

## Three-minute questions

Be ready to explain why tests use stubs, what the pin identifies, how the citation
is derived, which PII is redacted, and why the three-case eval is only a smoke check.
State that image analysis, cloud deployment and live inference are deferred.
Describe peer review as pending until the assigned accessible PR has been reviewed.
