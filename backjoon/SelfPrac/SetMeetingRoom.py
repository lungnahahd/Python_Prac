# 회의실 배정(1931)
## 난이도 : 실버 1

import sys
import heapq
input = sys.stdin.readline

case_count = int(input())
time_table = []

class_num = []

for _ in range(case_count):
    start, end = list(map(int, input().split()))
    heapq.heappush(time_table, (-end, -start))


result = 0
before_start_time = sys.maxsize
while time_table:
    now_end, now_start = heapq.heappop(time_table)
    now_end, now_start = -now_end, -now_start
    if before_start_time > now_start:
        
        if before_start_time > now_end:
            result += 1
            before_start_time = now_start

print(result)