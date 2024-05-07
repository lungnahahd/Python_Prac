# 연구소 3 (17142)
## 난이도 : 골드 3

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
INT_MAX = sys.maxsize

size, cnt_virus = list(map(int, input().split()))
laboratory = []
start_virus = []
move_row = [-1,0,+1,0]
move_col = [0,-1,0,+1]

for row in range(size):
    temp = list(map(int, input().split()))
    laboratory.append(temp)
    for col in range(size):
        if temp[col] == 2:
            start_virus.append((row, col))


result = INT_MAX
for now_case in combinations(start_virus,cnt_virus):
    save = deque([])

    visited = [[INT_MAX for _ in range(size)] for _ in range(size)]
    for r in range(size):
        for c in range(size):
            if laboratory[r][c] == 1:
                visited[r][c] = -1
    for row, col in now_case:
        save.append((row, col, 0))
        visited[row][col] = 0
    
    while save:
        now_row, now_col, now_time = save.popleft()
        for idx in range(4):
            next_row, next_col = now_row + move_row[idx], now_col + move_col[idx]
            if 0 <= next_row < size and 0 <= next_col < size:
                if laboratory[next_row][next_col] != 1 and visited[next_row][next_col] == INT_MAX:
                    # if laboratory[next_row][next_col] == 2:
                    #     visited[next_row][next_col] = now_time
                    #     save.append((next_row, next_col, now_time))
                    # else:
                    visited[next_row][next_col] = now_time + 1
                    save.append((next_row, next_col, now_time + 1))
    for r in range(size):
        for c in range(size):
            if laboratory[r][c] == 2:
                visited[r][c] = 0
                
    mid_result = max(map(max, visited))
    if mid_result != INT_MAX:
        result = min(result, mid_result)
if result == INT_MAX:
    result = -1
print(result)