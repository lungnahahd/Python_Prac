# 드래곤 커브 (15685)
## 난이도 : 골드 3
import sys
from collections import deque
input = sys.stdin.readline


cnt = int(input())
total_curve = [[0 for _ in range(100)] for _ in range(100)]

def make_curve(generation, node_hq):



move_row = [0, -1, 0, 1]
move_col = [1, 0, -1, 0]
for _ in range(cnt):
    col, row, way, generation = list(map(int, input().split()))
