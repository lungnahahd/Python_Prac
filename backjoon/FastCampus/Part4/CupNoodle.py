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
buffer = []

while now_time != 1:
    temp_deadline, temp_cup_noodle = heapq.heappop(problems)
    if -temp_deadline < now_time :
        now_time = -temp_deadline
        result += (-temp_cup_noodle)
    else:
        #if now_time != 1:
        heapq.heappush(problems, (-(now_time-1),temp_cup_noodle))



print(result)


# 4
# 1 50
# 2 30
# 3 60
# 3 70

# 180