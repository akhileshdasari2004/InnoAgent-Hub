## InnoAgent-Hub Demos

### Open Innovation Session (`open-innovation-session.json`)

This JSON file describes a sample multi-agent graph for an open innovation workflow:

- The **Interface Agent** collects an idea from the user.
- The **Firecrawl Agent** researches related projects and articles.
- The **GitHub Agent** analyzes similar repositories and issues.
- The **Community Agent** gathers feedback from community sources.
- The **Interface Agent** synthesizes the results back to the user.

### Crowdsource Demo (`crowdsource-demo.py`)

This script simulates a community-driven flow:

- Fetches crowdsourced prompts from a mock GitHub repository.
- Sends them through the agent graph described in the JSON session.
- Logs combined outputs for inspection.

You can use these demos as templates to build your own open innovation workflows.
