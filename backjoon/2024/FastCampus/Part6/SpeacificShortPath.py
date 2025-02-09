# 특정한 최단 경로 (1504)
## 난이도 : 골드 4

import sys
import heapq
INT_MAX = sys.maxsize
input = sys.stdin.readline 

node_cnt, road_cnt = list(map(int,input().split()))
paths = [[] for _ in range(node_cnt+1)]

for _ in range(road_cnt):
    a, b, cost = list(map(int, input().split()))
    paths[a].append((b, cost))
    paths[b].append((a, cost))
must_visit = list(map(int, input().split()))

def short_path(start):
    global paths
    path = [INT_MAX for _ in range(node_cnt+1)]
    path[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        now_cost, now_node = heapq.heappop(hq)
        if now_cost < path[now_node]:
            continue
        for n, val in paths[now_node]:
            if path[n] > val + now_cost:
                path[n] = val + now_cost
                heapq.heappush(hq, (path[n], n))
    return path
mid_1 = short_path(must_visit[0]) 
mid_2 = short_path(must_visit[1])
mid_3 = short_path(1)
result = INT_MAX 
if (mid_1[must_visit[1]] != INT_MAX):
    temp_1 = mid_1[must_visit[1]] + mid_3[must_visit[0]] + mid_2[node_cnt]
    temp_2 = mid_3[must_visit[1]] + mid_2[must_visit[0]] + mid_1[node_cnt]
    result = min(temp_1, temp_2, result)
else:
    temp_1 = mid_3[must_visit[1]] * 2 + mid_3[must_visit[0]] * 2 + mid_3[node_cnt]
    temp_2 = mid_3[must_visit[1]] + mid_3[must_visit[0]] * 2 + mid_2[node_cnt]
    temp_3 = mid_3[must_visit[0]] + mid_3[must_visit[1]] * 2 + mid_1[node_cnt]
    result = min(temp_1, temp_2, temp_3, result)
if result == INT_MAX:
    result = -1
print(result)