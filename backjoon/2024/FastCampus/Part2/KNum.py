# K 번쨰 수 찾기(11004)
## 난이도 : 중

import heapq

num_cnt, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

temp = []

for num in nums:
    heapq.heappush(temp, num)

for idx in range(k-1):
    heapq.heappop(temp)

print(temp[0])
