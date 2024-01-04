# 절댓값 힙 (11286)
## 난이도 : 중

import heapq

cnt_cmd = int(input())

arr = []
result = []
for _ in range(cnt_cmd):
    cmd = int(input())
    if (cmd == 0):
        if len(arr) == 0:
            result.append(0)
        else:
            abs_val, val = heapq.heappop(arr)
            result.append(val)
    else:
        heapq.heappush(arr, (abs(cmd),cmd))

for num in result:
    print(num)