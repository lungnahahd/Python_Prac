# 배열 추출
## 우선순위 큐를 사용 이유 : 빠르게 최대값을 찾기 위해 우선순위 큐를 사용

import heapq

heapArr = []
cmdCount = int(input())
for i in range(cmdCount):
    cmd = int(input())
    if cmd == 0:
        if not heapArr:
            print(0)
        else:
            out = heapq.heappop(heapArr)
            print(-out)
    else:
        heapq.heappush(heapArr, -cmd)