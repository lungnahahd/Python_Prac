# 문제 추천 시스템
## TreeSet 사용 이유 :  쌍으로 대입하여 각 위치에서 최대 최소를 빠르게 찾기 위해 사용

from sortedcontainers import SortedSet
s = SortedSet()

bookSize = int(input())

for i in range(bookSize):
    num,hard = input().split()
    s.add((int(hard), int(num)))

cmdSize = int(input())
for i in range(cmdSize):
    cmd = input().split()
    if cmd[0] == "rc":
        if cmd[1] == "1":
            hard, num = s[-1]
            print(num)
        else:
            hard,num = s[0]
            print(num)
    elif cmd[0] == "sv":
        s.remove((int(cmd[2]),int(cmd[1])))
    else :
        s.add((int(cmd[2]),int(cmd[1])))
