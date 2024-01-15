# 강의실 (1374)
## 난이도 : 중

import sys
import heapq
import copy

input = sys.stdin.readline

cnt_class = int(input())
result = 0
remain = []
temp = []

for _ in range(cnt_class):
    no, start, end = list(map(int, input().split()))
    heapq.heappush(remain, (-end, -start, no))

s_time = -1
e_time = 0
while len(remain) != 0 :
    end_temp, start_temp, no_temp = heapq.heappop(remain)
    if (s_time == -1 or s_time >= -end_temp):
        s_time = -start_temp
        e_time = -end_temp
    else :
        heapq.heappush(temp, (end_temp, start_temp, no_temp))
    if len(remain) == 0:
        result += 1
        remain = copy.deepcopy(temp)
        temp = []
        s_time = -1
print(result)

