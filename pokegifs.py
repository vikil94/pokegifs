import json
import requests
import os


res = requests.get("https://pokeapi.co/api/v2/pokemon/charizard/")
body = json.loads(res.content)

print(body['types'])
print(body['name'])

my_key = os.environ.get("GIPHY_KEY")
pokemon = "mewtwo"
rating = "g"
gif_url = (f"https://api.giphy.com/v1/gifs/search?api_key={my_key}&q={pokemon}&rating={rating}")


requests.get(gif_url)
print(f"This is the gif: {gif_url}")