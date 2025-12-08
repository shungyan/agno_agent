import requests

url = "http://localhost:7777/sessions/f4b57df1-f661-420f-9d4e-0086fc2bf45b"
headers = {
    "accept": "*/*"
}

response = requests.delete(url, headers=headers)

print(response.status_code)
print(response.text)
