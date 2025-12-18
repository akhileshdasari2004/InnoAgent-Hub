## Contributing to InnoAgent-Hub

### Adding a New Agent

- Create a new directory under `src/agents/<agent_name>/`.
- Add `main.py`, any helper modules, and a `run_agent.sh` script.
- Ensure there is an `__init__.py` so it is importable as a package.
- Register the agent in:
  - `backend/orchestrator/application.yaml` (runtime + options)
  - `config/registry.toml` (for Studio/registry integration)

### Code Style

- **Python**: Use `black` and `flake8`. Aim for clear, documented functions and small modules.
- **TypeScript/JavaScript**: Follow the existing ESLint and Prettier configuration.
- **YAML/JSON**: Keep configuration minimal, documented, and validated where possible.

### Testing

- Add unit tests under `tests/`:
  - `test_<agent>.py` for each agent.
  - `test_collaboration.py` for end-to-end or integration flows.
- Use `pytest` for running tests:

```bash
pytest
```

### Pull Request Process

- Fork or branch from `revamp`.
- Keep commits small and focused (one logical change per commit).
- Ensure `pytest`, linters, and CI all pass before requesting review.
- Document new features or breaking changes in `docs/` and update demos if relevant.

### License and Ownership

InnoAgent-Hub is released under the MIT License; see the `LICENSE` file at the project root.
