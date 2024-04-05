# 트리 (4803)
## 난이도 : 골드 4

import sys
input = sys.stind.readline

def cnt_tree(gp):
    cnt = 0
    stack = []



    return cnt


while True:
    node_cnt, line_cnt = list(map(int, input().split()))
    cnt = 1
    if node_cnt == 0 and line_cnt == 0:
        break
    graph = [[] for _ in range(node_cnt+1)]
    for idx in range(line_cnt):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
