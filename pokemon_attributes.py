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

def decode_block_B(blockB):
    move1_Id = blockB[0] + (blockB[1] * 256)
    move1_Pp = blockB[8]
    move1_Pp_Ups = blockB[12]

    move2_Id = blockB[2] + (blockB[3] * 256)
    move2_Pp = blockB[9]
    move2_Pp_Ups = blockB[13]

    move3_Id = blockB[4] + (blockB[5] * 256)
    move3_Pp = blockB[10]
    move3_Pp_Ups = blockB[14]
    
    move4_Id = blockB[6] + (blockB[7] * 256)
    move4_Pp = blockB[11]
    move4_Pp_Ups = blockB[15]

    iv_Data = blockB[16] + (blockB[17] * 256) + (blockB[18] * 65536) + (blockB[19] * 16777216)
    hp_Iv = iv_Data & 0x1F
    attack_Iv = (iv_Data >> 5) & 0x1F
    defense_Iv = (iv_Data >> 10) & 0x1F
    speed_Iv = (iv_Data >> 15) & 0x1F
    spAtk_Iv = (iv_Data >> 20) & 0x1F
    spDef_Iv = (iv_Data >> 25) & 0x1F

    return {
    "move1_Id": move1_Id,
    "move1_Pp": move1_Pp,
    "move1_Pp_Ups": move1_Pp_Ups,
    "move2_Id": move2_Id,
    "move2_Pp": move2_Pp,
    "move2_Pp_Ups": move2_Pp_Ups,
    "move3_Id": move3_Id,
    "move3_Pp": move3_Pp,
    "move3_Pp_Ups": move3_Pp_Ups,
    "move4_Id": move4_Id,
    "move4_Pp": move4_Pp,
    "move4_Pp_Ups": move4_Pp_Ups,
    "hp_Iv": hp_Iv,
    "attack_Iv": attack_Iv,
    "defense_Iv": defense_Iv,
    "speed_Iv": speed_Iv,
    "spAtk_Iv": spAtk_Iv,
    "spDef_Iv": spDef_Iv
    }