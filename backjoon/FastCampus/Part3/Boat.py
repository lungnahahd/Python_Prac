# 배 (1092)
## 난이도 : 골드 5

import sys
import heapq
from collections import deque

input = sys.stdin.readline

crain_cnt = int(input())
crain_list = list(map(int, input().split()))
crain_hq = [[] for _ in range(len(crain_list))]
crain_list.sort()
box_cnt = int(input())
box_list = list(map(int,input().split()))
box_dict = dict()


for box in box_list:
    if box in box_dict:
        box_dict[box] += 1
    else:
        box_dict[box] = 1
    for idx in range(len(crain_list)):
        if box <= crain_list[idx]:
            heapq.heappush(crain_hq[idx], -box)

count = 0
time = 0
while count < box_cnt:
    for idx in range(crain_cnt):
        while crain_hq[idx]:
            now_weight = heapq.heappop(crain_hq[idx])
            now_weight = -now_weight
            if box_dict[now_weight] != 0:
                box_dict[now_weight] -= 1
                count += 1
                break
    time += 1
print(time)