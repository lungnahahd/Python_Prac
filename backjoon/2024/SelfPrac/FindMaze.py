# 미로 탐색 (2178)
## 난이도 : 실버 1

import sys
from collections import deque
input = sys.stdin.readline

row_size, col_size = list(map(int, input().split()))
maze = []
move_r = [0,+1,0,-1]
move_c = [-1,0,+1,0]

for _ in range(row_size):
    now_value = list(map(int, list(input())[:-1]))
    maze.append(now_value)

def bfs(r,c):
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    visited[r][c] = True
    save = deque([(r,c, 1)])
    while save:
        now_r, now_c, now_cost = save.popleft()
        for idx in range(4):
            next_r, next_c = now_r + move_r[idx] , now_c + move_c[idx]
            if next_r == row_size - 1 and next_c == col_size - 1:
                return now_cost + 1
            if 0 <= next_r < row_size and 0 <= next_c < col_size:
                if maze[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    save.append((next_r, next_c, now_cost + 1))

print(bfs(0,0))