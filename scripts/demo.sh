#!/usr/bin/env bash
# Run from any directory with the project virtual environment active.
set -euo pipefail
cd "$(dirname "$0")/.."
demo_port="${DEMO_PORT:-8080}"
export TRIAGE_API_KEY="${TRIAGE_API_KEY:-demo}"

# 1. Start the local authenticated stub service.
python -m uvicorn services.triage.app:app --host 127.0.0.1 --port "$demo_port" &
demo_server_pid=$!
trap 'kill "$demo_server_pid" 2>/dev/null || true; wait "$demo_server_pid" 2>/dev/null || true' EXIT
sleep 0.3

# 2. Confirm health after startup; fail if our server could not start.
for attempt in {1..50}; do
    if ! kill -0 "$demo_server_pid" 2>/dev/null; then
        echo "Demo server exited; check whether port $demo_port is already occupied." >&2
        exit 1
    fi
    if curl -fsS "http://127.0.0.1:$demo_port/health"; then
        kill -0 "$demo_server_pid"
        break
    fi
    if [ "$attempt" -eq 50 ]; then
        echo "Demo server did not become healthy." >&2
        exit 1
    fi
    sleep 0.1
done
printf '\n'

# 3. Send a grounded logistics message, demonstrating both lookup and stock tool.
curl -fsS "http://127.0.0.1:$demo_port/triage" \
    -H "X-Api-Key: $TRIAGE_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{"text":"track delivery of ors sachets","item":"ors_sachets"}'
printf '\n'
