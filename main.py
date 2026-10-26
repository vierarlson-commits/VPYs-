import requests
import json

response = requests.get("https://api.github.com/users/octocat")

json_data = json.dumps(response.json(), indent=2)

print(json_data)