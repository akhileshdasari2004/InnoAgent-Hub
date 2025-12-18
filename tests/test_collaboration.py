from pathlib import Path

import json


def test_open_innovation_session_json_valid() -> None:
    session_path = Path(__file__).resolve().parents[1] / "demos" / "open-innovation-session.json"
    data = json.loads(session_path.read_text(encoding="utf-8"))
    assert "agentGraph" in data
    assert "agents" in data["agentGraph"]


