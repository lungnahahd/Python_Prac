# 우체국 (2141)
## 난이도 : 골드 4

import sys
import heapq
input = sys.stdin.readline 


location_num = int(input())
save = []
people_num = 0

for _ in range(location_num):
    where, num = list(map(int, input().split()))
    heapq.heappush(save, (where, num))
    people_num += num

mid_num = people_num  // 2

now_val = 0
answer = 0
while save:
    point, now_num = heapq.heappop(save)
    now_val += now_num
    if now_val >= mid_num:
        answer = point
        break
print(answer)