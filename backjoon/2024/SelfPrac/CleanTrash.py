# 쓰레기 치우기 (1736)
## 난이도 : 골드 2 

import sys
input = sys.stdin.readline

row_size, col_size = list(map(int, input().split()))

room = []

for _ in range(row_size):
    temp = list(map(int, input().split()))
    room.append(temp)


def clean_trash(now_row, now_col):
    global room

    chg_col = now_col
    for now_c in range(now_col, col_size):
        if room[now_row][now_c] == 1:
            room[now_row][now_c] = 0
            chg_col = now_c
    if now_row + 1 < row_size:
        clean_trash(now_row + 1, chg_col)

result = 0

for row_start in range(row_size):
    for col_start in range(col_size):
        if room[row_start][col_start] == 1:
            result += 1
            clean_trash(row_start, col_start)

print(result)