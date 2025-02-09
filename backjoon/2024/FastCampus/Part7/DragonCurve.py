# 드래곤 커브 (15685)
## 난이도 : 골드 3
import sys
from collections import deque
input = sys.stdin.readline


cnt = int(input())
total_curve = [[0 for _ in range(101)] for _ in range(101)]

def make_curve(node_hq):
    temp = []
    now_row, now_col = node_hq[0]
    for idx in range(len(node_hq)-1):
        start_row, start_col, next_row, next_col = node_hq[idx][0], node_hq[idx][1], node_hq[idx+1][0], node_hq[idx+1][1]
        col_dist, row_dist = start_col - next_col, start_row - next_row
        if row_dist == -1:
            next_row, next_col = now_row, now_col - 1
        elif row_dist == 1:
            next_row, next_col = now_row, now_col + 1
        elif col_dist == -1:
            next_row, next_col = now_row + 1, now_col
        elif col_dist == 1:
            next_row, next_col = now_row - 1, now_col
        if (0 <= next_row < 101 and 0 <= next_col < 101):
            total_curve[next_row][next_col] = 1
        temp.append((next_row, next_col))
        now_row, now_col = next_row, next_col
    for row, col in temp:
        node_hq.appendleft((row, col))
    return node_hq

def count_result(total_curve):
    global count
    for r in range(100):
        for c in range(100):
            if total_curve[r][c] == 1:
                if total_curve[r+1][c] == 1 and total_curve[r][c+1] == 1 and total_curve[r+1][c+1] == 1:
                    count += 1

move_row = [0, -1, 0, 1]
move_col = [1, 0, -1, 0]
for _ in range(cnt):
    col, row, way, generation = list(map(int, input().split()))
    node_hq = deque([])
    node_hq.appendleft((row, col))
    node_hq.appendleft((row + move_row[way], col + move_col[way]))
    if 0 <= row < 101 and 0 <= col < 101:
        total_curve[row][col] = 1
    if 0 <= row + move_row[way] < 101 and 0 <= col + move_col[way] < 101:
        total_curve[row + move_row[way]][col + move_col[way]] = 1
    for _ in range(generation):
        node_hq = make_curve(node_hq)


count = 0
count_result(total_curve)
print(count)