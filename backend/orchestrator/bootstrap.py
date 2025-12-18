"""
Bootstrap script for the InnoAgent-Hub orchestrator layer.

This module is responsible for:
- Ensuring required environment variables are present
- Preparing Python paths so local agents in src/agents can be imported
- Providing a single entrypoint hook that other tooling (scripts, IDEs, tests)
  can call before interacting with Coral Server.
"""

import os
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"


def setup_environment() -> None:
    """
    Configure environment for running Coral Server with local agents.
    """
    # Ensure src is on sys.path so agents can be imported as packages
    if str(SRC_DIR) not in sys.path:
        sys.path.insert(0, str(SRC_DIR))

    # Default environment defaults can be set here if desired
    os.environ.setdefault("INNOAGENT_HUB_ENV", "development")


def bootstrap() -> None:
    """
    Public bootstrap function to be invoked by scripts/tests.
    """
    setup_environment()


if __name__ == "__main__":
    bootstrap()


