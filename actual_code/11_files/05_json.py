import json
import requests

# Request -> url, verb/method, headers, body
# Response -> status code

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
data = response.json()

print(data)

with open('pikachu.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)