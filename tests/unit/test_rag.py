import json

from services.triage.rag import retrieve


def test_retrieval_uses_source_records(tmp_path):
    source = tmp_path / "clinics.json"
    source.write_text(json.dumps({"clinics": [
        {"id": "a", "name": "Alpha", "stock": {"ors_sachets": 7}},
        {"id": "b", "name": "Beta", "stock": {"bandages": 12}},
    ]}))
    matches = retrieve("ORS sachets", source=source)
    assert len(matches) == 1
    assert matches[0]["record"]["stock"]["ors_sachets"] == 7
    assert matches[0]["record_id"] == "a"
    assert matches[0]["source"] == str(source)
    assert retrieve("unmatchedquery", source=source) == []
    assert retrieve("", source=source) == []
