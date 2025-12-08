import requests

session_id = "671ec414-cc44-4fa2-a059-9ecd5503f3ce"
url = f"http://localhost:7777/sessions/{session_id}?type=agent"

headers = {
    "accept": "application/json"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json().get("session_name")) 
