# 보석 도둑 (1202)
## 난이도 : 골드 2

import sys
import heapq
input = sys.stdin.readline

cnt_jewery, cnt_bag = list(map(int, input().split()))

jewery_save = []
jewery_dict = dict()
bag_save = []
temp_steal = []

for _ in range(cnt_jewery):
    weight, cost = list(map(int, input().split()))
    heapq.heappush(jewery_save, (-cost, -weight))
    temp_key = str(weight) + str(cost)
    if temp_key in jewery_dict:
        jewery_dict[temp_key] += 1
    else:
        jewery_dict[temp_key] = 1

for _ in range(cnt_bag):
    size = int(input())
    bag_save.append(size)
bag_save.sort()

can_steal = [[] for _ in range(len(bag_save))]
result = 0
visited = set()
while jewery_save:
    cost, weight = heapq.heappop(jewery_save)
    for bag_idx in range(len(bag_save)):
        if bag_idx not in visited and  bag_save[bag_idx] >= -weight:
            result += (-cost)
            visited.add(bag_idx)
            break
    if len(visited) == cnt_bag:
        break

print(result)