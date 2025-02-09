# DFS와 BFS (1260)
## 난이도 : 하

import sys
import heapq
from collections import deque
input = sys.stdin.readline

cnt_node, cnt_line, start_node = list(map(int, input().split()))
bfs_graph = [[] for _ in range(cnt_node+1)]
dfs_graph = [[] for _ in range(cnt_node+1)]
dfs_visited = [False for _ in range(cnt_node+1)]
bfs_visited = [False for _ in range(cnt_node+1)]

for _ in range(cnt_line):
    a_node, b_node = list(map(int, input().split()))
    heapq.heappush(dfs_graph[a_node], b_node)
    heapq.heappush(dfs_graph[b_node], a_node)
    heapq.heappush(bfs_graph[a_node], b_node)
    heapq.heappush(bfs_graph[b_node], a_node)

dfs_rst = []

def dfs(start_node):
    global dfs_visited
    global dfs_graph
    global dfs_rst

    if not dfs_visited[start_node]:
        dfs_rst.append(str(start_node))
        dfs_visited[start_node] = True
        for _ in range(len(dfs_graph[start_node])):
            next_node = heapq.heappop(dfs_graph[start_node])
            if not dfs_visited[next_node]:
                dfs(next_node)
    return dfs_rst

def bfs(start_node):
    global bfs_visited
    global bfs_graph

    temp = deque([start_node])
    bfs_visited[start_node] = True
    result = [str(start_node)]

    while temp:
        now_node = temp.popleft()
        for _ in range(len(bfs_graph[now_node])):
            next_node = heapq.heappop(bfs_graph[now_node])
            if not bfs_visited[next_node]:
                bfs_visited[next_node] = True 
                temp.append(next_node)
                result.append(str(next_node))
    return result

print(' '.join(dfs(start_node)))
print(' '.join(bfs(start_node)))