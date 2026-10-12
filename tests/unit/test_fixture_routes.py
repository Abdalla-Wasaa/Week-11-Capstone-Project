import json
from pathlib import Path

import pytest

from agents.router import route

ROWS = [json.loads(line) for line in Path("fixtures/triage_messages_sample.jsonl").read_text().splitlines()]


@pytest.mark.parametrize("row", ROWS, ids=[row["id"] for row in ROWS])
def test_fixture_route(row):
    assert route(row["text"]) == row["label"], f"{row['id']}: incorrect label for {row['text']!r}"


@pytest.mark.parametrize("record_id, expected", [("T-002", "logistics_lookup"), ("T-003", "catalog_mismatch")])
def test_gold_fixture_routes(record_id, expected):
    row = next(row for row in ROWS if row["id"] == record_id)
    assert row["label"] == expected
    assert route(row["text"]) == expected
