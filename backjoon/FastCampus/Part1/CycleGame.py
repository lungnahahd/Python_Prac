# 사이클게임 (20040)
## 난이도 : 골드 4

import sys
from collections import deque
input = sys.stdin.readline
node_cnt, line_cnt = list(map(int, input().split()))
mother = [idx for idx  in range(node_cnt)]
graph = [[] for _ in range(node_cnt)]
visited = [False for _ in range(node_cnt)]

def change_mother(max_n, min_n):
    global mother
    mother[max_n] = min_n

def find_mother(node):
    if node == mother[node]:
        return node
    else:
        return find_mother(mother[node])

for step in range(line_cnt):
    a, b = list(map(int, input().split()))
    max_num = max(a,b)
    min_num = min(a,b)
    graph[min_num].append((max_num, step+1))
    change_mother(max_num, min_num)

for num in range(node_cnt):
    mother[num] = find_mother(num)

def find_cycle(start):
    global visited
    visited[start] = True
    save = deque([start])
    result = -1
    isCylce = False
    while save:
        now_node = save.popleft()
        for next_node, step in graph[now_node]:
            if not visited[next_node]:
                result = max(result, step)
                visited[next_node] = True
                save.append(next_node)
            else:
                if mother[now_node] == mother[next_node]:
                    result = max(result, step)
                    isCylce = True
    if not isCylce:
        result = -1
    return result

answer = 0
for num in range(node_cnt):
    if not visited[num]:
        temp = find_cycle(num)
        if temp != - 1 :
            if answer == 0:
                answer = temp
            else:
                answer = min(answer, temp)
print(answer)