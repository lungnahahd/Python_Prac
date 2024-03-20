# 컵라면 (1781)
## 난이도 : 골드 2

import sys
import heapq

INT_MAX = sys.maxsize

cnt = int(input())

problems = []

for _ in range(cnt):
    deadline, cup_noodle = list(map(int, input().split()))
    heapq.heappush(problems, (-deadline, -cup_noodle))

now_time = INT_MAX
result = 0

while problems:
    temp_deadline, temp_cup_noodle = heapq.heappop(problems)
    if -temp_deadline < now_time:
        now_time = -temp_deadline
        result += (-temp_cup_noodle)
print(result)