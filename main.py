from pokemon_decoder import decodePokemon

file = open("C:/Users/Sean McGrath/Desktop/Year 4 Final Project/Project/Lua/data/live_data.txt", "r")
pokemon1TableString = file.read()
pokemon1TableNumber = pokemon1TableString.split(",")

for i in range(len(pokemon1TableNumber)):
    pokemon1TableNumber[i] = int(pokemon1TableNumber[i])
#print(pokemon1TableNumber)
file.close()

decodePokemon(pokemon1TableNumber) 