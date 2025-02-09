a = input()
get = int(a)

fnum = 1
bnum = 7
count = 1
cal = 1

if get == 1 :
    print(1)
else :
    while(True):
        cal += 1
        realcal = cal * 6
        if fnum <= get and bnum >= get:
            count +=1
            break
        elif bnum < get:
            fnum = bnum
            bnum = realcal + bnum
            count += 1

    print(count)
