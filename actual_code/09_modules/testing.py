import requests

data = requests.get("https://www.google.com")

print(data.text)