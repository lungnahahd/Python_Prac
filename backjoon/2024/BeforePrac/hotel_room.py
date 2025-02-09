import math

count = input()
count = int(count)

for i in range(count):
    if i == 0:
        m=[]
    h, w, n = input().split()
    height = int(h)
    room = int(w)
    guest = int(n)

    front = guest % height
    if front == 0 :
        front = height
    
    back = math.ceil(guest / height)


    if back < 10:
        back_str = "0" + str(back)
    else : 
        back_str = str(back)

    getnum = str(front) + back_str
    m.append(getnum)
    
    if i == count - 1:
        for j in m:
            print(j)

 