# 상한 귤

import sys
from collections import deque
input = sys.stdin.readline

INT_MAX = sys.maxsize

move_r = [1,0,-1,0]
move_c = [0,1,0,-1]

map_size, ripe_cnt = list(map(int, input().split()))
place = []
ripe = []

answer = [[INT_MAX for _ in range(map_size)] for _ in range(map_size)]
for r_idx in range(map_size):
    temp = list(map(int, input().split()))
    place.append(temp)
    for c_idx in range(map_size):
        if temp[c_idx] == 2:
            ripe.append((r_idx, c_idx, 0))
            answer[r_idx][c_idx] = 0


ripe = deque(ripe)

while ripe:
    now_r, now_c, now_time = ripe.popleft()
    for m_idx in range(4):
        next_r, next_c = now_r + move_r[m_idx], now_c + move_c[m_idx]
        if 0 <= next_r < map_size and 0 <= next_c < map_size:
            if place[next_r][next_c] != 0 and answer[next_r][next_c] > now_time + 1:
                answer[next_r][next_c] = now_time + 1
                ripe.append((next_r, next_c, now_time + 1))


for r_idx in range(map_size):
    for c_idx in range(map_size):
        if answer[r_idx][c_idx] == INT_MAX:
            print(-1, end= ' ')
        else:
            print(answer[r_idx][c_idx], end= ' ')
    print()
