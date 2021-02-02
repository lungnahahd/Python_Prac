import math


a = input()
get = int(a)

fnum = 1
bnum = 2
sum = fnum + bnum
if get == 1:
    print("1/1")
else:
    while(True):
        if sum < get:
            fnum = bnum
            bnum += 1
        else : 
            if bnum % 2 != 0 :
                up = sum % get
                up = math.floor(up) + 1
                down = bnum - up + 1
            else : 
                down = sum % get
                down = math.floor(down) + 1
                up = bnum - down + 1
            print(str(up) + "/" + str(down))
            break
        sum = sum + bnum