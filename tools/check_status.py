import requests

content_id = "392d3828-d091-5e61-8d09-f9b398330a5a"
db_id = "knowledge_db"  # The id you set in SqliteDb(id="...")

# Check content status
url = f"http://localhost:7777/knowledge/content/{content_id}/status"
params = {"db_id": db_id}

response = requests.get(url, params=params)
print(response.json())
# Returns: {"status": "processing", "status_message": ""}