"""
Simple demo script showing how a community-driven prompt flow could work.

This does not start Coral Server itself; instead it demonstrates the kind
of data that the Community Agent might fetch and pass into a session.
"""

from __future__ import annotations

import json
from pathlib import Path


DEMO_ROOT = Path(__file__).resolve().parent
SESSION_FILE = DEMO_ROOT / "open-innovation-session.json"


def load_session() -> dict:
    with SESSION_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    session = load_session()

    example_prompts = [
        {
            "title": "AI-assisted bug triage",
            "description": "Use multi-agent workflows to cluster and prioritize GitHub issues.",
        },
        {
            "title": "Open innovation idea board",
            "description": "Collect ideas from GitHub discussions and Firecrawl web research.",
        },
    ]

    print("Loaded session graph with agents:", ", ".join(session["agentGraph"]["agents"].keys()))
    print("Example community prompts:")
    for prompt in example_prompts:
        print(f"- {prompt['title']}: {prompt['description']}")


if __name__ == "__main__":
    main()


