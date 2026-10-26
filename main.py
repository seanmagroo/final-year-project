def pokeName(X):

    print("PID:", X[0], X[1], X[2], X[3])
    print("Checksum:", X[6], X[7])

    A, B, C, D = X[0], X[1], X[2], X[3]
    E, F = X[6], X[7]

    littleEndian = A + (B * 256) + (C * 65536) + (D * 16777216)
    checkSum = E + (F * 256)

    return littleEndian, checkSum

file = open("C:/Users/Sean McGrath/Desktop/Year 4 Final Project/Project/Lua/liveData/live_data.txt", "r")
pokemon1TableString = file.read()
pokemon1TableNumber = pokemon1TableString.split(",")
for i in range(len(pokemon1TableNumber)):
    pokemon1TableNumber[i] = int(pokemon1TableNumber[i])

print(pokemon1TableNumber)
file.close()