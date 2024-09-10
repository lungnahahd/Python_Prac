# 정육점 (2258)
## 난이도 : 골드 4

import sys
import heapq
input = sys.stdin.readline 

house_cnt, want_weight = list(map(int, input().split()))

house = []
stack_house = []
stack_weight = 0
for _ in range(house_cnt):
    weight, cost = list(map(int, input().split()))
    heapq.heappush(house, (cost, weight))

for cost, weight in house:
    stack_weight += weight
    heapq.heappush(stack_house, (stack_weight, cost))

answer = 0
while stack_house:
    now_weight, now_cost = heapq.heappop(stack_house)
    if now_weight >= want_weight:
        answer = now_cost
        break
if now_cost == 0:
    print(-1)
else:
    print(answer)