# 수 정렬하기 (2750)
## 난이도 : 하

import sys

input = sys.stdin.readline
import heapq

cnt = int(input())

nums = []

for _ in range(cnt):
    now = int(input())
    heapq.heappush(nums, now)

while nums:
    temp = heapq.heappop(nums)
    print(temp)