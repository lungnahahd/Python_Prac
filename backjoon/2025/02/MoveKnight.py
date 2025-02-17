# 나이트의 이동 (7562)
## 난이도 : 실버 1

import sys
from collections import deque
input = sys.stdin.readline

case_cnt = int(input())

def find_move_cnt(start_r, start_c, end_r, end_c, loc):
    move_r = [-2,-1,+1,+2,-2,-1,+1,+2]
    move_c = [-1,-2,-2,-1,+1,+2,+2,+1]
    next_node = deque([(start_r,start_c,0)])
    loc[start_r][start_c] = 1

    while next_node:
        now_r, now_c, now_val = next_node.popleft()
        if now_r == end_r and now_c == end_c:
            return now_val
        for move_idx in range(8):
            next_r, next_c = now_r + move_r[move_idx], now_c + move_c[move_idx]
            if 0 <= next_r < len(loc) and 0 <= next_c < len(loc):
                if loc[next_r][next_c] != 1:
                    loc[next_r][next_c] = 1
                    next_node.append((next_r, next_c, now_val + 1))


for _ in range(case_cnt):
    location_size = int(input())
    location = [[0 for _ in range(location_size)] for _ in range(location_size)]

    start_row, start_col = list(map(int, input().split()))
    end_row, end_col = list(map(int, input().split()))

    print(find_move_cnt(start_row, start_col, end_row, end_col, location))