# 종이 조각 (14391)
## 난이도 : 골드 3

import sys
input = sys.stdin.readline

row_cnt, col_cnt = list(map(int,input().split()))
nums_loc = []

for _ in range(row_cnt):
    temp = str(input().rsplit())
    nums_loc.append(list(temp)[2:-2])

def col_way_sum():
    result = 0
    for c_idx in range(col_cnt):
        now_num = ''
        already_start = False
        for r_idx in range(row_cnt):
            if not already_start:
                if nums_loc[r_idx][c_idx] != '0':
                    now_num += nums_loc[r_idx][c_idx]
                    already_start = True
            else:
                now_num += nums_loc[r_idx][c_idx]
        result += int(now_num)
    return result

def row_way_sum():
    result = 0
    for r_idx in range(row_cnt):
        now_num = ''
        already_start = False
        for c_idx in range(col_cnt):
            if not already_start:
                if nums_loc[r_idx][c_idx] != '0':
                    now_num += nums_loc[r_idx][c_idx]
                    already_start = False
            else:
                now_num += nums_loc[r_idx][c_idx]
        result += int(now_num)
    return result

row_result = row_way_sum()
col_result = col_way_sum()
print(max(row_result, col_result))