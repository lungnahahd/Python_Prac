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
box_can_crain_cnt = [0 for _ in range(crain_cnt)]

for box in box_list:
    if box in box_dict:
        box_dict[box] += 1
    else:
        box_dict[box] = 1
    for idx in range(len(crain_list)):
        if box <= crain_list[idx]:
            box_can_crain_cnt[idx] += 1

print(box_can_crain_cnt)

time = 0
end_box = 0
for idx in range(crain_cnt):
    remain = crain_cnt - idx
    now_box = box_can_crain_cnt[idx] - end_box
    if remain == 1:
        time += now_box
        break
    time += (now_box // remain)
    end_box += (now_box// remain) * remain
    if end_box >= box_cnt:
        break
print(time)