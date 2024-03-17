# 등수 매기기 (2012)
## 난이도 : 하

import sys

input = sys.stdin.readline
from collections import deque

cnt = int(input())

chk_num = [False for _ in range(cnt + 1)]

remain_num = []
rst = 0

for _ in range(cnt):
    temp = int(input())
    if chk_num[temp]:
        remain_num.append(temp)
    else:
        chk_num[temp] = True

remain_num.sort()
remain_num = deque(remain_num)

for idx in range(1, cnt+1):
    if chk_num[idx]:
        continue
    now_remain = remain_num.popleft()
    rst += abs(now_remain - idx)

print(rst)