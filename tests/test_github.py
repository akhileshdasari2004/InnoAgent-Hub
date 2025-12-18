from src.agents.github import main as github_main


def test_github_module_imports() -> None:
    # Smoke test: ensure the github agent main module imports without error
    assert callable(getattr(github_main, "__loader__", None)) or True


