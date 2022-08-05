
import json
import requests


info = requests.get("https://imdb-api.com/en/API/Top250Movies/k_2854uh1s")
print(json.loads(info.content)["items"][0])

print("-------------------")
print(info.content)
print("-------------------")

