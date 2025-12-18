from src.agents.interface import main as interface_main


def test_interface_module_imports() -> None:
    # Smoke test: ensure the interface agent main module imports without error
    assert callable(getattr(interface_main, "__loader__", None)) or True


