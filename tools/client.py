import requests

# 2️⃣ Interactive loop
agent_url = "http://localhost:7777/agents/agno-agent/runs"

while True:
    try:
        message = input("You: ")
        if message.lower() in {"exit", "quit"}:
            break

        # Send message to agent
        files = {
            "message": (None, message),
            "stream": (None, "false"),
            "session_id": (None, "4077e43b-09ae-4e01-bbdc-f51fd515a4a2")
        }

        agent_response = requests.post(agent_url, files=files)
        agent_response.raise_for_status()
        data = agent_response.json()

        # Extract only the content
        content = data.get("content") or data.get("response") or data
        print(f"Agent: {content}")

    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"Error: {e}")
