# N-Queen (9663)
## 난이도 : 중

import sys
input = sys.stdin.readline

n = int(input())
∂
rst = 0
game_world = [[False for _ in range(n)] for _ in range(n)]

def bfs(start):
    global rst


    for idx in range(start, n):
        