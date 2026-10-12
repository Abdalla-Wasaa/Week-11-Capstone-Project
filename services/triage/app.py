"""Capstone base API, adapted from the Week 6 FastAPI hello service."""

import os
import secrets

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel

from agents.router import route
from agents.tools.mcp_stub import call_stock
from services.triage.rag import grounded_answer
from services.triage.redact import redact

app = FastAPI(title="AfyaPlus Capstone")


@app.get("/health")
def health() -> dict[str, str]:
    """Confirm that the API is running."""
    return {"status": "ok"}


def handle_message(payload: dict, *, stub: bool = False) -> dict:
    if stub:
        text = redact(payload["text"])
        result = {"status": "ok", "text": text, "tool": route(text), "model_id": "stub-local"}
        result.update(grounded_answer(text))
        if result["tool"] == "logistics_lookup":
            result["tool_result"] = call_stock(payload.get("item", "ors_sachets"))
        return result

    raise NotImplementedError("Live message handling is not implemented")


class Message(BaseModel):
    text: str
    item: str = "ors_sachets"


def require_api_key(x_api_key: str | None = Header(default=None)) -> None:
    """Enforce the teaching API key when TRIAGE_API_KEY is configured."""
    expected = os.getenv("TRIAGE_API_KEY")
    if expected and (x_api_key is None or not secrets.compare_digest(x_api_key.encode(), expected.encode())):
        raise HTTPException(status_code=401, detail="Invalid API key")


@app.post("/triage", dependencies=[Depends(require_api_key)])
def triage(message: Message) -> dict:
    return handle_message(message.model_dump(), stub=True)
