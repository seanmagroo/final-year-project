function partyPokeOne()

local A,B,C,D,littleEndian,partyOffset,party,X
A = memory.readbyte(0x02101D2C)
B = memory.readbyte(0x02101D2D)
C = memory.readbyte(0x02101D2E)
D = memory.readbyte(0x02101D2F)
print("Memory: " .. A,B,C,D) -- Pointer to party memory address

littleEndian = A + (B * 256) + (C * 65536) + (D *16777216)
print("littleEndian: " .. littleEndian)

partyOffset = 0xD094

party = littleEndian + partyOffset -- adding party offset gives address of the first pokemon
print("Party: " .. party) 

X = memory.readbyterange(party,236) -- all addresses of first pokemon

print ("1st Party Member: ", X)

return X

end   

pokemon1 = partyPokeOne()
pokeName(pokemon1) -- In future bring this logic into the python script