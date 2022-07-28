# 폭탄 해체 작업

import heapq

caseSize = int(input())

lBoom = []

for _ in range(caseSize):
    get = list(map(int, input().split()))
    heapq.heappush(lBoom,(-get[0],-get[1]))

sTime = 0
eTime = 0
lTime = [i for i in range(caseSize + 1)]
result = 0

while lBoom:
    nScore,nTime = heapq.heappop(lBoom)
    nScore,nTime = -nScore,-nTime
    if result == 0:
        result += nScore
        eTime = nTime-1
    else:
        if eTime > nTime:
            result += nScore
