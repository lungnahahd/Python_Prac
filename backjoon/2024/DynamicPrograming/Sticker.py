# 스티커
## 스티커를 최대 점수를 뗄 수 있도록 하는 것
### 입력 : 첫 줄에 테스트 개수 T가 입력
### 입력 : 각 테스트 케이스 첫 줄에는 n, 다음부터는 n개의 위치 스티커 점수
### 출력 : 스티커 점수의 최댓값을 출력

import sys
from typing import Final, Tuple
input = sys.stdin.readline

Size = int(input())

final = []



checkBool = [False,False]
checkA = False
checkB = False

def sum(a,b):
    result = [0,0]
    if checkBool[0]:
        checkBool[0] = False
        if a[0] + b[1] > a[0] + b[0]:
            result[1] = a[0] + b[1]
        else:
            result[0] = a[0] + b[0]
    elif checkBool[1]:
        checkBool[1] = False
        if a[1] + b[1] > a[1] + b[0]:
            result[1] = a[1] + b[1]
        else:
            result[0] = a[1] + b[0]
    for i in range(2):
 
        if i == 0:
            if a[0] + b[1] > a[1]:
                result[1] = a[0] + b[1]
            else:
                result[1] = a[1]
                checkBool[1] = True
        else:
            if a[1] + b[0] > a[0]:
                result[0] = a[1] + b[0]
            else:
                result[0] = a[0]
                checkBool[0] = True
    return result




result=[]
for a in range(Size):
    case = int(input())
    # sticker = [[0 for col in range(case)] for row in range(1)]
    inputSticker = []
    inputSticker.append(list(map(int,input().split())))
    inputSticker.append(list(map(int,input().split())))

    check = 0
    tempA =[]
    tempA.append(inputSticker[0][0])
    tempA.append(inputSticker[1][0])
    while check < case - 1:
        tempB = [inputSticker[0][check+1],inputSticker[1][check+1]]
        tempA = sum(tempA,tempB)
        check+= 1
    
    result.append(max(tempA))
    #print(tempA)

for i in result:
    print(i)