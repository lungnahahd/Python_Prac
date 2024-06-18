# 사이클게임 (20040)
## 난이도 : 골드 4

import sys
from collections import deque
input = sys.stdin.readline

node_cnt, line_cnt = list(map(int, input().split()))
visited = [False for _ in range(node_cnt)]
graph = [[] for _ in range(node_cnt)]


def check_cicle(start, mother):
    global visited
    visited[start] = True
    isCycle = False
    result = -1
    save = deque([start])
    mother[start] = start
    while save:
        now_node = save.popleft()
        for next_node, step in graph[now_node]:
            if visited[next_node]:
                if mother[now_node] != next_node:
                    result = max(result, step)
                    isCycle = True
            else:
                visited[next_node] = True
                result = max(result, step)
                mother[next_node] = now_node
                save.append(next_node)
    if not isCycle:
        result = -1 
    return result


for idx in range(line_cnt):
    a,b = list(map(int, input().split()))
    graph[a].append((b,idx+1))
    graph[b].append((a,idx+1))

answer = -1
for node in range(node_cnt):
    if not visited[node]:
        mother = [-1 for _ in range(node_cnt)]
        temp_answer = check_cicle(node, mother)
    if temp_answer != -1:
        if answer == -1:
            answer = temp_answer
        else:
            answer = min(answer, temp_answer)
if answer == -1:
    print(0)
else:
    print(answer)