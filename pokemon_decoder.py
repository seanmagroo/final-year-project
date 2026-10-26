from pokemon_attributes import decode_block_A

def decodePokemon(X):

    A, B, C, D = X[0], X[1], X[2], X[3]
    E, F = X[6], X[7]

    print("PID: ", A, B, C, D)
    print("Checksum: ", E, F)

    pid = A + (B * 256) + (C * 65536) + (D * 16777216)
    checkSum = E + (F * 256)
    encrypted_Data = X[8:136]

    print("PID: ", pid)
    print("Check Sum: ", checkSum)
    print("Encrypted Data: ", encrypted_Data)

    decrypted_Data = decrypt_Data(encrypted_Data, checkSum)
    blockA, blockB, blockC, blockD = unshuffle_blocks(decrypted_Data, pid)

    decoded_block_A = decode_block_A(blockA)
    print(decoded_block_A)

def decrypt_Data(encrypted_Data, seed):

    decrypted_Data = []

    for i in range(0, len(encrypted_Data), 2):
        encrypted_Value = encrypted_Data[i] + (encrypted_Data[i+1] * 256)
        
        seed = (seed * 0x41C64E6D + 0x6073) & 0xFFFFFFFF
        xorKey = seed >> 16 # Right bit shift by 16 bits
    
        decrypted_Value = encrypted_Value ^ xorKey # XOR operation on remaining 16 bits
    
        decrypted_Data.append(decrypted_Value & 0xFF)
        decrypted_Data.append(decrypted_Value >> 8)   # AI generated decryption loop, decrypts the memory data for the pokemon
    
    print("Decrypted data:", decrypted_Data)
    print("Length:", len(decrypted_Data))

    return decrypted_Data

def unshuffle_blocks(decryptedData, pid):

    block0 = decryptedData[0:32]
    block1 = decryptedData[32:64]
    block2 = decryptedData[64:96]
    block3 = decryptedData[96:128]
    
    shuffleValue = ((pid >> 13) & 0x1F) % 24
    print("Shuffle value:", shuffleValue)


    blockOrders = [
    "ABCD", "ABDC", "ACBD", "ACDB", "ADBC", "ADCB",
    "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
    "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA",
    "DABC", "DACB", "DBAC", "DBCA", "DCAB", "DCBA"
    ]
    
    order = blockOrders[shuffleValue]
    print("Block order:", order)
    blocks = [block0, block1, block2, block3]

    blockA = blocks[order.index("A")]
    blockB = blocks[order.index("B")]
    blockC = blocks[order.index("C")]
    blockD = blocks[order.index("D")]

    return blockA, blockB, blockC, blockD
        