# 연속합
## 임의의 수열이 제공되며 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 가장 큰 합을 구하기
### 입력 : 첫 줄에 정수의 크기가 입력되고, 두번 째 줄에는 수열이 입력
### 출력 : 첫 줄에 연속 수열 합의 최대가 출력

import sys
input = sys.stdin.readline

size = int(input())
get = input().split()
numList = []
for i in get:
    numList.append(int(i))

sumList = []
sumList.append(numList[0])
for i in range(1,size):
    before = sumList[i-1]
    after = before + numList[i]
    sumList.append(after)


standard = sumList.index(max(sumList))
result = sumList[standard]
for i in range(standard):
    if sumList[standard] < 0:
        check = result - sumList[standard]
        if result < check:
            result = check

print(result)  