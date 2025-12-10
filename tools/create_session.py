import requests

url = "http://localhost:7777/sessions?type=agent"
headers = {
    "Content-Type": "application/json"
}
data = {
    "session_name": "My Session"
}

response = requests.post(url, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)   
session_data = response.json()
session_id = session_data.get("session_id")
session_name = session_data.get("session_name")
    
print(session_id)
print(session_name)