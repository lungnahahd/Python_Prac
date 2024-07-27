# 주유소 (13305)
## 난이도 : 실버 3

import sys
import heapq
input = sys.stdin.readline

count_city = int(input())
road_value = list(map(int, input().split()))
oil_cost = list(map(int, input().split()))

very_cheap = []

answer = 0
for idx in range(len(road_value)):
    heapq.heappush(very_cheap, oil_cost[idx])
    now_oil = very_cheap[0]
    answer += (now_oil * road_value[idx])

print(answer)