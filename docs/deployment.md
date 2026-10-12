# Deployment

## Run locally

Run these commands from `module4-capstone` with the virtual environment active:

```bash
pip install -r requirements.txt
pytest -q
uvicorn services.triage.app:app --host 127.0.0.1 --port 8080
```

Leave the server running. Use a second terminal for the user-guide examples,
integration test, and performance script. Running from the project directory is
required because the router loads `config.json` relative to the working directory.

## Env vars

- `TRIAGE_API_KEY`: optional teaching auth key. When set on the server, `/triage` requires a matching `X-Api-Key` header; missing or incorrect keys return 401.
- `SERVICE_UP=1`: enables the integration health test; it does not start the server.
- `OPENAI_API_KEY`: not consumed by the current implementation. Setting it does not enable live inference.

For an authenticated local demo, set a teaching key before starting the server:

```bash
export TRIAGE_API_KEY=local-demo-key
uvicorn services.triage.app:app --host 127.0.0.1 --port 8080
```

Keep real secrets out of tracked files. The local stub permits unauthenticated
messages when `TRIAGE_API_KEY` is unset; `/health` is always unauthenticated.

## Health

```bash
curl -f http://localhost:8080/health
SERVICE_UP=1 pytest -q -m integration
python scripts/measure_perf.py --url http://localhost:8080/health --n 10 --out perf_stub.json
```

Health returns HTTP 200 with `{"status":"ok"}`. The measurement script writes
`perf_stub.json` only after successful requests; its caption is
"laptop teaching stub; not a production SLA".

## Fallback

Cloud and Docker deployment: **not executed live**. The supported fallback is the
local Uvicorn workflow above; it needs no cloud credentials or model key.
If port 8080 refuses connections, start the server and check its startup logs.
If it is occupied, identify the existing service before choosing another port;
the current integration test expects 8080.

A future cloud deployment would install the dependencies, configure the API key
through a secret store, start Uvicorn behind HTTPS, and verify health and authenticated
message requests. Those steps are a plan, not deployment evidence. Stop the local
server with Ctrl+C after the demo.
