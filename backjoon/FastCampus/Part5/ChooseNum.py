# 숫자고르기 (2668)
## 난이도 : 골드 5

import sys
input = sys.stdin.readline

n = int(input())
numbers = [0 for _ in range(n+1)]
cycle_num = []
visited, finished = [False for _ in range(n+1)], [False for _ in range(n+1)]

def chkCycle(start):
    global visited, finished
    end = numbers[start]
    visited[start] = True
    if not visited[end]:
        chkCycle(end)
    else:
        if start == end:
            cycle_num.append(start)
        elif not finished[end]:
            temp = end
            while True:
                temp = numbers[temp]
                cycle_num.append(temp)
                if end == temp:
                    break

    finished[start] = True



for idx in range(1,n+1):
    numbers[idx] = int(input())

for idx in range(1, n+1):
    if not visited[idx]:
        chkCycle(idx)
print(len(cycle_num))
cycle_num.sort()
for num in cycle_num:
    print(num)