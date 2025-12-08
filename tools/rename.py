import requests

session_id = "4077e43b-09ae-4e01-bbdc-f51fd515a4a2"
url = f"http://localhost:7777/sessions/{session_id}/rename?type=agent"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

data = {
    "session_name": "red"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json().get("session_name")) 
