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
        if go != end and location[go][end] != 0:
            loc_map[go].append((end, location[go][end]))

def dfs(start_node, now_node, visited, value):
    global temp
    if len(visited) == city_cnt-1 :
            if location[now_node][start_node] != 0:
                temp = min(temp, value + location[now_node][start_node])
    else:
        for next_node, next_val in loc_map[now_node]:
            if next_node not in visited and next_node != start_node:
                visited.add(next_node)
                dfs(start_node, next_node, visited, value + next_val)
                visited.remove(next_node)


answer = INT_MAX
for idx in range(city_cnt):
    temp = INT_MAX
    dfs(idx, idx, set(), 0)
    answer = min(answer, temp)
print(answer)

