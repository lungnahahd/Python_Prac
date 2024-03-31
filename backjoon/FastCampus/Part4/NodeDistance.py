# 노드 사이의 거리 (1240)
## 골드 5

import sys
from collections import deque

input = sys.stdin.readline

cnt_node, cnt_line = list(map(int, input().split()))

result = []
graph = [[0 for _ in range(cnt_node + 1)] for _ in range(cnt_node + 1)]

for _ in range(cnt_node-1):
    x, y, cost = list(map(int, input().split()))
    graph[x][y] = cost
    graph[y][x] = cost

def bfs(x,y):
    global graph, result
    visited = set()
    stack = deque([])
    stack.append((x, 0))

    while stack:
        now_start, mid_rst = stack.popleft()
        for idx in range(1, cnt_node+1):
            if graph[now_start][idx] != 0:
                if idx == y:
                    return mid_rst + graph[now_start][idx]
                else:
                    if idx not in visited:
                        stack.append((idx, mid_rst + graph[now_start][idx]))
        visited.add(now_start)

for _ in range(cnt_line):
    node_one, node_two = list(map(int, input().split()))
    result.append(bfs(min(node_one, node_two), max(node_one, node_two)))

for val in result:
    print(val)
