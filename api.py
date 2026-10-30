import json
from flask import Flask
from pokemon_decoder import decodePokemon

app = Flask(__name__)

@app.route("/party")
def get_party():

    with open("data/live_data.json", "r") as file:
        liveData = json.load(file)

    liveParty = []

    for pokemon in liveData["party"]:
        liveParty.append(decodePokemon(pokemon))

    return liveParty