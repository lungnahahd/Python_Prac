# 효율적인 해킹 (1325)
## 난이도 : 하

import sys
from collections import deque

input = sys.stdin.readline

cnt_computer, cnt_believe = list(map(int, input().split()))

computer = [[] for _ in range(cnt_computer+1)]
result = [0 for _ in range(cnt_computer+1)]


def bfs(start, visited):
    go = deque([start])
    make_disease = 0
    while go:
        now_com = go.popleft()
        visited[now_com] = True
        make_disease += 1
        for next_com in computer[now_com]:
            if visited[next_com]:
                continue
            go.append(next_com)
    return make_disease

for _ in range(cnt_believe):
    a_com, b_com = list(map(int, input().split()))
    computer[b_com].append(a_com) # b 컴퓨터가 감염되면, a 컴퓨터가 감염

for idx in range(1, cnt_computer+1):
    visited = [False for _ in range(cnt_computer+1)]
    result[idx] = bfs(idx, visited)

big_num = max(result)
answer = []

for idx in range(1, cnt_computer):
    if (result[idx] == big_num):
        answer.append(str(idx))
print(' '.join(answer))