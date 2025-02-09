# 음계 (2920)


music = list(map(int, input().split()))

if (music[0] != 1 and music[0] != 8):
    print("mixed")
elif (music[0] == 1):
    start = 1
    for m in music:
        if(m != start):
            print("mixed")
            break
        start += 1
    if (start == 9):
        print("ascending")
elif (music[0] == 8):
    start = 8
    for m in music:
        if(m != start):
            print("mixed")
            break
        start -= 1
    if (start == 0):
        print("descending")
        
print(music)

