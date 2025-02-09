# 소트인사이드 (1427)
## 난이도 : 하

import heapq

nums = list(input())
temp = []

for num in nums:
    num = int(num)
    heapq.heappush(temp, -num)

result = []
while(temp):
    now = -heapq.heappop(temp)
    result.append(str(now))

print(''.join(result))
