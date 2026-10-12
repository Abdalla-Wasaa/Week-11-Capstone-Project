"""Run with python -m services.triage.rag_smoke; no API or server required."""
from services.triage.rag import DEFAULT_SOURCE, grounded_answer, retrieve


def main() -> int:
    matches = retrieve("ors sachets")
    if not matches:
        raise RuntimeError("RAG smoke failed: no ORS record retrieved")
    match = matches[0]
    if match["record"]["stock"].get("ors_sachets") != 25:
        raise RuntimeError("RAG smoke failed: unexpected demo stock")
    if match["record_id"] != "demo-1" or match["source"] != str(DEFAULT_SOURCE):
        raise RuntimeError("RAG smoke failed: missing or incorrect source")
    if retrieve("unmatchedquery"):
        raise RuntimeError("RAG smoke failed: unmatched query returned records")
    answer = grounded_answer("ors sachets")
    if "25" not in answer["answer"] or not answer["sources"]:
        raise RuntimeError("RAG smoke failed: answer is not grounded")
    print(answer["answer"])
    print("RAG smoke passed: demo clinic retrieved, stock=25, source verified, unmatched query empty.")
    print(f"Source: {match['source']} (record {match['record_id']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
