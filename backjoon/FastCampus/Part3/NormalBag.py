# 평범한 배낭 (12865)
## 난이도 : 하

# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

import sys
import heapq

case, max_weight = list(map(int, input().split()))

temp = []

for _ in range(case):
    weight, cost = list(map(int, input().split()))
    heapq.heappush(temp, (cost, weight))

result = 0

while temp:
    now_cost, now_weight = heapq.heappop(temp)

    for cost, weight in temp:
        if now_weight + weight <= max_weight:
            now_weight += weight
            now_cost += cost
    result = max(now_cost, result)

print(result)