function pokemonPartyRetriever()

    local A,B,C,D,littleEndian,partyOffset,party,X,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,partyCount
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

    partyCount = memory.readbyte(party - 4)
    print("Party size:", partyCount)

    pokemon1 = memory.readbyterange(party,236)
    if partyCount >= 2 then
        pokemon2 = memory.readbyterange(party + 236,236)
    end
    if partyCount >= 3 then
        pokemon3 = memory.readbyterange(party + 472,236)
    end
    if partyCount >= 4 then
        pokemon4 = memory.readbyterange(party + 708,236)
    end
    if partyCount >= 5 then
        pokemon5 = memory.readbyterange(party + 944,236)
    end
    if partyCount >= 6 then
        pokemon6 = memory.readbyterange(party + 1180,236)
    end

    print ("1st Party Member: ", pokemon1)
    print ("2nd Party Member: ", pokemon2)
    print ("3rd Party Member: ", pokemon3)
    print ("4th Party Member: ", pokemon4)
    print ("5th Party Member: ", pokemon5)
    print ("6th Party Member: ", pokemon6)


    return pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6
end   

local lastUpdate = 0

while true do

    local currentTime = os.time()
    
    if currentTime - lastUpdate >= 2 then

        pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6 = pokemonPartyRetriever()

        local file = io.open("C:/Users/Sean McGrath/Desktop/Year 4 Final Project/Project/Lua/data/live_data.json", "w")

        pokemon1TableString = table.concat(pokemon1, ",")
        file:write('{"party": [')
        file:write("\n")
        file:write("[", pokemon1TableString, "]")

        if pokemon2 ~= nil then
            pokemon2TableString = table.concat(pokemon2, ",")
            file:write(",\n[", pokemon2TableString, "]")
        end

        if pokemon3 ~= nil then
            pokemon3TableString = table.concat(pokemon3, ",")
            file:write(",\n[", pokemon3TableString, "]")
        end

        if pokemon4 ~= nil then
            pokemon4TableString = table.concat(pokemon4, ",")
            file:write(",\n[", pokemon4TableString, "]")
        end

        if pokemon5 ~= nil then
            pokemon5TableString = table.concat(pokemon5, ",")
            file:write(",\n[", pokemon5TableString, "]")
        end

        if pokemon6 ~= nil then
            pokemon6TableString = table.concat(pokemon6, ",")
            file:write(",\n[", pokemon6TableString, "]")
        end

        file:write("\n]}")
        file:close()

        lastUpdate = currentTime
    end

    for i = 1, 60 do
        emu.frameadvance()
    end

end