# 뿌요뿌요 (11559)
## 난이도 : 골드 4


import sys
from collections import deque
input = sys.stdin.readline


# 세로 12 줄, 각 줄에 6개 
puyo_map = []
for _ in range(12):
    line = list(input())
    puyo_map.append(line)

move_r = [-1,0,+1,0]
move_c = [0,-1,0,+1]

def get_rid_puyo(start_row, start_col):
    visited = [[False for _ in range(6)] for _ in range(12)] # 뿌요뿌요 방문 여부를 확인하는 배열

    cnt = 1
    now_color = puyo_map[start_row][start_col]
    visited.append((start_row, start_col))
    puyos = deque([(start_row, start_col)])
    while puyos:
        now_r, now_c = puyos.popleft()
        for idx in range(4):
            next_r, next_c = now_r + move_r[idx], now_c + move_c[idx]
            if (0 <= next_r < 12 and 0 <= next_c < 6):
                if (next_r, next_c) not in visited and now_color == puyo_map[next_r][next_c]:
                    cnt += 1
                    visited.append((next_r, next_c))
                    puyos.append((next_r, next_c))
