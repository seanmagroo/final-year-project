import json
from pokemon_attributes import decode_block_A, decode_block_B
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
POKEMON_DATA_PATH = PROJECT_ROOT / "Lua" / "data" / "pokemon.json"

def decodePokemon(X):

    with POKEMON_DATA_PATH.open("r", encoding="utf-8") as file:
        pokemonData = json.load(file)

    A, B, C, D = X[0], X[1], X[2], X[3]
    E, F = X[6], X[7]

    # print("PID: ", A, B, C, D)
    # print("Checksum: ", E, F)

    pid = A + (B * 256) + (C * 65536) + (D * 16777216)
    checkSum = E + (F * 256)
    encrypted_Data_Blocks = X[8:136]

    # print("PID: ", pid)
    # print("Check Sum: ", checkSum)
    # print("Encrypted Data: ", encrypted_Data)

    decrypted_Data_Blocks = decrypt_Data(encrypted_Data_Blocks, checkSum)
    blockA, blockB, blockC, blockD = unshuffle_blocks(decrypted_Data_Blocks, pid)

    decoded_block_A = decode_block_A(blockA)
    decoded_block_B = decode_block_B(blockB)

    encrypted_Data = X[136:236]
    decrypted_Data = decrypt_Data(encrypted_Data, pid)
    level = decrypted_Data[4]
    currentHp = decrypted_Data[6] + decrypted_Data[7] * 256
    maxHp = decrypted_Data[8] + decrypted_Data[9] * 256


    statusFlag = decrypted_Data[0]
    status = "Healthy"
    if statusFlag & 0x07: # Sleep occupies 3 bits
        status = "Sleep"
    elif statusFlag & 0x08:
        status = "Poisoned"
    elif statusFlag & 0x10:
        status = "Burned"
    elif statusFlag & 0x20:
        status = "Frozen"
    elif statusFlag & 0x40:
        status = "Paralyzed"
    elif statusFlag & 0x80:
        status = "Badly Poisoned"

    species_Id = decoded_block_A["species_Id"]

    print()
    print(pokemonData[str(species_Id)]["name"])
    print(pokemonData[str(species_Id)]["types"])
    print(f"Level: {level} | HP: {currentHp} /{maxHp} | Status: {status}")
    print()
    print(pokemonData[str(species_Id)]["baseStats"])
    print()
    print(decoded_block_A)
    print()
    print(decoded_block_B)
    print()

    return{
    "species_Id": species_Id,
    "name": pokemonData[str(species_Id)]["name"],
    "types": pokemonData[str(species_Id)]["types"],
    "level": level,
    "currentHp": currentHp,
    "maxHp": maxHp,
    "status": status,
    "baseStats": (pokemonData[str(species_Id)]["baseStats"]),
    "blockA": decoded_block_A,
    "blockB": decoded_block_B
    }

def decrypt_Data(encrypted_Data, seed):

    decrypted_Data = []

    for i in range(0, len(encrypted_Data), 2):
        encrypted_Value = encrypted_Data[i] + (encrypted_Data[i+1] * 256)
        
        seed = (seed * 0x41C64E6D + 0x6073) & 0xFFFFFFFF
        xorKey = seed >> 16 # Right bit shift by 16 bits
    
        decrypted_Value = encrypted_Value ^ xorKey # XOR operation on remaining 16 bits
    
        decrypted_Data.append(decrypted_Value & 0xFF)
        decrypted_Data.append(decrypted_Value >> 8)   # AI generated decryption loop, decrypts the memory data for the pokemon
    
    # print("Decrypted data:", decrypted_Data)
    # print("Length:", len(decrypted_Data))

    return decrypted_Data

def unshuffle_blocks(decryptedData, pid):

    block0 = decryptedData[0:32]
    block1 = decryptedData[32:64]
    block2 = decryptedData[64:96]
    block3 = decryptedData[96:128]
    
    shuffleValue = ((pid >> 13) & 0x1F) % 24
    # print("Shuffle value:", shuffleValue)


    blockOrders = [
    "ABCD", "ABDC", "ACBD", "ACDB", "ADBC", "ADCB",
    "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
    "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA",
    "DABC", "DACB", "DBAC", "DBCA", "DCAB", "DCBA"
    ]
    
    order = blockOrders[shuffleValue]
    # print("Block order:", order)
    blocks = [block0, block1, block2, block3]

    blockA = blocks[order.index("A")]
    blockB = blocks[order.index("B")]
    blockC = blocks[order.index("C")]
    blockD = blocks[order.index("D")]

    return blockA, blockB, blockC, blockD
        