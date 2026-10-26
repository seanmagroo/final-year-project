def decode_block_A(blockA):
    species_Id = blockA[0] + (blockA[1] * 256)
    held_Item_Id = blockA[2] + (blockA[3] * 256)
    
    trainer_Id = blockA[4] + (blockA[5] * 256)
    trainer_Secret_Id = blockA[6] + (blockA[7] * 256)
    
    experience = blockA[8] + (blockA[9] * 256) + (blockA[10] * 65536) + (blockA[11] * 16777216)
    
    Friendship = blockA[12]
    Ability_Id = blockA[13]
    markings = blockA[14]
    language = blockA[15]

    hp_Ev = blockA[16]
    attack_Ev = blockA[17]
    defense_Ev = blockA[18]
    speed_Ev = blockA[19]
    spAtk_Ev = blockA[20]
    spDef_Ev = blockA[21]

    return {
    "species_Id": species_Id,
    "held_Item_Id": held_Item_Id,
    "trainer_Id": trainer_Id,
    "trainer_Secret_Id": trainer_Secret_Id,
    "experience": experience,
    "Friendship": Friendship,
    "Ability_Id": Ability_Id,
    "markings": markings,
    "language": language,
    "hp_Ev": hp_Ev,
    "attack_Ev": attack_Ev,
    "defense_Ev": defense_Ev,
    "speed_Ev": speed_Ev,
    "spAtk_Ev": spAtk_Ev,
    "spDef_Ev": spDef_Ev
    }