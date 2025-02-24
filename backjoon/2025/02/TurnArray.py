# 배열 돌리기 1 (16926)
## 난이도 : 골드 5

import sys
from collections import deque
input = sys.stdin.readline

row_cnt, col_cnt, turn_cnt = list(map(int, input().split()))
location = []

for _ in range(col_cnt):
    location.append(list(map(int, input().split())))

def rotate_dq(start_r, start_c, end_r, end_c):
    global location

    now_target = deque([])
    # 윗 라인의 값을 넣는 로직
    for c in range(start_c, end_c+1):
        now_target.append(location[start_r][c])
    # 우 라인의 값을 넣는 로직 
    for r in range(start_r+1, end_r +1):
        now_target.append(location[r][end_c])
    # 하단 라인의 값을 넣는 로직
    for c in range(end_c-1, start_c -1, -1):
        now_target.append(location[end_r][c])
    # 좌 라인의 값을 넣는 로직
    for r in range(end_c-1, start_c, -1):
        now_target.append(location[r][start_c])
    now_target.rotate(-turn_cnt)

    for c in range(start_c, end_c+1):
        location[start_r][c] = now_target.popleft()
    for r in range(start_r+1, end_r+1):
        location[r][end_c] = now_target.popleft()
    for c in range(end_c-1,start_c-1, -1):
        location[end_r][c] = now_target.popleft()
    for r in range(end_c-1, start_c, -1):
        location[r][start_c] = now_target.popleft()

s_row, s_col, e_row, e_col = 0, 0, row_cnt-1, col_cnt-1
while (s_row <= e_row and s_col <= e_col):
    rotate_dq(s_row, s_col, e_row, e_col)
    s_row += 1
    s_col += 1
    e_row -= 1
    e_col -= 1

for r_idx in range(len(location)):
    for num in location[r_idx]:
        print(num, end = ' ')
    print()