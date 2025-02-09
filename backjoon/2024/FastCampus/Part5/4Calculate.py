# 4연산 (14395)
## 난이도 : 골드 4

import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize
from collections import deque

start_num, end_num = list(map(int, input().split()))
visited = set()
result = []


def bfs_cal(start):
    global visited, result

    method = ['*', '+', '-', '/']

    save = deque([(start, '')])
    visited.add(start)

    while save:
        num, cal = save.popleft()
        for idx in range(4):
            if method[idx] == '*':
                temp_num = num * num
                temp_cal = cal + '*'
            elif method[idx] == '+':
                temp_num = num + num
                temp_cal = cal + '+'
            elif method[idx] == '-':
                temp_num = num - num
                temp_cal = cal + '-'
            elif method[idx] == '/' and num != 0:
                temp_num = num / num
                temp_cal = cal + '/'

            if temp_num in visited:
                continue

            if temp_num == end_num:
                result.append(temp_cal)
                return
            if temp_num < end_num:
                save.append((temp_num, temp_cal))
                visited.add(temp_num)


if start_num == end_num:
    print(0)
bfs_cal(start_num)

if len(result) == 0 and start_num != end_num:
    print(-1)
elif len(result) != 0 and start_num != end_num:
    result.sort()
    print(result[0])