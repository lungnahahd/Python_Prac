# 컵라면 (1781)
## 난이도 : 골드 2

import sys
import heapq
input = sys.stdin.readline

count = int(input())
q_noodles = []

for _ in range(count):
    deadline, cup_cost = list(map(int, input().split()))
    heapq.heappush(q_noodles, (-deadline, -cup_cost))

time = -q_noodles[0][0]
result = 0
while q_noodles:
    now_time, now_cost = heapq.heappop(q_noodles)
    now_time, now_cost = -now_time, -now_cost
    if time >= now_time:
        #print(now_time, now_cost)
        result += now_cost
        time -= 1
    time = min(time, now_time-1)
    if time <= 0:
        break
print(result)