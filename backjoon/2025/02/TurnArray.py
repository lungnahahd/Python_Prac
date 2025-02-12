# 배열 돌리기 1 (16926)
## 난이도 : 골드 5

import sys
input = sys.stdin.readline

row_cnt, col_cnt, turn_cnt = list(map(int, input().split()))
location = []

for _ in range(col_cnt):
    location.append(list(map(int, input().split())))

def left_turn(start_r, start_c, end_r):
    global location
    last_value = 0
    for r_idx in range(start_r, end_r + 1):
        last_value = location[start_r+1][start_c]
        location[start_r+1][start_c] = location[start_r][start_c]
    return last_value

def right_turn(start_r, start_c, end_r, start_value):
    global location
    start_r -= 1
    last_value = location[start_r][start_c]
    location[start_r][start_c] = start_value
    for r_idx in range(start_r-1, end_r-1, -1):
        location[r_idx][start_c], last_value = last_value, location[r_idx][start_c]
    return last_value

def down_turn(start_r, start_c, end_c, start_value):
    global location
    start_c += 1
    last_value = location[start_r][start_c]
    location[start_r][start_c] = start_value
    for c_idx in range(start_c+1, end_c+1):
        location[start_r][c_idx], last_value = last_value, location[start_r][c_idx]
    return last_value

def top_turn(start_r, start_c, end_c, start_value):
    global location
    start_c -= 1
    last_value = location[start_r][start_c]
    location[start_r][start_c] = start_value
    for c_idx in range(start_c-1, end_c -1, -1):
        location[start_r][c_idx], last_value = last_value, location[start_r][c_idx]



