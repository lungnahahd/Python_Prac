# 이분 그래프 (1707)
## 난이도 : 골드4

import sys
input = sys.stdin.readline

case_cnt = int(input())
visited = []
load_visit = set()
isCycle = False
result = []

def chkCycle(start, graph):
    global visited, load_visit, isCycle
    visited[start] = True

    for next_node in graph[start]:
        if not visited[next_node]:
            load_visit.add((min(start,next_node), max(start,next_node)))
            chkCycle(next_node, graph)
        else:
            if (min(start, next_node), max(start, next_node)) not in load_visit:
                isCycle = True
                break



for _ in range(case_cnt):
    node_cnt, line_cnt = list(map(int,input().split()))
    graph = [[] for _ in range(node_cnt+1)]
    visited = [False for _ in range(node_cnt+1)]
    load_visit.clear()
    isCycle = False
    for _ in range(line_cnt):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    for idx in range(1, node_cnt+1):
        if not visited[idx]:
            chkCycle(idx,graph)
        if isCycle:
            result.append("NO")
            break
    if not isCycle:
        result.append("YES")

for rst in result:
    print(rst)