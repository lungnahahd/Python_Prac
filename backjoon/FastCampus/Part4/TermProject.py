# 텀 프로젝트 (9466)
## 난이도 : 골드 3

import sys

case_cnt = int(input())
result = []
cycle_member = set()
isCycle = False


def dfs(start, graph, cycle_mother):
    global cycle_member, visited, isCycle, finished
    
    visited[start] = True
    next_node = graph[start] - 1
    if not visited[next_node]:
        visited[next_node] = True
        isCycle = False
        dfs(next_node, graph, cycle_mother)
    else:
        if not isCycle:
            if next_node == start:
                cycle_member.add(next_node)
                finished[next_node] = True
            else:
                isCycle = True
                dfs(next_node, graph, next_node)
        else:
            cycle_member.add(next_node)
            if (next_node == cycle_mother):
                finished[next_node] = True
                isCycle = False
            else:
                if not finished[next_node]:
                    finished[next_node] = True
                    dfs(next_node, graph, cycle_mother)

for _ in range(case_cnt):
    student_cnt = int(input())
    students = list(map(int, input().split()))
    visited = [False for _ in range(student_cnt)]
    finished = [False for _ in range(student_cnt)]
    for idx in range(student_cnt):
        if not visited[idx]:
            dfs(idx, students, -1)
        
    result.append(student_cnt - len(cycle_member))
    cycle_member.clear()

for rst in result:
    print(rst)