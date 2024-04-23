# 보석 도둑 (1202)
## 난이도 : 골드 2

import sys
import heapq
input = sys.stdin.readline


cnt_jwery, cnt_bag = list(map(int, input().split()))
jwery, bag = [], []

for _ in range(cnt_jwery):
    weight, cost = list(map(int, input().split()))
    heapq.heappush(jwery, (weight, cost))

for _ in range(cnt_bag):
    size = int(input())
    bag.append(size)
    #heapq.heappush(bag, -size)

bag.sort()
result = 0
temp = []


for size in bag:
    while len(jwery) !=0 and jwery[0][0] <= size:
        now_weight, now_cost = heapq.heappop(jwery)
        heapq.heappush(temp, (-now_cost, -now_weight))
    out_cost, _ = heapq.heappop(temp)
    result += (-out_cost)
    while temp:
        in_cost, in_weight = heapq.heappop(temp)
        heapq.heappush(jwery, (-in_weight, -in_cost))
    
print(result)