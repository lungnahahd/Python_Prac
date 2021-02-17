import sys
input = sys.stdin.readline
num = input()
num = int(num)
count = 0

for num in range(num):
    words = input()
    re = list(words)
    vps = 0
    flag = True
    for i in range(len(re)-1):
        if re[i] == "(":
            vps += 1
        else :
            vps += -1
        if vps < 0:
            flag = False
            break
    if flag and vps == 0 :
        print("YES")
    else:
        print("NO")