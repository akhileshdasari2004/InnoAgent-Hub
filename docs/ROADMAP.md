## InnoAgent-Hub Roadmap

### Near-Term

- **Community Agent for Crowdsourced Prompts**

  - Implement `src/agents/community/` with:
    - `main.py` polling GitHub issues or discussions.
    - `community_tools.py` for fetching and parsing community input.
  - Wire into `config/registry.toml` and `backend/orchestrator/application.yaml`.

- **Open Innovation Demo Flows**
  - Curate example sessions in `demos/open-innovation-session.json`.
  - Provide scripts and docs for running collaborative workflows.

### Medium-Term

- **Real-time Collaboration**

  - Integrate Socket.io or similar for live session updates.
  - Allow multiple users to observe and influence the same agent graph.

- **Voting & Feedback Mechanisms**

  - Add simple voting APIs and UI elements for ranking ideas.
  - Aggregate feedback into agent prompts and prioritization logic.

- **Enhanced Visualization Dashboards**
  - Build Studio/Next.js dashboards for:
    - Agent activity timelines
    - Idea evolution graphs
    - Community engagement metrics

### Long-Term

- **Pluggable Community Sources**

  - Support additional platforms (Discord, forums, surveys) as input streams.

- **Advanced Analytics**
  - Track idea lifecycle from suggestion to implementation.
  - Provide insight into which agents and tools contribute most value.
