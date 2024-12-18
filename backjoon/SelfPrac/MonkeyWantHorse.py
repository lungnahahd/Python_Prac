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
answer = -1
def find_way(row, col, jump, move_val):
    for m_idx in range(4):
        if next_row == row_cnt - 1 and next_col == col_cnt - 1:
            answer = visited[next_row][next_col][0]
            return 
        next_row, next_col = row + monkey_row[m_idx], col + monkey_col[m_idx]
        if 0 <= next_row < row_cnt and 0 <= next_col < col_cnt:
            if move_val + 1 > visited[next_row][next_col][0]:
                break
            if move_val + 1 == visited[next_row][next_col][0] and jump <= visited[next_row][next_col][1]:
                break
            visited[next_row][next_col]= (move_val + 1, jump)
            find_way(next_row,next_col, jump, move_val + 1)


    ## 말 움직이기 코드 작성하기
