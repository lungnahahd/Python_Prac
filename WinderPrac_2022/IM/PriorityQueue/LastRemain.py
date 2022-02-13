# 마지막으로 남은 숫자
## n개의 숫자가 주어졌을 때 가장 큰 숫자 2개를 뽑아 제거하고 두 숫자의 차이에 해당하는 숫자를 다시 집어넣는 것을 2개 이상의 숫자가 남아 있는 한 계속 반복하려고 합니다
##  만약 뽑은 가장 큰 숫자 2개가 동일하다면, 이 경우에는 차이가 0이기 때문에 새롭게 집어넣지 않는다고 합니다.
##  이 과정을 진행한 이후 마지막으로 남게되는 숫자를 구하는 프로그램을 작성해보세요.
### 우선순위 큐 사용 이유 : 계속 최대값을 뽑는 과정을 빠르게 반복해야되므로 사용

import heapq

numArr = []
size = int(input())
numList = list(map(int, input().split()))

for i in numList:
    heapq.heappush(numArr,-i)

while len(numArr) >= 2:
    outA = heapq.heappop(numArr)
    outB = heapq.heappop(numArr)
    differ = abs(outA) - abs(outB)
    if differ != 0:
        heapq.heappush(numArr, -differ)

if numArr:
    print(-numArr[0])
else:
    print(-1)