# 외판원 순회2
## 난이도 : 실버 2

import sys, heapq, copy
from collections import deque
input = sys.stdin.readline
INT_MAX = sys.maxsize

city_cnt = int(input())
location = []
cost = [[INT_MAX for _ in range(city_cnt)] for _ in range(city_cnt)]
loc_map = [[] for _ in range(city_cnt)]
for _ in range(city_cnt):
    temp = list(map(int, input().split()))
    location.append(temp)

for go in range(city_cnt):
    for end in range(city_cnt):
        if go != end:
            heapq.heappush(loc_map[go], (location[go][end],end))

def dfs(start_node):
    visited = set()
    path = deque([start_node])
    result = 0
    temp_loc_map = copy.deepcopy(loc_map)
    while path:
        now_node = path.popleft()
        visited.add(now_node)
        if len(visited) == city_cnt:
            result += location[now_node][start_node]
            return result
        while temp_loc_map[now_node]:
            temp_val, temp_node = heapq.heappop(temp_loc_map[now_node])
            if temp_node not in visited:
                result += temp_val
                visited.add(temp_node)
                path.append(temp_node)
                break

answer = INT_MAX
for idx in range(city_cnt):
    answer = min(answer, dfs(idx))
print(answer)

