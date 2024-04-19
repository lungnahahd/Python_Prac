# 크게 만들기 (2812)
## 난이도 : 골드 3

import sys
from collections import deque

num_cnt, out_cnt = list(map(int, input().split()))
#nums = list(input())
#dq = deque(nums)
test = input()
result = 0
def backTracking(out_cnt, now_num, remain):
    global result
    #print(now_num)

    if out_cnt == 0:
        now_num  += remain
        result = max(result, int(now_num))
    elif len(remain) == out_cnt or len(remain) == 0:
        result = max(result, int(now_num))
    elif len(remain) == 1:
        now_num += remain
        result = max(result, int(now_num))
    else:
        backTracking(out_cnt-1, now_num, remain[1:])
        backTracking(out_cnt, now_num + remain[0], remain[1:])
        



backTracking(out_cnt, '0', test)
print(result)