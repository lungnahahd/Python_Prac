# 유기농배추 (1012)
## 난이도 : 하

import sys
from collections import deque

input = sys.stdin.readline

case_cnt = int(input())
d_row = [1,0,-1,0]
d_col = [0,1,0,-1]

answer = []

def bfs(start, visited, ground):
    temp = deque([start])
    while temp:
        row, col = temp.popleft()
        visited[row][col] = True
        for idx in range(4):
            now_row, now_col = row + d_row[idx], col + d_col[idx]
            if ((0<= now_row < len(ground)) and (0<= now_col < len(ground[0])) and ground[now_row][now_col] == 1):
                if (not visited[now_row][now_col]):
                    temp.append((now_row, now_col))
    return visited



for _ in range(case_cnt):
    col, row, cnt_cabbage = list(map(int, input().split()))     # 가로, 세로, 배추 갯수
    ground = [[0 for _ in range(col)] for _ in range(row)]  # 땅을 의미하는 리스트
    visited = [[False for _ in range(col)] for _ in range(row)] # 방문 여부를 나타낼 리스트
    result = 0

    for _ in range(cnt_cabbage):
        col_cabbage, row_cabbage = list(map(int, input().split()))
        ground[row_cabbage][col_cabbage] = 1

    for r in range(row):
        for c in range(col):
            if(ground[r][c] == 1 and not visited[r][c]):
                visited = bfs((r,c), visited, ground)
                result += 1

    answer.append(str(result))

for rst in answer:
    print(rst)