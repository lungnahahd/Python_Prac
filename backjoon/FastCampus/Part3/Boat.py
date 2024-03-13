# 배 (1092)
## 난이도 : 중

import sys
import heapq
from collections import deque

input = sys.stdin.readline

crain_cnt = int(input())
crains = list(map(int, input().split()))
crains.sort(reverse=True)
box_cnt = int(input())
boxs  = list(map(int, input().split()))
boxs.sort(reverse=True)
#boxs = []

# for box in temp:
#     heapq.heappush(boxs, -box)



rst_time = 0

if boxs[0] > crains[0]:
    rst_time = -1
else:
    dq_boxs = deque(boxs)

    while dq_boxs:
        for crain in crains: 
            for box in dq_boxs:
                if crain >= box:
                    dq_boxs.popleft()
                    break
        rst_time += 1

    
print(rst_time)