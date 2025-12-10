import requests

url = "http://localhost:7777/sessions?type=agent"
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)

sessions = response.json()

# Print sessions in a readable way
for i, session in enumerate(sessions.get("data", []), start=1):
    print(f"{i}. Session ID: {session.get('session_id')}, Session Name: {session.get('session_name')}")
