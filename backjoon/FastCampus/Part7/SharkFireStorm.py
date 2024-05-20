# 마법사 상어와 파이어스톰 (20058)
## 난이도 : 골드 3

import sys
import copy
input = sys.stdin.readline

N, case_cnt = list(map(int, input().split()))
size = 2**N
area = []

for _ in range(size):
    temp = list(map(int, input().split()))
    area.append(temp)

case = list(map(int, input().split()))
move_col = [+1,0,-1,0]
move_row = [0,+1,0,-1]


def turn_real(area, start_row, end_row, start_col, end_col):
    origin = copy.deepcopy(area)
    ## 여기에 새로운 파이어스톰 구현 필요
    


def turn_area(area, start_row, end_row, start_col, end_col):
    while start_col < end_col:
        next_row, next_col = start_row, start_col
        before_val = area[start_row][start_col]
        for idx in range(4):
            while start_row <= next_row + move_row[idx] <= end_row and start_col <= next_col + move_col[idx] <= end_col:
                next_row += move_row[idx]
                next_col += move_col[idx]
                temp = area[next_row][next_col]
                area[next_row][next_col] = before_val
                before_val = temp
        start_row += 1
        start_col += 1
        end_row -= 1
        end_col -= 1
    return area

def fire_storm(area):
    for r in range(len(area)):
        for c in range(len(area)):
            if area[r][c] != 0 :
                count = 0
                for idx in range(4):
                    next_r, next_c = r + move_row[idx], c + move_col[idx]
                    if 0 <= next_r < len(area) and 0 <= next_c < len(area):
                        if area[next_r][next_c] != 0:
                            count += 1
                if count < 3:
                    area[r][c] -= 1
    return area

def count_ice(area):
    result = 0
    for r in range(len(area)):
        for c in range(len(area)):
            result += area[r][c]
    return result

            

for cs in case:
    if cs == 0:
        now_end_col, now_end_row = len(area), len(area)
        #area = turn_area(area, 0, now_end_row-1, 0, now_end_col-1)
    else:
        jump = 2**cs
        now_end_row, now_end_col = jump - 1, jump - 1
        while True:
            while True:
                print(now_end_row - jump + 1, now_end_row, now_end_col - jump + 1, now_end_col)
                area = turn_area(area, now_end_row - jump + 1, now_end_row, now_end_col - jump + 1, now_end_col)
                if 0 <= now_end_col + jump < len(area):
                    now_end_col += jump
                else:
                    break
            if 0 <= now_end_row + jump < len(area):
                now_end_row += jump
                now_end_col = jump - 1
            else:
                break
    area = fire_storm(area)
print(count_ice(area))
