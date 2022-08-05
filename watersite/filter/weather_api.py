# API key
# b2dd5c69be01455f75bf8ba04be10678


import requests

info = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Nur-Sultan&appid=b2dd5c69be01455f75bf8ba04be10678&units=metric")

print("-------------------")
print(info.content)
print("-------------------")
