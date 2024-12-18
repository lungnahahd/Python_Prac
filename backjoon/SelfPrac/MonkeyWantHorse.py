# 말이 되고픈 원숭이 (1600)
## 골드 3

import sys
from collections import deque
input = sys.stdin.readline 
INT_MAX = sys.maxsize


jump_cnt = int(input())
col_cnt, row_cnt = list(map(int, input().split()))
zone = []
visited = [[(INT_MAX, 0) for _ in range(col_cnt)] for _ in range(row_cnt)]

monkey_row = [+1, 0, -1, 0]
monkey_col = [0, +1, 0, -1]
horse_row = [+1,+2,+1,+2,-1,-2,-1,-2]
horse_col = [+2,+1,-2,-1,+2,+1,-2,-1]

for _ in range(row_cnt):
    temp = list(map(int, input().split()))
    zone.append(temp)
answer = INT_MAX
def find_way(row, col, jump, move_val):
    global answer
    for m_idx in range(4):
        next_row, next_col = monkey_row[m_idx] + row, monkey_col[m_idx] + col
        if next_row == row_cnt - 1 and next_col == col_cnt - 1:
            answer = min(move_val+1, answer)
            break
        if 0 <= next_row < row_cnt and 0 <= next_col < col_cnt:
            if zone[next_row][next_col] == 1:
                continue
            if move_val + 1 > visited[next_row][next_col][0]:
                continue
            if move_val + 1 == visited[next_row][next_col][0] and jump <= visited[next_row][next_col][1]:
                continue
            visited[next_row][next_col]= (move_val + 1, jump)
            find_way(next_row,next_col, jump, move_val + 1)
    
    if jump != 0:
        for h_idx in range(8):
            next_row, next_col = horse_row[h_idx] + row, horse_col[h_idx] + col
            if next_row == row_cnt - 1 and next_col == col_cnt - 1:
                answer = min(move_val + 1, answer)
                break
            if 0 <= next_row < row_cnt and 0 <= next_col < col_cnt:
                if zone[next_row][next_col] == 1:
                    continue
                if move_val + 1 > visited[next_row][next_col][0]:
                    continue
                if move_val + 1 == visited[next_row][next_col][0] and jump <= visited[next_row][next_col][1]:
                    continue
                visited[next_row][next_col] = (move_val + 1, jump)
                find_way(next_row, next_col, jump-1, move_val + 1)

find_way(0,0,jump_cnt,0)

if answer == INT_MAX:
    print(-1)
else:
    print(answer)