import requests

# URL to list sessions
url = "http://localhost:7777/sessions"
params = {
    "type": "agent",
    "component_id": "agno-agent",
    "limit": 20,
    "page": 1,
    "sort_by": "created_at",
    "sort_order": "desc"
}

response = requests.get(url, params=params)
response.raise_for_status()

sessions = response.json()

# Print sessions in a readable way
for i, session in enumerate(sessions.get("data", []), start=1):
    print(f"{i}. Session ID: {session.get('session_id')}, Session Name: {session.get('session_name')}")
