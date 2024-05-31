# 보석 도둑 (1202)
## 난이도 : 골드 2

import sys
import heapq
input = sys.stdin.readline

cnt_jewery, cnt_bag = list(map(int, input().split()))

jewery_save = []
bag_save = []
temp_steal = []

for _ in range(cnt_jewery):
    weight, cost = list(map(int, input().split()))
    heapq.heappush(jewery_save, (-cost, -weight))

for _ in range(cnt_bag):
    size = int(input())
    heapq.heappush(bag_save, size)

for _ in range(cnt_bag):
    cost, weight = heapq.heappop(jewery_save)
    heapq.heappush(temp_steal, (-weight, cost))

result = 0
while bag_save:
    now_weight, now_cost = heapq.heappop(temp_steal)
    if bag_save[0] >= now_weight:
        result += (-now_cost)
        heapq.heappop(bag_save)
    else:
        append_cost, append_weight = heapq.heappop(jewery_save)
        heapq.heappush(temp_steal, (-append_weight, append_cost))
print(result)