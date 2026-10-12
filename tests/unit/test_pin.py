import json
from pathlib import Path


def test_pin_has_model_and_version():
    pin = json.loads(Path("services/triage/prompts/pin.json").read_text())
    assert pin.get("model_id")
    assert pin.get("prompt_version")
    assert pin["prompt_version"] == pin["version"]
