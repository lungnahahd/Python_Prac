# 벽 부수고 이동하기 (2206)
## 난이도 : 골드 3

import sys
from collections import deque

row_size, col_size = list(map(int, input().split()))
maze = []
visited = [[False for _ in range(col_size)] for _ in range(row_size)]
for _ in range(row_size):
    maze.append(list(input()))

r_move = [0,+1,0,-1]
c_move = [-1,0,+1,0]

answer = sys.maxsize

def dfs_use_queue(start_r, start_c, now_maze):
    global answer, maze
    local_visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    local_visited[start_r][start_c] = True
    go_dq = deque([(start_r, start_c, 1)])
    while go_dq:
        now_row, now_col, now_dist = go_dq.popleft()
        for move in range(4):
            next_row, next_col = now_row + r_move[move], now_col + c_move[move]
            if next_row == row_size - 1 and next_col == col_size - 1:
                return now_dist + 1
            if 0 <= next_row < row_size and 0 <= next_col < col_size:
                if now_maze[next_row][next_col] == "0" and  not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    go_dq.append((next_row, next_col, now_dist + 1))
    return sys.maxsize

answer = min(answer, dfs_use_queue(0,0,maze))
for row in range(row_size):
    for col in range(col_size):
        if maze[row][col] == "1":
            maze[row][col] = "0"
            answer = min(answer, dfs_use_queue(0,0,maze))
            maze[row][col] = "1"





def dfs(row, col, now_maze, visited, isRemove, dist):
    global answer
    for idx_move in range(4):
        next_r, next_c = row + r_move[idx_move], col + c_move[idx_move]
        if 0 <= next_r < row_size and 0 <= next_c < col_size:
            if next_r == row_size - 1 and next_c == col_size - 1:
                answer = min(answer, dist+1)
                continue
            if visited[next_r][next_c]:
                continue
            if maze[next_r][next_c] == "0":
                visited[next_r][next_c] = True
                dfs(next_r, next_c, now_maze, visited, isRemove, dist+1)
                visited[next_r][next_c] = False
            else:
                if isRemove:
                    continue
                now_maze[next_r][next_c] = "0"
                visited[next_r][next_c] = True
                dfs(next_r, next_c, now_maze, visited, True, dist+1)
                now_maze[next_r][next_c] = "1"
                visited[next_r][next_c] = False
            


#dfs(0,0,maze,visited, False, 1)
if answer == sys.maxsize:
    answer = -1
print(answer)
