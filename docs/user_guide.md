# User guide

## Run

Follow [Deployment](deployment.md) to install dependencies and start the API from
`module4-capstone`. Keep the server running in one terminal and send requests from another.

For a server started without `TRIAGE_API_KEY`:

```bash
curl -f http://localhost:8080/triage \
  -H 'Content-Type: application/json' \
  -d '{"text":"track delivery of ors sachets","item":"ors_sachets"}'
```

When the server has `TRIAGE_API_KEY=local-demo-key`, include
`-H 'X-Api-Key: local-demo-key'` in that request. Missing or incorrect keys return 401;
a missing or invalid `text` field returns 422.

A successful response has `status: ok`, `model_id: stub-local`, a routing `tool`,
redacted `text`, an `answer`, and `sources`. This example selects `logistics_lookup`,
reports synthetic ORS stock of 25 with a source citation, and includes `tool_result`.
The default `item` is `ors_sachets`. Item selection affects the stock tool;
retrieval independently matches the message text.

## Health check

```bash
curl -f http://localhost:8080/health
```

Expected response: `{"status":"ok"}`. Connection refused means the server is not
listening at that address; inspect the server terminal and restart it if needed.

## Fallback path

All HTTP message requests currently use stub mode, whether or not a model key is set.
The service redacts emails, routes the request, performs local retrieval, and calls
the local stock-tool stub for logistics intents. An unmatched retrieval query returns
"No matching demo clinic record found." with no sources. Direct calls to
`handle_message(..., stub=False)` raise `NotImplementedError`.

This demo does not diagnose patients, track real shipments, or analyze listing images.
To check retrieval without starting the server:

```bash
python -m services.triage.rag_smoke
```

## Fixture location

`fixtures/triage_messages_sample.jsonl` contains 300 synthetic routing rows.
`fixtures/clinics.json` supplies synthetic stock records. JSONL contains one JSON
record per line and no comment lines. Generate, diagnose, and evaluate offline:

```bash
python scripts/make_fixture.py --rows 300 --out fixtures/triage_messages_sample.jsonl
python scripts/diagnose_fixture.py fixtures/triage_messages_sample.jsonl
python evals/run_eval.py evals/golden.jsonl
pytest -q
```

Diagnosis should report all rows agree with the router; the golden set currently
scores `3/3 = 1.00`. Build evidence and the repaired-label incident are in
[Build checkpoint](build_checkpoint.md).
