#!/bin/bash
set -euo pipefail

COMMAND=${1:-local}

case "$COMMAND" in
  local)
    echo "Starting local stack with docker-compose..."
    docker compose -f config/docker-compose.yml up --build
    ;;
  vercel)
    echo "For Vercel, configure the InnoAgent-Hub Next.js app in the InnoAgent-Hub/ directory."
    echo "Set environment variables (OPENAI_API_KEY, GITHUB_PERSONAL_ACCESS_TOKEN, FIRECRAWL_API_KEY) in Vercel."
    ;;
  railway)
    echo "For Railway, deploy the backend/orchestrator/coral-server and agents as services."
    echo "Use config/docker-compose.yml as a reference for environment and networking."
    ;;
  *)
    echo "Usage: scripts/deploy.sh [local|vercel|railway]"
    exit 1
    ;;
esac


