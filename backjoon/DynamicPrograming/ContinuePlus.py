# 연속합
## 임의의 수열이 제공되며 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 가장 큰 합을 구하기
### 입력 : 첫 줄에 정수의 크기가 입력되고, 두번 째 줄에는 수열이 입력
### 출력 : 첫 줄에 연속 수열 합의 최대가 출력


################### 같은 부호일 경우 tempResult에서 동일하게 처리해줘보기

# 10
# 14 40 80 84 -22 -28 72 80 69 -44
# 221

# 정답 : 390


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
    elif i > 0:
        temp += i
    elif i == 0:
        tempResult.append(i)
tempLarge = max(tempResult)

plusTemp = 0
minusTemp = 0
secondTemp = []
for i in tempResult:
    if i < 0:
        minusTemp += i
        if plusTemp != 0:
            secondTemp.append(plusTemp)
            plusTemp = 0
    elif i > 0:
        plusTemp += i
        if minusTemp != 0:
            secondTemp.append(minusTemp)
            minusTemp = 0
if minusTemp != 0:
    secondTemp.append(minusTemp)
if plusTemp != 0:
    secondTemp.append(plusTemp)
            

temp = 0
finalResult = []
for i in range(len(secondTemp)):   
    if secondTemp[i] < 0 :
        if i == 0:
            continue
            #finalResult.append(tempResult[i])
        elif i == len(secondTemp) - 1:
            break
        else:
            if -secondTemp[i] < secondTemp[i-1] and -secondTemp[i] < secondTemp[i+1]:
                finalResult.append(secondTemp[i] + secondTemp[i-1] + secondTemp[i + 1])
            else:
                finalResult.append(secondTemp[i-1])
    elif tempResult[i] > 0 and i == len(tempResult) -1 :
        finalResult.append(tempResult[i])
if len(finalResult) == 0:
    print(tempLarge)
else:
    finalLarge = max(finalResult)

    if finalLarge > tempLarge:
        print(finalLarge)
    else:
        print(tempLarge)