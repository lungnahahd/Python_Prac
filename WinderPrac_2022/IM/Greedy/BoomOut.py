# 폭탄 해체 작업

import heapq

caseSize = int(input())

lBoom = []
maxTime = -1

for _ in range(caseSize):
    get = list(map(int, input().split()))
    heapq.heappush(lBoom,(-get[1],-get[0]))
    maxTime = max(maxTime,get[1])

eTime = maxTime
saveBoom = []
lTime = [i for i in range(caseSize + 1)]
result = 0
nowTime = True

while eTime != 0 :
    while lBoom and -lBoom[0][0] >= eTime:
        nTime,nScore = heapq.heappop(lBoom)
        nTime,nScore = -nTime, -nScore
        saveBoom.append(nScore)
    if len(saveBoom) != 0:
        big = max(saveBoom)
        result += big
        saveBoom.remove(big)
    eTime -= 1

print(result)