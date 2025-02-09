# 방번호 (1082)
## 난이도 : 골드 3

import sys
import heapq
input = sys.stdin.readline

num_cnt = int(input())
num_list = list(map(int, input().split()))
now_money = int(input())
cost_list = ['' for _ in range(now_money+1)]
sort_list = []
for idx in range(len(num_list)):
    now_idx = num_list[idx] * num_cnt
    if now_idx <= now_money+1:
        cost_list[now_idx] = str(num_list[idx]) * num_cnt    
    heapq.heappush(sort_list,(num_list, idx))

while sort_list:
    now_cost, now_num = heapq.heappop(sort_list)
    