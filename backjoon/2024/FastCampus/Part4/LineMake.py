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
    num_save.append((x,-1))
    num_save.append((y,+1))

num_save.sort(reverse=True)

while num_save:
    now_node, now_val = num_save.pop()
    if now_val == -1:
        if state == 0:
            start = now_node
        state += now_val
    else:
        state += now_val
        if state == 0:
            result += abs(now_node - start)
print(result)
        