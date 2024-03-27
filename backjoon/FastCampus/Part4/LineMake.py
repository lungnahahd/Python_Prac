# 섯 긋기 (2170)
## 난이도 : 골드 5

import sys
import heapq

input = sys.stdin.readline

cnt_line = int(input())
num_save = []
result = 0
state, start = 0, 0

for _ in range(cnt_line):
    x, y = list(map(int, input().split()))
    heapq.heappush(num_save, (x, -1))
    heapq.heappush(num_save, (y, +1))

while num_save:
    now_node, now_val = heapq.heappop(num_save)
    if now_val == -1:
        if state == 0:
            start = now_node
        state += now_val
    else:
        state += now_val
        if state == 0:
            result += abs(now_val - start)
print(result)
        