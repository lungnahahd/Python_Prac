# 강의실 (1374)
## 난이도 : 골드 5

import sys
import heapq

input = sys.stdin.readline
finished = set()
remain = []
studying_room = []

count_room = int(input())
result = 0

for _ in range(count_room):
    num, start, end = list(map(int, input().split()))
    heapq.heappush(remain, (-end, start, num))

while remain:
    now_end, now_start, now_num = heapq.heappop(remain)

    if len(studying_room) == 0:
        if result == 0:
            result += 1
    else:
        if abs(studying_room[0]) < abs(now_end):
            result += 1
        else:
            heapq.heappop(studying_room)
    heapq.heappush(studying_room, (-now_start))

print(result)