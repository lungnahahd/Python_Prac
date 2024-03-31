# 노드 사이의 거리 (1240)
## 골드 5

import sys
from collections import deque

input = sys.stdin.readline

cnt_node, cnt_line = list(map(int, input().split()))

result = []
graph = [[] for _ in range(cnt_node + 1)]

for _ in range(cnt_node-1):
    x, y, cost = list(map(int, input().split()))
    graph[x].append((y,cost))
    graph[y].append((x,cost))

def bfs(x,y):
    global graph, result
    visited = set()
    stack = deque([])
    stack.append((x, 0))
    visited.add(x)

    while stack:
        now_start, mid_rst = stack.popleft()
        for next_node, cost in graph[now_start]:
            if next_node not in visited:
                if next_node == y:
                    return mid_rst + cost
                else:
                    visited.add(next_node)
                    stack.append((next_node, mid_rst + cost))

for _ in range(cnt_line):
    node_one, node_two = list(map(int, input().split()))
    result.append(bfs(node_two, node_one))

for val in result:
    print(val)
