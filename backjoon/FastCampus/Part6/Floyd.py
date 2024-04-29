# 플로이드 (11404)
## 난이도 : 골드 4

import sys
INT_MAX = sys.maxsize
input = sys.stdin.readline

cnt_city = int(input())
cnt_bus = int(input())

answer = [[INT_MAX for _ in range(cnt_bus+1)] for _ in range(cnt_bus+1)]

for _ in range(cnt_bus):
    start, end, cost = list(map(int, input().split()))
    answer[start][end] = min(answer[start][end], cost)

for k in range(1, cnt_city+1):
    for i in range(1, cnt_city+1):
        for j in range(1, cnt_city+1):
            if i == j:
                answer[i][j] = 0
            else:
                temp_cost = answer[i][k] + answer[k][j]
                answer[i][j] = min(temp_cost, answer[i][j])

for i in range(1, cnt_city+1):
    for j in range(1, cnt_city+1):
        print(answer[i][j], end=' ')
    print()