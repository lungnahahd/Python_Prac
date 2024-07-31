# 안전 영역 (2468)
## 난이도 : 실버 1

import sys
from collections import deque
input = sys.stdin.readline

size = int(input())
area = []

very_height = 0
for _ in range(size):
    temp = list(map(int, input().split()))
    very_height = max(very_height, max(temp))
    area.append(temp)


very_height -= 1
move_r = [0, +1, 0, -1]
move_c = [-1, 0, +1, 0]

def bfs(row, col, now_visited, max_tall):
    now_visited[row][col] = True
    now_go_list = deque([(row, col)])

    while now_go_list:
        now_row, now_col = now_go_list.popleft()
        for idx in range(4):
            next_row, next_col = now_row + move_r[idx], now_col + move_c[idx]
            if 0 <= next_row < size and 0 <= next_col < size:
                if not now_visited[next_row][next_col] and area[next_row][next_col] > max_tall:
                    now_visited[next_row][next_col] = True
                    now_go_list.append((next_row, next_col))
    return now_visited



result_safe_cnt = 1

while very_height > 0:
    visited = [[False for _ in range(size)] for _ in range(size)]
    now_safe_cnt = 0
    for now_r in range(size):
        for now_c in range(size):
            if not visited[now_r][now_c] and area[now_r][now_c] > very_height:
                visited = bfs(now_r, now_c, visited, very_height)
                now_safe_cnt += 1
    result_safe_cnt = max(result_safe_cnt, now_safe_cnt)
    very_height -= 1

print(result_safe_cnt)