# 보석 도둑 (1202)
## 난이도 : 골드 2

import sys
import heapq
input = sys.stdin.readline


cnt_jwery, cnt_bag = list(map(int, input().split()))
jwery, bag = [], []

for _ in range(cnt_jwery):
    weight, cost = list(map(int, input().split()))
    heapq.heappush(jwery, (-cost, -weight))

for _ in range(cnt_bag):
    size = int(input())
    heapq.heappush(bag, -size)

result = 0
while bag and jwery:
    now_size = heapq.heappop(bag)
    now_size = -(now_size)
    while jwery:
        now_cost, now_weight = heapq.heappop(jwery)
        now_weight = -(now_weight)
        now_cost = -(now_cost)
        if now_weight <= now_size:
            result += now_cost
            break
print(result)