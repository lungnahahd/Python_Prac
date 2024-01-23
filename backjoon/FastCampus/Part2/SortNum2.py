# 수 정렬하기 2 (2751)
## 난이도 : 하

import heapq

cnt = int(input())
n_num = []

for _ in range(cnt):
    temp = int(input())
    heapq.heappush(n_num, temp)
    
while n_num:
    now = heapq.heappop(n_num)
    print(now)

