from mcp.server.fastmcp import Context, FastMCP
import sys
from dotenv import load_dotenv
import os
import requests, json
from datetime import datetime
import ollama, chromadb
from ollama import Client

# Load .env file
load_dotenv()

# Access environment variables
server = os.getenv("server")
database = os.getenv("database")
user = os.getenv("user")
password = os.getenv("password")


mcp = FastMCP("service", host="0.0.0.0", port=6969)


@mcp.tool()
def rag(
    query: str,
) -> dict:
    """
    use rag to understand key features of each machine

    if multiple machine is queried, use rag one by one, for example:
    what is the difference between zenith lite and zenith alpha

    rag(zenith lite)
    rag(zenith alpha)

    Args:
    query (str): Machine name you want to know
    """
    client = Client(host="http://host.docker.internal:11434")
    embedmodel = "nomic-embed-text"
    chroma = chromadb.HttpClient(host="host.docker.internal", port=7999)
    collection = chroma.get_or_create_collection("kohyoung")
    print(collection)
    queryembed = client.embeddings(model=embedmodel, prompt=query)["embedding"]
    print(queryembed)
    relevantdocs = collection.query(query_embeddings=[queryembed], n_results=5)[
        "documents"
    ][0]
    docs = "\n\n".join(relevantdocs)

    return {
        "related info": docs,
    }


if __name__ == "__main__":
    try:
        # Run the server
        mcp.run(transport="streamable-http")

    except KeyboardInterrupt:
        print("Server shutting down gracefully...")
        print("Server has been shut down.")

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    finally:
        print("Thank you for using MCP Server!")