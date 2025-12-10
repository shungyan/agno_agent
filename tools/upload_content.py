import requests

# Upload a file
url = "http://localhost:7777/knowledge/content"

# Replace with your actual db_id from your SqliteDb configuration
params = {
    "db_id": "knowledge_db"  # The id you set in SqliteDb(id="...")
}

file_path = r"C:\Users\SiP-SY Tham\Desktop\agno\kohyoung.txt"

files = {
    "file": ("kohyoung.txt", open(file_path, "rb"), "text/plain")
}

data = {
    "name": "My Document",
    "description": "Optional description"
}

response = requests.post(url, params=params, files=files, data=data)
print(response.json())