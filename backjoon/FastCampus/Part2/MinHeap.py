# 최소 힙
## 난이도 : 하

import heapq

cnt = int(input())

save = []
result = []

for _ in range(cnt):
    num = int(input())
    if num == 0:
        if len(save) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(save))
    else:
        heapq.heappush(save, num)

for num in result:
    print(num)