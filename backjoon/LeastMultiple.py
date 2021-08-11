# 최소공배수
## 두 자연수 A와 B가 주어지고, 그 두 자연수의 최소공배수를 구하는 프로그램
### 입력 : 첫째 줄에는 몇 번 실행할 것인지가 주어지고, 그 다음 줄부터는 각각 2개씩 자연수가 입력
### 출력 : 입력으로 주어진 두 자연수 쌍의 최소공배수를 구해서 출력

import sys
input = sys.stdin.readline

caseNum = int(input())
result = []

for i in range(caseNum):
    bigNum, smallNUm = 0, 0
    a, b = map(int,input().split())
    if a > b:
        bigNum = a
        smallNUm = b
    elif a < b:
        bigNum = b
        smallNUm = a
    else:
        result.append(a)    
        #print(a)
        continue
    if smallNUm == 1:
        result.append(bigNum)
        #print(bigNum)
        continue
    if bigNum % smallNUm == 0 :
        result.append(bigNum)
        continue
    check = smallNUm - 1
    while True:
        if smallNUm % check == 0:
            if check * bigNum % smallNUm == 0:
                result.append(check* bigNum)
                #print(check * bigNum)
                break
            else:
                result.append(bigNum*smallNUm)
                #print(bigNum * smallNUm)
                break
        else:
            check = check - 1
        if check < smallNUm / 2:
            result.append(bigNum* smallNUm)
            break
    
for i in result:
    print(i)