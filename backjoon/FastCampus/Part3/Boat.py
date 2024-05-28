# 배 (1092)
## 난이도 : 골드 5

import sys
import heapq
from collections import deque

input = sys.stdin.readline

crain_cnt = int(input())
crain_list = list(map(int, input().split()))
#crain_hq = [[] for _ in range(len(crain_list))]
crain_dq = [[] for _ in range(len(crain_list))]
crain_list.sort()
box_cnt = int(input())
box_list = list(map(int,input().split()))
box_dict = dict()

max_box = -1

for box in box_list:
    max_box = max(max_box, box)
    if box in box_dict:
        box_dict[box] += 1
    else:
        box_dict[box] = 1
    for idx in range(len(crain_list)):
        if box <= crain_list[idx]:
            crain_dq[idx].append(box)
            #heapq.heappush(crain_hq[idx], -box)

for idx in range(len(crain_list)):
    crain_dq[idx].sort()
    #crain_dq[idx] = deque(crain_dq[idx])

if max_box > crain_list[-1]:
    print(-1)
else:
    count = 0
    time = 0
    while count < box_cnt:
        for idx in range(crain_cnt):
            while crain_dq[idx]:
                now_weight = crain_dq[idx].pop()
                #now_weight = heapq.heappop(crain_hq[idx])
                #now_weight = -now_weight
                if box_dict[now_weight] != 0:
                    box_dict[now_weight] -= 1
                    count += 1
                    break
        time += 1
    print(time)