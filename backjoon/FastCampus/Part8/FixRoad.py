# 흙길 보수하기 (1911)
## 난이도 : 골드 5

import sys
import heapq
input = sys.stdin.readline

need_fix, bridge = list(map(int, input().split()))
road = []

for _ in range(need_fix):
    start, end = list(map(int, input().split()))
    heapq.heappush(road, (start,end-1))

before_start = -1
answer_count = 0
while road:
    now_start, now_end = heapq.heappop(road)
    if now_start < before_start:
        now_start = before_start 
    while now_start <= now_end:
        now_start += (bridge)
        answer_count += 1
    before_start = now_start
print(answer_count)