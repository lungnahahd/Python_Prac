# 텀 프로젝트 (9466)
## 난이도 : 골드 3

import sys

case_cnt = int(input())
result = []


def dfs(start, graph, visited):
    next_node = graph[start] - 1
    while True:
        if visited[start]:
            return True
        if visited[next_node]:
            if visited[start]:
                return True
            else:
                return False
        visited[next_node] = True
        next_node = graph[next_node] - 1
            


for _ in range(case_cnt):
    student_cnt = int(input())
    students = list(map(int, input().split()))
    visited = [False for _ in range(student_cnt)]
    rst = 0
    for idx in range(student_cnt):
        visited = [False for _ in range(student_cnt)]
        make_team = dfs(idx, students, visited)
        if not make_team:
            rst += 1
    result.append(rst)

for not_team in result:
    print(not_team)