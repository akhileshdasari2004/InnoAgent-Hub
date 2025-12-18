## InnoAgent-Hub: A Multi-Agent Platform for Open Innovation

### Overview

InnoAgent-Hub is a multi-agent AI platform built on **Coral Protocol** that orchestrates several specialized agents to support open innovation workflows. It brings together interface, GitHub analysis, web research, and community-driven collaboration into a single, extensible hub.

The goal is to make it easy for teams at hackathons and beyond to prototype collaborative AI workflows, crowdsource ideas, and visualize complex agent interactions in real time.

### Features

- **Multi-agent orchestration**: Coordinate Interface, GitHub, Firecrawl, and Community agents via Coral Server.
- **Extensible architecture**: Add new agents and tools with minimal wiring.
- **Open Innovation support**: Demo flows for crowdsourced prompts and feedback.
- **Visual Studio UI**: Coral Studio integration for session and agent graph visualization.
- **Config-driven**: Centralized configuration and environment management.

### Quick Start

1. **Check dependencies**

```bash
./scripts/check-dependencies.sh
```

2. **Start Coral Server**

```bash
./scripts/start-server.sh
```

3. **Start Coral Studio**

```bash
cd frontend/studio
./start-studio.sh
```

4. **Open the UI**

Visit `http://127.0.0.1:5173` in your browser and connect to the Coral Server at `localhost:5555`.

### Architecture

The high-level system architecture is shown below:

![InnoAgent-Hub Architecture](../images/innoagent-hub-architecture.png)

- **Frontend User Interface** (Vercel + React/Next.js) for idea submission, dashboards, and thread viewing.
- **Backend & Orchestration** (Coral Server + Java) for agent lifecycle management, routing, and session control.
- **Multi-Agent System** (Interface, GitHub, Firecrawl, Community agents) for research, analysis, feedback and ranking.
- **Data & State** layer for session memory, idea history, and feedback logs.
- **External AI & Data Sources** (OpenAI, GitHub API, open datasets) powering the agent tools.

See `ARCHITECTURE.md` in this `docs/` directory for a full architectural overview, including Mermaid diagrams, layers, and extension points.

### License

This project is licensed under the **MIT License**. See the `LICENSE` file in the repository root for details.
