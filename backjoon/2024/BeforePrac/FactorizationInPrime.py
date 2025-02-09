import math
import sys
input = sys.stdin.readline

beforeNum = int(input())

result = []
for i in range(2, beforeNum + 1):
    while True:
        if beforeNum % i == 0:
            result.append(i)
            beforeNum = beforeNum // i
        else:
            break
    if beforeNum == i:
        break


for i in result:
    print(i)
