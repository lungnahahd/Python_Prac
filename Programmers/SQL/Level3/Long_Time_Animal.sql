SELECT ain.ANIMAL_ID, ain.NAME FROM ANIMAL_INS AS ain JOIN ANIMAL_OUTS AS aout on ain.ANIMAL_ID = aout.ANIMAL_ID ORDER BY (aout.DATETIME - ain.DATETIME) DESC LIMIT 2