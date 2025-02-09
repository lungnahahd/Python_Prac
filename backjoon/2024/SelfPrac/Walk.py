# 걷기 (1459)
## 난이도 : 실버 3

import sys
input = sys.stdin.readline

row_max, col_max, direct_val, cross_val = list(map(int, input().split()))

answer = 0
if direct_val * 2 <= cross_val:
    answer = direct_val * (row_max + col_max)
else:
    while row_max != 0 or col_max != 0:
        if row_max != 0 and col_max != 0:
            if row_max > col_max:
                answer += cross_val * (col_max)
                row_max -= col_max
                col_max = 0
            elif row_max < col_max:
                answer += cross_val * (row_max)
                col_max -= row_max
                row_max = 0
            else:
                answer += cross_val * (row_max)
                break
        else:
            now_val = max(row_max, col_max)
            if cross_val <= direct_val:
                can_cross = (now_val // 2) * 2
                can_direct = now_val % 2
                answer += (can_cross * cross_val)
                answer += (can_direct * direct_val)
            else:
                answer += (now_val * direct_val)
            break

print(answer)