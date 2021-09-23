# 연속합
## 임의의 수열이 제공되며 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 가장 큰 합을 구하기
### 입력 : 첫 줄에 정수의 크기가 입력되고, 두번 째 줄에는 수열이 입력
### 출력 : 첫 줄에 연속 수열 합의 최대가 출력

import sys
from typing import Counter, final
input = sys.stdin.readline

size = int(input())
get = input().split()
numList = []
for i in get:
    numList.append(int(i))

tempResult = []
temp = 0
for i in numList:
    if i < 0:
        if temp == 0:
            tempResult.append(i)
        else:
            tempResult.append(temp)
            temp = 0
            tempResult.append(i)
    elif i >= 0:
        temp += i
#print(tempResult)
tempLarge = max(tempResult)

temp = 0
finalResult = []
count = 0
for i in range(len(tempResult)):   
    if tempResult[i] < 0 :
        if i == 0:
            finalResult.append(tempResult[i])
        elif i == len(tempResult) - 1:
            finalResult.append(tempResult[i-1])
            finalResult.append(tempResult[i])
        else:
            if -tempResult[i] < tempResult[i-1] and -tempResult[i] < tempResult[i+1] and tempResult[i-1] > 0 and tempResult[i + 1] > 0:
                finalResult.append(tempResult[i]+tempResult[i-1] + tempResult[i+1])
            else:
                finalResult.append(tempResult[i-1])
    elif tempResult[i] > 0 and i == len(tempResult) -1 :
        finalResult.append(tempResult[i])
finalLarge = max(finalResult)

if finalLarge > tempLarge:
    print(finalLarge)
else:
    print(tempLarge)
    