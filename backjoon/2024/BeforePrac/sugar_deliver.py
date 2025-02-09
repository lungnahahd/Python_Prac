sugar_kg = int(input())

sugar_get = 0

while (True):
    if sugar_kg % 5 == 0:
        sugar_get += sugar_kg / 5
        break
    elif sugar_kg < 0:
        sugar_get = -1
        break
    else :
        sugar_kg = sugar_kg - 3
        sugar_get += 1
print(int(sugar_get))