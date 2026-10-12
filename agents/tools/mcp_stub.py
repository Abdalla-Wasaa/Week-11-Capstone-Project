"""In-process MCP tools/call stub. No live MCP server or network transport."""
import json

from agents.tools.logistics import check_stock


def dispatch(request: dict) -> dict:
    """Handle the stock tool using the MCP JSON-RPC request/result shape."""
    params = request.get("params", {})
    if request.get("jsonrpc") != "2.0" or request.get("method") != "tools/call" or params.get("name") != "check_stock":
        raise ValueError("Unsupported stub MCP request")
    result = check_stock(params["arguments"]["item"])
    return {
        "jsonrpc": "2.0", "id": request["id"],
        "result": {"content": [{"type": "text", "text": json.dumps(result)}], "isError": False},
    }


def call_stock(item: str) -> dict:
    response = dispatch({
        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": "check_stock", "arguments": {"item": item}},
    })
    return json.loads(response["result"]["content"][0]["text"])
