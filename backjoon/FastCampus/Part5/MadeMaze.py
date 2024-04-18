# 미로 만들기
## 난이도 : 골드 4

import sys
from collections import deque
INT_MAX = sys.maxsize
#input = sys.stdin.readline

size = int(input())
visited = [[INT_MAX for _ in range(size)] for _ in range(size)]
maze = []

# 처음 받은 미로를 세팅
for _ in range(size):
    temp = list(map(int, input()))
    maze.append(temp)

def find_end(start_r, start_c):
    global visited
    move_r = [0,1,0,-1]
    move_c = [1,0,-1,0]

    save = deque([(start_r, start_c, 0)])
    while save:
        now_r, now_c, now_cost = save.popleft()
        for idx in range(4):
            next_r, next_c = now_r + move_r[idx], now_c + move_c[idx]
            if 0 <= next_r < size and 0 <= next_c < size:
                if maze[next_r][next_c] == 0:
                    next_cost = now_cost+1
                else:
                    next_cost = now_cost
                # 초기 상태이거나, 지금까지 지나온 검은 방의 개수가 더 적다면 갱신
                if visited[next_r][next_c] == INT_MAX or next_cost < visited[next_r][next_c]:
                    visited[next_r][next_c] = next_cost
                    save.append((next_r, next_c, next_cost))

find_end(0,0)
print(visited[size-1][size-1])