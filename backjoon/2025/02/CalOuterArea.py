# 겉넓이 구하기 (16931)
## 난이도 : 실버 2

import sys
input = sys.stdin.readline

row_size, col_size = list(map(int, input().split()))
outer_area = []
result = 0

for _ in range(row_size):
    temp = list(map(int, input().split()))
    outer_area.append(temp)
    result += len(temp) * 2

for r_idx in range(row_size):
    before_high = 0
    for c_idx in range(col_size):
        if before_high < outer_area[r_idx][c_idx]:
            result += (outer_area[r_idx][c_idx] - before_high)
        before_high = outer_area[r_idx][c_idx]

for r_idx in range(row_size):
    before_high = 0
    for c_idx in range(col_size-1, -1, -1):
        if before_high < outer_area[r_idx][c_idx]:
            result += (outer_area[r_idx][c_idx] - before_high)
        before_high = outer_area[r_idx][c_idx]

for c_idx in range(col_size):
    before_high = 0
    for r_idx in range(row_size):
        if before_high < outer_area[r_idx][c_idx]:
            result += (outer_area[r_idx][c_idx] - before_high)
        before_high = outer_area[r_idx][c_idx]

for c_idx in range(col_size):
    before_high = 0
    for r_idx in range(row_size-1, -1, -1):
        if before_high < outer_area[r_idx][c_idx]:
            result += (outer_area[r_idx][c_idx] - before_high)
        before_high = outer_area[r_idx][c_idx]



print(result)