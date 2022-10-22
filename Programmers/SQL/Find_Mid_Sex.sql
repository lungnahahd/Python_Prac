SELECT ain.ANIMAL_ID, ain.ANIMAL_TYPE, ain.NAME FROM ANIMAL_INS AS ain JOIN ANIMAL_OUTS AS aout ON ain.ANIMAL_ID = aout.ANIMAL_ID and aout.SEX_UPON_OUTCOME != ain.SEX_UPON_INTAKE WHERE aout.SEX_UPON_OUTCOME LIKE "%Spayed%" or aout.SEX_UPON_OUTCOME LIKE "%Neutered%"