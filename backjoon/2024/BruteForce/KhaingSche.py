# 카잉 달력 (6064)
## 난이도 : 실버 1 

import sys
import math
input = sys.stdin.readline

case_cnt = int(input())


def find_max_year(a,b):
    return a * b / math.gcd(a,b)


for _ in range(case_cnt):
    max_M, max_N, x, y = list(map(int, input().split()))
    max_year = int(find_max_year(max_M, max_N))
    arr_x = []
    set_y = set()
    not_end_x, not_end_y = True, True
    idx = 0
    now_add = 0
    mid_result = -1
    while x <= max_year:
        if (x - y) >= 0:
            if (x - y) % max_N == 0:
                mid_result = x
                break
        x += max_M

    print(mid_result)