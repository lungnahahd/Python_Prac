# 도로 포장 (1162)
## 난이도 : 플레티넘 5

import sys
import heapq
import copy
input = sys.stdin.readline

cnt_city, cnt_way, make_road = list(map(int, input().split()))
jun_map = [[] for _ in range(cnt_city+1)]
visited = set()
visited.add(1)
result = sys.maxsize

for _ in range(cnt_way):
    a, b, time = list(map(int, input().split()))
    jun_map[a].append((b,time))
    jun_map[b].append((a,time))


def dfs(start, mid, mid_sum):
    global visited, result

    if start == cnt_city:
        temp = copy.deepcopy(mid)
        heapq.heapify(temp)
        for _ in range(make_road):
            mid_sum = mid_sum + heapq.heappop(temp)
        result = min(result, mid_sum)


    for next_city, time in jun_map[start]:
        if next_city not in visited:
            visited.add(next_city)
            mid.append(-time)
            dfs(next_city, mid, mid_sum + time)
            mid.pop()
            visited.remove(next_city)

dfs(1,[], 0)
print(result)
