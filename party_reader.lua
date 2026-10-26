function pokemonPartyRetriever()

local A,B,C,D,littleEndian,partyOffset,party,X,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6
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

pokemon1 = memory.readbyterange(party,236) -- all addresses of first pokemon
pokemon2 = memory.readbyterange(party + 236,236)
pokemon3 = memory.readbyterange(party + 472,236)
pokemon4 = memory.readbyterange(party + 708,236)
pokemon5 = memory.readbyterange(party + 944,236)
pokemon6 = memory.readbyterange(party + 1180,236)

print ("1st Party Member: ", pokemon1)
print ("2nd Party Member: ", pokemon2)
print ("3rd Party Member: ", pokemon3)
print ("4th Party Member: ", pokemon4)
print ("5th Party Member: ", pokemon5)
print ("6th Party Member: ", pokemon6)

return pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6
end   

pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6 = pokemonPartyRetriever()

local file = io.open("C:/Users/Sean McGrath/Desktop/Year 4 Final Project/Project/Lua/data/live_data.json", "w")
pokemon1TableString = table.concat(pokemon1, ",")
pokemon2TableString = table.concat(pokemon2, ",")
pokemon3TableString = table.concat(pokemon3, ",")
pokemon4TableString = table.concat(pokemon4, ",")
pokemon5TableString = table.concat(pokemon5, ",")
pokemon6TableString = table.concat(pokemon6, ",")

file:write('{"party": [')

file:write("\n")
file:write("[", pokemon1TableString, "],")
file:write("\n")

file:write("[", pokemon2TableString, "],")
file:write("\n")

file:write("[", pokemon3TableString, "],")
file:write("\n")

file:write("[", pokemon4TableString, "],")
file:write("\n")

file:write("[", pokemon5TableString, "],")
file:write("\n")

file:write("[", pokemon6TableString, "]")
file:write("\n")

file:write("]")
file:write("}")

file:close()