"""
Utility functions for the Community Agent.

These are intentionally lightweight and designed for hackathon/demo usage.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class CommunityIdea:
    title: str
    url: str
    summary: str


def parse_github_issues(issues: List[dict]) -> List[CommunityIdea]:
    """
    Convert a list of GitHub issue dicts into CommunityIdea objects.
    """
    ideas: List[CommunityIdea] = []
    for issue in issues:
        ideas.append(
            CommunityIdea(
                title=issue.get("title", "Untitled"),
                url=issue.get("html_url", ""),
                summary=(issue.get("body") or "").strip()[:280],
            )
        )
    return ideas


