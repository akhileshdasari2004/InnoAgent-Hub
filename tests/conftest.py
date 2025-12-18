"""
Shared pytest fixtures for InnoAgent-Hub tests.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def _set_test_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Provide safe default environment variables for tests.
    """
    monkeypatch.setenv("MODEL_API_KEY", "test-key")
    monkeypatch.setenv("GITHUB_PERSONAL_ACCESS_TOKEN", "test-gh")
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-firecrawl")


@pytest.fixture
def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


