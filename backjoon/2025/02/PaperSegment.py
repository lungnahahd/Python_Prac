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
    max_num = 0
    idx = 0
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
        if now_num == '':
            result += 0
        else:
            if max_num < int(now_num):
                idx = c_idx
                max_num = int(now_num)
            result += int(now_num)
    return (max_num, idx)

def row_way_sum():
    result = 0
    max_num = 0
    idx = 0
    for r_idx in range(row_cnt):
        now_num = ''
        already_start = False
        for c_idx in range(col_cnt):
            if not already_start:
                if nums_loc[r_idx][c_idx] != '0':
                    now_num += nums_loc[r_idx][c_idx]
                    already_start = True
            else:
                now_num += nums_loc[r_idx][c_idx]
        if now_num == '':
            result += 0
        else:
            if max_num < int(now_num):
                idx = r_idx
                max_num = int(now_num)
            result += int(now_num)
    return (max_num, idx)


def col_way_sum_a():
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
        if now_num == '':
            result += 0
        else:
            result += int(now_num)
    return result

def row_way_sum_b():
    result = 0
    for r_idx in range(row_cnt):
        now_num = ''
        already_start = False
        for c_idx in range(col_cnt):
            if not already_start:
                if nums_loc[r_idx][c_idx] != '0':
                    now_num += nums_loc[r_idx][c_idx]
                    already_start = True
            else:
                now_num += nums_loc[r_idx][c_idx]
        if now_num == '':
            result += 0
        else:
            result += int(now_num)
    return result



row_result = row_way_sum_b()
col_result = col_way_sum_a()


answer_a = max(row_result, col_result)
answer_b = 0
for case_idx in range(min(row_cnt, col_cnt)):
    row_result, row_idx = row_way_sum()
    col_result, col_idx = col_way_sum()
    if row_result >= col_result:
        nums_loc.pop(row_idx)
        answer_b += row_result
        row_cnt -= 1
    else:
        for idx in range(len(nums_loc)):
            nums_loc[idx].pop(col_idx)
        answer_b += col_result
        col_cnt -= 1

answer = max(answer_a, answer_b)
print(answer)