# 로봇 청소기 (14503)
## 난이도 : 골드 5

import sys
from collections import deque
input = sys.stdin.readline

row_size, col_size = list(map(int, input().split()))
start_row, start_col, way = list(map(int, input().split()))
visited = [[False for _ in range(col_size)] for _ in range(row_size)]

move_r = [-1,0,+1,0]
move_c = [0,-1,0,+1]


room = []
for _ in range(row_size):
    room.append(list(map(int, input().split())))

result = 1
visited[start_row][start_col] = True
go_plan = deque([(start_row, start_col, way)])

while go_plan:
    now_row, now_col, now_way = go_plan.popleft()
    isCanClean = False
    for m_idx in range(4):
        next_r, next_c = now_row + move_r[m_idx], now_col + move_c[m_idx]
        if 0 <= next_r < row_size and 0 <= next_c < col_size:
            if not visited[next_r][next_c] and room[next_r][next_c] == 0:
                isCanClean = True
                break
    if isCanClean:
        next_way = int((now_way + 1) % 4)
        next_r, next_c = now_row + move_r[next_way], now_col + move_c[next_way]
        if 0 <= next_r < row_size and 0 <= next_c < col_size:
                if not visited[next_r][next_c] and room[next_r][next_c] == 0:
                    result += 1
                    visited[next_r][next_c] = True
                    go_plan.append((next_r, next_c, next_way))
                else:
                    go_plan.append((now_row, now_col, next_way))
    else:
        next_r, next_c = now_row - move_r[now_way] , now_col - move_c[now_way]
        if 0 <= next_r < row_size and 0 <= next_c < col_size:
            if room[next_r][next_c] == 0:
                go_plan.append((next_r, next_c, now_way))
            else:
                break
        else:
            break
            

print(result)