"""Local retrieval over synthetic clinic records; no model inference."""
import json
import re
from pathlib import Path

DEFAULT_SOURCE = Path(__file__).resolve().parents[2] / "fixtures" / "clinics.json"


def retrieve(query: str, *, source: Path = DEFAULT_SOURCE) -> list[dict]:
    """Return records sharing query tokens, with a source and record ID."""
    tokens = set(re.findall(r"[a-z0-9]+", query.lower()))
    if not tokens:
        return []
    clinics = json.loads(source.read_text())["clinics"]
    matches = []
    for clinic in clinics:
        searchable = " ".join([clinic["name"], *clinic.get("stock", {})])
        record_tokens = set(re.findall(r"[a-z0-9]+", searchable.lower()))
        score = len(tokens & record_tokens)
        if score:
            matches.append({"record": clinic, "source": str(source), "record_id": clinic["id"], "score": score})
    return sorted(matches, key=lambda match: match["score"], reverse=True)


def grounded_answer(query: str) -> dict:
    """Build a deterministic answer exclusively from retrieved demo records."""
    matches = retrieve(query)
    if not matches:
        return {"answer": "No matching demo clinic record found.", "sources": []}
    match = matches[0]
    record = match["record"]
    stock = ", ".join(f"{item}: {units}" for item, units in record.get("stock", {}).items())
    return {
        "answer": f"{record['name']} synthetic stock: {stock}.",
        "sources": [{"file": match["source"], "record_id": match["record_id"]}],
    }
