# 연속합2
## 수열이 주어지고, 연속된 몇 개의 수를 선택해서 구할 수 있는 가장 큰 합 구하기
## 단, 수는 한 개 이상 선택해야하고, 수열에서 수를 하나 제거할 수도 있음(제거하지 않아도 됨)
### 입력 : 첫 줄에 수열의 길이, 두번 쨰 줄에 수열이 입력
### 출력 : 첫 줄에 가장 큰 합을 출력

import sys
input = sys.stdin.readline

size = int(input())
list = input().split()
sumList = []
tempSum = 0
for i in range(size):
    if int(list[i]) < 0 :
        if tempSum != 0:
            sumList.append(tempSum)
            tempSum = 0
        sumList.append(int(list[i]))
    else :
        tempSum += int(list[i])
if tempSum != 0 :
    sumList.append(tempSum)
oneResult = [0 for i in range(len(sumList))]
twoResult = [0 for i in range(len(sumList))]
oneResult[0] = sumList[0]
case1 = max(sumList)

for i in range(1,len(sumList)):
    oneResult[i] = oneResult[i-1] + sumList[i]
    twoResult[i] = max(oneResult[i-1], twoResult[i-1] + sumList[i])


case2 = max(oneResult)
if len(sumList) == 1:
    print(max(case1,case2))
else:
    case3 = max(twoResult[1:])
    print(max(case1,case2,case3))