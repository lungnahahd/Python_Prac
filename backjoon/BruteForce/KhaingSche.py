# 카잉 달력 (6064)
## 난이도 : 실버 1 

import sys
input = sys.stdin.readline

case_cnt = int(input())


def find_max_year(a,b):
    max_num = max(a,b)
    for num in range(max_num, a*b + 1):
        if num % a == 0 and num % b == 0:
            return num



for _ in range(case_cnt):
    max_M, max_N, x, y = list(map(int, input().split()))
    max_year = find_max_year(max_M, max_N)
    set_x, set_y = set(), set()
    arr_x, arr_y = [], []
    not_end_x, not_end_y = True, True
    idx = 0
    now_add = 0
    while not_end_x or not_end_y:
        if not_end_x:
            now_add = x + max_M * idx 
            if (now_add > max_year):
                not_end_x = False
            else:
                set_x.add(now_add)
                arr_x.append(now_add)
        if not_end_y:
            now_add = y + max_N * idx
            if (now_add > max_year):
                not_end_y = False
            else:
                set_y.add(now_add)
                arr_y.append(now_add)
        idx += 1
    mid_result = -1
    for num in arr_x:
        if num in set_y:
            mid_result = num
            break
    print(mid_result)