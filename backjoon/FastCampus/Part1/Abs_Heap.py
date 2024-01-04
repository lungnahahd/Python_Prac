# 절댓값 힙 (11286)
## 난이도 : 중

import heapq
from collections import deque

cnt_cmd = int(input())

arr = deque([])
result = []

for _ in range(cnt_cmd):
    cmd = int(input())
    if (cmd == 0):
        if len(arr) == 0:
            result.append(0)
        else:
            abs_val, val = arr.popleft()
            #abs_val, val = heapq.heappop(arr)
            result.append(val)
    else:
        arr.append((abs(cmd), cmd))
        arr = deque(sorted(arr))
        #heapq.heappush(arr, (abs(cmd),cmd))

for num in result:
    print(num)