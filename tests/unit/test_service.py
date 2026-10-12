from services.triage.app import handle_message


def test_service_runs_in_stub_mode():
    out = handle_message({"text": "hello"}, stub=True)
    assert out["status"] == "ok"
    assert out["tool"] == "triage"
    assert out["model_id"] == "stub-local"


def test_service_redacts_and_routes_in_stub_mode():
    out = handle_message({"text": "track delivery for user@example.com"}, stub=True)
    assert out["tool"] == "logistics_lookup"
    assert out["text"] == "track delivery for [REDACTED]"


def test_service_grounded_lookup_and_mcp_stub():
    out = handle_message({"text": "track delivery of ors sachets"}, stub=True)
    assert "ors_sachets: 25" in out["answer"]
    assert out["sources"][0]["record_id"] == "demo-1"
    assert out["tool_result"] == {"item": "ors_sachets", "stock": [{"clinic": "demo-1", "units": 25}]}
