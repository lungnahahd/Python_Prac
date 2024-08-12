# 영역 구하기 (2583)
## 난이도 : 실버 1
import sys
from collections import deque
input = sys.stdin.readline

row_size, col_size, out_area_size = list(map(int, input().split()))

area = [[0 for _ in range(col_size)] for _ in range(row_size)]
visited = [[False for _ in range(col_size)] for _ in range(row_size)]
move_r = [-1,0,+1,0]
move_c = [0,-1,0,+1]

def remove_area(start_row, start_col, end_row, end_col):
    global area
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            area[r][c] = 1


def bfs(start_row, end_row):
    global visited

    save = deque([(start_row, end_row)])
    now_cost = 1
    while save:
        now_r, now_c = save.popleft()
        for m_idx in range(4):
            next_r, next_c = now_r + move_r[m_idx], now_c + move_c[m_idx]
            if 0 <= next_r < row_size and 0 <= next_c < col_size:
                if not visited[next_r][next_c] and area[next_r][next_c] == 0:
                    visited[next_r][next_c] = True
                    save.append((next_r,next_c))
                    now_cost += 1
    return now_cost


for case in range(out_area_size):
    now_start_col, now_start_row, now_end_col, now_end_row = list(map(int, input().split()))
    remove_area(now_start_row, now_start_col, now_end_row, now_end_col)

result = []
for r in range(row_size):
    for c in range(col_size):
        if area[r][c] == 0 and not visited[r][c]:
            visited[r][c] = True
            result.append(bfs(r,c))

result.sort()
answer = ''
print(len(result))
for num in result:
    answer += str(num)
    answer += ' '
print(answer[:-1])