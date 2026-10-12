## Summary

Describe the concrete change and link the relevant [proposal](../proposal.md)
and [skill matrix](../skill_matrix.md) rows. Include behavior before and after.

## Tests

- [ ] `pytest -q` (paste actual result)
- [ ] Optional live integration: `SERVICE_UP=1 pytest -q -m integration`
- [ ] `python evals/run_eval.py evals/golden.jsonl` (paste score)

## Checklist

Tick only items verified against this PR; record follow-ups for unchecked items.

- [ ] No secrets or .env in diff
- [ ] proposal.md path choice explicit
- [ ] skill_matrix.md maps required skills to weeks
- [ ] integration_map.json paths exist on disk (deferred paths explicitly called out)
- [ ] pytest -q unit layer attached or CI green
- [ ] Eval score printed
- [ ] Fixture row count in hundreds; no production scrape claim
- [ ] README links all five docs

## Comment format for reviewers

- Checklist: item ticked or not, one line each, with evidence.
- Block: must fix before merge; identify file and required change.
- Nit: optional polish.
- Ask: a question, not a demand.
