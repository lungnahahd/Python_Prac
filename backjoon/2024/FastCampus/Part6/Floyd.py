# 플로이드 (11404)
## 난이도 : 골드 4

import sys
INT_MAX = int(1e9)
#input = sys.stdin.readline

cnt_city = int(input())
cnt_bus = int(input())

answer = [[INT_MAX] * (cnt_city+1) for _ in range(cnt_city+1)]

for _ in range(cnt_bus):
    start, end, cost = list(map(int, input().split()))
    answer[start][end] = min(answer[start][end], cost)

for i in range(1, cnt_city+1):
    for j in range(1, cnt_city+1):
        if i == j:
            answer[i][j] = 0

for k in range(1, cnt_city+1):
    for i in range(1, cnt_city+1):
        for j in range(1, cnt_city+1):
                answer[i][j] = min(answer[i][k] + answer[k][j], answer[i][j])

for i in range(1, cnt_city+1):
    for j in range(1, cnt_city+1):
        if answer[i][j] == INT_MAX:
            print(0, end= ' ')
        else:
            print(answer[i][j], end=' ')
    print()