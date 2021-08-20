import requests
import json

url = "http://localhost:5000/users"

payload = json.dumps({
  "userid": 3,
  "username": "Mary",
  "email": "Mary@gmail.com",
  "role": "Member",
  "password": "abc123"
})
headers = {
  'Content-Type': 'application/json'
}

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
print(payload)
