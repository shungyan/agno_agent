from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.db.sqlite import SqliteDb
from agno.tools.mcp import MCPTools
from agno.os import AgentOS
import uvicorn

INSTRUCTION = """
You are a agent that can do RAG
"""

# Create the Agno Agent
agno_agent = Agent(
    name="Agno Agent",
    model=Ollama(id="qwen3:8b", provider="Ollama",host="http://host.docker.internal:11434"),
    db=SqliteDb(db_file="agno.db"),
    tools=[MCPTools(transport="streamable-http", url="http://host.docker.internal:6969/mcp")],
    add_history_to_context=True,
    enable_session_summaries=True,
    add_session_summary_to_context=True,
    num_history_runs=10,
    markdown=True,
    instructions=INSTRUCTION
)

# ************* Create AgentOS *************
agent_os = AgentOS(agents=[agno_agent])
# Get the FastAPI app for the AgentOS
app = agent_os.get_app()

# ************* Run AgentOS *************
if __name__ == "__main__":
    agent_os.serve(app="agno_agent:app", host="0.0.0.0",reload=True)