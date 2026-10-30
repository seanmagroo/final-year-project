import json
from flask import Flask
from pokemon_decoder import decodePokemon
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LIVE_DATA_PATH = PROJECT_ROOT / "Lua" / "data" / "live_data.json"

app = Flask(__name__)

@app.route("/party")
def get_party():

    with LIVE_DATA_PATH.open("r", encoding="utf-8") as file:
        liveData = json.load(file)

    liveParty = []

    for pokemon in liveData["party"]:
        liveParty.append(decodePokemon(pokemon))

    return liveParty