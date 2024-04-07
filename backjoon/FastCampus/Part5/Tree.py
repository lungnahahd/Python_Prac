# 트리 (4803)
## 난이도 : 골드 4

import sys
input = sys.stdin.readline
cnt = 0
case_cnt = 1
isCycle = False
result = []

def chk_tree(start, visited, save):
    global cnt, isCycle
    for idx in graph[start]:
        if not visited[idx]:
            visited[idx]  = True
            road.add((min(start,idx), max(start,idx)))
            save.add(idx)
            chk_tree(idx, visited, save)
        else:
            if ((min(start,idx), max(start,idx)) not in road):
                isCycle = True
                road.add((min(start,idx), max(start,idx)))
            

while True:
    node_cnt, line_cnt = list(map(int, input().split()))

    if node_cnt == 0 and line_cnt == 0:
        break
    graph = [[] for _ in range(node_cnt+1)]
    for idx in range(line_cnt):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    stack = []
    save, road = set(),set()
    cnt = 0
    mid_rst = 0
    visited = [False for _ in range(len(graph))]
    for idx in range(1, node_cnt+1):
        isCycle = False
        save.clear()
        if not visited[idx]:
            visited[idx]
            chk_tree(idx, visited, save)
            if  not isCycle:
                mid_rst += 1
    if mid_rst == 0:
        temp = "Case " + str(case_cnt) + ": No trees."
    elif mid_rst == 1:
        temp = "Case " + str(case_cnt) + ": There is one tree."
    else:
        temp = "Case " + str(case_cnt) + ": A forest of " + str(mid_rst) + " trees."
    result.append(temp) 
    case_cnt += 1

for rst in result:
    print(rst)