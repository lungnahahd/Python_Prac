# 적록색약 (10026)
## 난이도 : 골드 5

import copy
from collections import deque

n = int(input())
grid, sick_grid = [], []
nomal_result, sick_result = 0, 0
nomal_visited = [[False for _ in range(n)] for _ in range(n)]
sick_visited  = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    temp_color = list(input())
    sick_color= copy.deepcopy(temp_color)
    grid.append(temp_color)
    for idx in range(n):
        if sick_color[idx] == 'G':
            sick_color[idx] = 'R'
    sick_grid.append(sick_color)

def bfs(grid, start_x, start_y, visited):
    move_x = [-1,0,+1,0]
    move_y = [0,+1,0,-1]
    stack = deque([(start_x, start_y)])
    color = grid[start_x][start_y]
    visited[start_x][start_y] = True
    while stack:
        now_x, now_y = stack.popleft()
        for idx in range(4):
            next_x, next_y = now_x + move_x[idx], now_y + move_y[idx]
            if 0 <= next_x < n and 0 <= next_y < n:
                if not visited[next_x][next_y] and grid[next_x][next_y] == color:
                    visited[next_x][next_y] = True
                    stack.append((next_x, next_y))

for x in range(n):
    for y in range(n):
        if not nomal_visited[x][y]:
            nomal_result += 1
            bfs(grid, x,y,nomal_visited)
        if not sick_visited[x][y]:
            sick_result += 1
            bfs(sick_grid, x,y,sick_visited)

print(nomal_result, end=' ')
print(sick_result)