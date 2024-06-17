# 이분 그래프 (1707)
## 난이도 : 골드4

import sys
from collections import deque
input = sys.stdin.readline



def bfs(start_num, visited):
    result = True
    
    save = deque([(start_num,-1)])
    visited[start_num] = -1
    next_val = 0
    while save:
        now_node, val = save.popleft()
        for num in graph[now_node]:
            if visited[num] == 0:
                visited[num] = -val
                save.append((num, -val))
            else:
                if visited[num] == val:
                    result = False
                    save.clear()
                    break
    return result

case_cnt = int(input())
for _ in range(case_cnt):
    node_cnt, line_cnt = list(map(int, input().split()))
    visited = [0 for _ in range(node_cnt+1)]
    graph = [[] for _ in range(node_cnt+1)]
    for _ in range(line_cnt):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    result = bfs(1, visited)
    if result:
        print("YES")
    else:
        print("NO")
