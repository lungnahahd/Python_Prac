# 치즈 (2636)
## 난이도 : 골드 4

import sys
import copy
from collections import deque

input = sys.stdin.readline
move_r = [0,-1,0,+1]
move_c = [-1,0,+1,0]

row_size, col_size = list(map(int, input().split()))

area = []
time = 0
total_cheeze = 0
out_cheeze_cnt = 0

for _ in range(row_size):
    temp = list(map(int, input().split()))
    total_cheeze += temp.count(1)
    area.append(temp)

def last_bfs(graph):
    global visited, out_cheeze_cnt

    out_cheeze = set()
    can_go  = deque([(0,0)])
    visited[0][0] = True
    while can_go:
        now_r, now_c = can_go.popleft()
        for idx in range(4):
            next_r, next_c = now_r + move_r[idx], now_c + move_c[idx]
            if 0 <= next_r < row_size and 0 <= next_c < col_size:
                if graph[next_r][next_c] == 1:
                    out_cheeze.add((next_r, next_c))
                    visited[next_r][next_c] = True
                elif graph[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    can_go.append((next_r, next_c))
    out_cheeze_cnt += len(out_cheeze)
    for out_r, out_c in out_cheeze:
        graph[out_r][out_c] = 0
    return graph



while True:
    out_cheeze_cnt = 0
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    area = last_bfs(area)
    total_cheeze -= out_cheeze_cnt
    time += 1
    if total_cheeze == 0:
        break


print(time)
print(out_cheeze_cnt)