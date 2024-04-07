# 텀 프로젝트 (9466)
## 난이도 : 골드 3

import sys

case_cnt = int(input())
result = []
cycle_member = set()



def dfs(start, graph):
    global cycle_member, visited
    stack = []
    stack.append((start,start))
    isCycle = False
    cycle_mother = -1
    while stack:
        node, mother = stack.pop()
        next_node = graph[node] - 1
        if not visited[next_node]:
            stack.append((next_node, node))
            visited[next_node] = True
        else:
            if not isCycle:
                if next_node == node:
                    cycle_member.add(next_node)
                else:
                    isCycle = True
                    cycle_member.add(next_node)
                    cycle_mother = next_node
            else:
                if cycle_mother == next_node:
                    isCycle = False    
                cycle_member.add(next_node)
                


for _ in range(case_cnt):
    student_cnt = int(input())
    students = list(map(int, input().split()))
    visited = [False for _ in range(student_cnt)]
    rst = 0
    for idx in range(student_cnt):
        if not visited[idx]:
            dfs(idx, students)
            print(cycle_member)
    cycle_member.clear()