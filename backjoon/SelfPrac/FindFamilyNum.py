# 촌수계산 (2644)
## 난이도 : 실버 2

import sys 
from collections import deque
input = sys.stdin.readline

people_num = int(input())
start, end = list(map(int, input().split()))
case_num = int(input())
graph = [[] for _ in range(people_num+1)]

for _ in range(case_num):
    mother, sun = list(map(int, input().split()))
    graph[mother].append(sun)
    graph[sun].append(mother)

def dfs():
    global start, end
    visited = [False for _ in range(people_num+1)]
    save = deque([(start,0)])
    visited[start] = True
    while save:
        now_node, point  = save.popleft()
        for node in graph[now_node]:
            if node == end :
                return point + 1
            if not visited[node]:
                visited[node] = True
                save.append((node, point+1))

    return -1
answer = dfs()
print(answer)