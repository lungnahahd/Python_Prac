# 최소공배수
## 두 자연수 A와 B가 주어지고, 그 두 자연수의 최소공배수를 구하는 프로그램
### 입력 : 첫째 줄에는 몇 번 실행할 것인지가 주어지고, 그 다음 줄부터는 각각 2개씩 자연수가 입력
### 출력 : 입력으로 주어진 두 자연수 쌍의 최소공배수를 구해서 출력

import sys
input = sys.stdin.readline

caseNum = int(input())
result = []

for i in range(caseNum):
    bigNum, smallNum = 0, 0
    a, b = map(int,input().split())
    if a > b:
        bigNum = a
        smallNum = b
    elif a < b:
        bigNum = b
        smallNum = a
    elif a == b:
        result.append(a)
        continue
    count = 1
    while True:
        checkNum = count * bigNum
        if checkNum % smallNum == 0:
            result.append(checkNum)
            break
        else:
            count += 1

for i in result:
    print(i)