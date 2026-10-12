"""Change for your project: nothing. Adapt only if your repo layout differs."""
import re
import subprocess
from pathlib import Path

_LIVE_KEY = re.compile(r"sk-live-[A-Za-z0-9_-]{6,}")


def test_env_not_tracked():
    out = subprocess.check_output(['git', 'ls-files'], text=True)
    assert not any(Path(name).name == '.env' for name in out.splitlines())


def test_no_sample_live_key_in_repo():
    for p in Path('.').rglob('*.py'):
        if 'venv' in p.parts or 'tests' in p.parts:
            continue
        assert _LIVE_KEY.search(p.read_text()) is None, f'live-looking key in {p}'


def test_redaction_strips_email():
    from services.triage.redact import redact
    assert 'user@example.com' not in redact('contact user@example.com now')


def test_triage_requires_configured_api_key(monkeypatch):
    from fastapi.testclient import TestClient

    from services.triage.app import app

    monkeypatch.setenv("TRIAGE_API_KEY", "teaching-test-key")
    with TestClient(app) as client:
        payload = {"text": "contact user@example.com about delivery"}
        assert client.post("/triage", json=payload).status_code == 401
        assert client.post("/triage", json=payload, headers={"X-Api-Key": "wrong"}).status_code == 401
        response = client.post("/triage", json=payload, headers={"X-Api-Key": "teaching-test-key"})
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
        assert response.json()["tool"] == "logistics_lookup"
        assert "user@example.com" not in response.json()["text"]
