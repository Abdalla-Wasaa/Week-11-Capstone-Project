"""Week 8 stock lookup adapted as a local synthetic-data tool stub."""
import json
from pathlib import Path

_FIXTURE = Path(__file__).resolve().parents[2] / "fixtures" / "clinics.json"


def check_stock(item: str) -> dict:
    """Return synthetic clinic stock without network or model calls."""
    clinics = json.loads(_FIXTURE.read_text())["clinics"]
    return {
        "item": item,
        "stock": [
            {"clinic": clinic["id"], "units": clinic["stock"].get(item, 0)}
            for clinic in clinics
        ],
    }
