# Agno Agent with MCP Server

This project leverages the **Agno Agent framework** and an **MCP server** to provide a session-based agent capable of RAG (Retrieval-Augmented Generation).  

- **RAG setup** is configured using the steps from another repository: [chroma](https://github.com/shungyan/chroma).  
- The agent and session manager are fully **dockerized** for easy deployment.  

---

## Prerequisites

Before running the agent, ensure you have:  

- **[uv](https://docs.astral.sh/uv/getting-started/installation/)**
- **Docker**  
- **Ollama**
---

## Setup

To start the agent using Docker Compose:  

```bash
docker compose up -d
```

This will build and run the agent container in detached mode.

---

## Running the Session Manager

After starting the container, you can run the session manager CLI locally:

```bash
uv venv
uv run chat.py
```

The terminal tool allows you to:

- **Create Session**: Start a new session with memory.
- **Rename Session**: Assign meaningful names to sessions.
- **List Sessions**: View all active sessions with their names.
- **Delete Session**: Remove sessions when no longer needed.

Each session maintains memory, allowing the agent to remember previous interactions.


