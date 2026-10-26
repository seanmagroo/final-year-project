import json
from pokemon_decoder import decodePokemon

file = open("C:/Users/Sean McGrath/Desktop/Year 4 Final Project/Project/Lua/data/live_data.json", "r")
liveData = json.load(file)
file.close()

for pokemon in liveData["party"]:
    decodePokemon(pokemon)