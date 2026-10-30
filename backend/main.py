import json
import time
import os
from pokemon_decoder import decodePokemon

previousParty = None

while True:

    file = open("C:/Users/Sean McGrath/Desktop/Year 4 Final Project/Project/Lua/data/live_data.json", "r")
    liveData = json.load(file)
    file.close()

    if previousParty != liveData["party"]:
        os.system("cls")
        liveParty = []
        
        for pokemon in liveData["party"]:
            liveParty.append(decodePokemon(pokemon))
            print("#########################################")
        
        previousParty = liveData["party"]

    time.sleep(2)