import requests
db_id = "21138089-9477-5cb5-98c0-fdc32ef6f1e0"
session_url = f"http://localhost:7777/sessions?type=agent&db_id={db_id}&session_name=test"

response = requests.post(session_url, json={})
response.raise_for_status()
session_data = response.json()
session_id = session_data.get("session_id")
session_name = session_data.get("session_name")
    
print(session_id)
print(session_name)