def pokeName(X):

    A, B, C, D = X[0], X[1], X[2], X[3]
    E, F = X[6], X[7]

    print("PID: ", A, B, C, D)
    print("Checksum: ", E, F)

    littleEndian = A + (B * 256) + (C * 65536) + (D * 16777216)
    checkSum = E + (F * 256)
    encryptedData = X[8:136]

    print("Little Endian:", littleEndian)
    print("Check Sum: ", checkSum)
    print("Encrypted Data: ", encryptedData)

    seed = checkSum
    decryptedData = []

    for i in range(0, len(encryptedData), 2):
        encryptedValue = encryptedData[i] + (encryptedData[i+1] * 256)

        seed = (seed * 0x41C64E6D + 0x6073) & 0xFFFFFFFF
        xorKey = seed >> 16

        decryptedValue = encryptedValue ^ xorKey

        decryptedData.append(decryptedValue & 0xFF)
        decryptedData.append(decryptedValue >> 8)   # AI generated decryption loop, decrypts the memory data for the pokemon

    print("Decrypted data:", decryptedData)
    print("Length:", len(decryptedData))

    block0 = decryptedData[0:32]
    block1 = decryptedData[32:64]
    block2 = decryptedData[64:96]
    block3 = decryptedData[96:128]

    shuffleValue = ((littleEndian >> 13) & 0x1F) % 24
    print("Shuffle value:", shuffleValue)

    blockA = block1
    speciesID = blockA[0] + (blockA[1] * 256)
    print("Species ID:", speciesID)

file = open("C:/Users/Sean McGrath/Desktop/Year 4 Final Project/Project/Lua/liveData/live_data.txt", "r")
pokemon1TableString = file.read()
pokemon1TableNumber = pokemon1TableString.split(",")

for i in range(len(pokemon1TableNumber)):
    pokemon1TableNumber[i] = int(pokemon1TableNumber[i])
print(pokemon1TableNumber)
file.close()

pokeName(pokemon1TableNumber)