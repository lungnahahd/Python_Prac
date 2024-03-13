# 배 (1092)
## 난이도 : 중

import sys
import heapq

input = sys.stdin.readline

crain_cnt = int(input())
crains = list(map(int, input().split()))
crains.sort(reverse=True)
box_cnt = int(input())
temp = list(map(int, input().split()))
boxs = []
for box in temp:
    heapq.heappush(boxs, -box)

rst_time = 0

while boxs:
    for crain in crains:
        if not boxs:
            break
        if crain >= -boxs[0]:
            heapq.heappop(boxs)
        else:
            break
    
    if boxs and -boxs[0] > crains[0]:
        rst_time = -1
        break

    rst_time += 1
print(rst_time)