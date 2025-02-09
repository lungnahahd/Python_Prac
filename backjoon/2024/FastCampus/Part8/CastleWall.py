# 성곽 (2234)
## 난이도 : 골드 3

import sys
from collections import deque
input = sys.stdin.readline

col, row = list(map(int, input().split()))
castle = []
visited = [[False for _ in range(col)] for _ in range(row)]

move_row = [1,0,-1,0]
move_col = [0,1,0,-1]

for _ in range(row):
    castle.append(list(map(int, input().split())))
    
def check_not_wall(cost, location):
    bin_value = bin(cost)[2:]
    bin_value = ('0' * (4-len(bin_value)) + bin_value)
    if bin_value[location] == '0':
        return True
    else:
        return False



def bfs(r, c):
    global visited, path
    visited[r][c] = True
    can_go = deque([(r,c)])
    cost = 1
    while can_go:
        now_r, now_c = can_go.popleft()
        for idx in range(4):
            next_r, next_c = now_r + move_row[idx], now_c + move_col[idx]
            if 0 <= next_r < row and 0 <= next_c < col and not visited[next_r][next_c]:
                if check_not_wall(castle[now_r][now_c], idx):
                    visited[next_r][next_c] = True
                    can_go.append((next_r, next_c))
                    path.append((next_r, next_c))
                    cost += 1
    return cost
room_cnt = 0
room_size = 0
remove_wall_room_size = 0
for r_idx in range(row):
    for c_idx in range(col):
        path = []
        if not visited[r_idx][c_idx]:
            path.append((r_idx, c_idx))
            now_cost = bfs(r_idx, c_idx)
            room_size = max(now_cost, room_size)
            room_cnt += 1
            for chg_r, chg_c in path:
                castle[chg_r][chg_c] = (now_cost, room_cnt)
for r_idx in range(row):
    for c_idx in range(col):
        for m_idx in range(4):
            next_r_idx, next_c_idx = r_idx + move_row[m_idx], c_idx + move_col[m_idx]
            if 0 <= next_r_idx < row and 0 <= next_c_idx < col:
                if castle[next_r_idx][next_c_idx][1] != castle[r_idx][c_idx][1]:
                    remove_wall_room_size = max(remove_wall_room_size, castle[next_r_idx][next_c_idx][0] + castle[r_idx][c_idx][0])

print(room_cnt)
print(room_size)
print(remove_wall_room_size)