# 알고스팟 (1261)
## 난이도 : 골드 4

import sys
from collections import deque
input = sys.stdin.readline

col_cnt, row_cnt = list(map(int, input().split()))
maze = []
move_r = [1,0,-1,0]
move_c = [0,1,0,-1]
answer = sys.maxsize
for idx in range(row_cnt):
    temp = list(input())
    maze.append(temp[:-1])

def bfs():
    global answer
    visited = [[sys.maxsize for _ in range(col_cnt)] for _ in range(row_cnt)]
    
    path = deque([(0,0,0)])
    visited[0][0] = 0
    while path:
        now_row, now_col, now_val = path.popleft()
        if now_row == row_cnt -1 and now_col == col_cnt -1:
            answer = min(answer, now_val)
        
        for move_idx in range(4):
            next_row, next_col = now_row + move_r[move_idx], now_col + move_c[move_idx]
            if 0 <= next_row < row_cnt and 0 <= next_col < col_cnt:
                if maze[next_row][next_col] == '0':
                    if visited[next_row][next_col] > now_val:
                        visited[next_row][next_col] = now_val
                        path.append((next_row, next_col, now_val))
                else:
                    if visited[next_row][next_col] > now_val + 1:
                        visited[next_row][next_col] = now_val + 1
                        path.append((next_row,next_col, now_val+1))

bfs()
print(answer)