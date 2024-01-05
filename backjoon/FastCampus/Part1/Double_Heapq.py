# 이중 우선 순위 큐 (7622)
## 난이도 : 중상

import sys
from collections import deque

input = sys.stdin.readline

cnt_case = int(input())
result = []

for _ in range(cnt_case):
    cnt_cmd = int(input())
    queue = deque([])
    for _ in range(cnt_cmd):
        cmd, num = input().split()
        if (cmd == 'I'):
            queue.append(int(num))
            queue = deque(sorted(queue))
        else:
            if (len(queue) == 0):
                continue
            elif (num == '-1'):
                queue.popleft()
            elif (num == '1'):
                queue.pop()
    if (len(queue) == 0):
        result.append('EMPTY')
    else:
        result.append(str(queue[-1]) + ' ' + str(queue[0]))
    

for rst in result:
    print(rst)