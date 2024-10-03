# 최단거리

import sys

INT_MAX = sys.maxsize
input = sys.stdin.readline

node_cnt, case_cnt = list(map(int, input().split()))
time_table = [[] for _ in range(node_cnt + 1)]
dist_table = [[INT_MAX for _ in range(node_cnt+1)] for _ in range(node_cnt+1)]

# 플로이드에서 사용할 2차원 배열
for i in range(1, node_cnt+1):
    dist_table[i][i] = 0

# 초기에 값을 받는 부분
for idx in range(node_cnt):
    temp = list(map(int, input().split()))
    for t_idx in range(node_cnt):
        dist_table[idx+1][t_idx+1] = temp[t_idx]

for k in range(1, node_cnt+1):
    for i in range(1, node_cnt+1):
        for j in range(1, node_cnt+1):
            dist_table[i][j] = min(dist_table[i][j], dist_table[i][k] + dist_table[k][j])


for _ in range(case_cnt):
    start, end = list(map(int, input().split()))
    print(dist_table[start][end])