import math
import sys
input = sys.stdin.readline

beforeNum = int(input())

standard = int(math.sqrt(beforeNum))
eratosList = [True for i in range(beforeNum + 1)]
eratosList[0] = False
eratosList[1] = False

for i in range(2,standard + 1):
    if eratosList[i]:
        check = 2
        while (check * i) <= beforeNum:
            eratosList[check * i] = False
            check += 1


result = []
calCount = 2
while not eratosList[beforeNum]:
    if eratosList[calCount]:
        if beforeNum % calCount == 0:
            result.append(calCount)
            beforeNum = beforeNum // calCount
        else:
            calCount += 1
    else:
        calCount += 1
result.append(beforeNum)

for i in result:
    print(i)