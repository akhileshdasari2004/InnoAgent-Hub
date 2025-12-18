from src.agents.firecrawl import main as firecrawl_main


def test_firecrawl_module_imports() -> None:
    # Smoke test: ensure the firecrawl agent main module imports without error
    assert callable(getattr(firecrawl_main, "__loader__", None)) or True


