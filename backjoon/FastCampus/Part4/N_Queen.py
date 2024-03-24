# N-Queen (9663)
## 난이도 : 중

import sys
input = sys.stdin.readline

n = int(input())

rst = 0
game_world = [[0] for _ in range(n)]

def bfs(start):
    global rst
    for idx in range(n):
        game_world[start] = idx
        if chk(game_world, start):
            if start+1 >= n:
                rst += 1
            else:
                bfs(start+1)

def chk(world,start):
    for idx in range(start):
        if idx != start:
            if world[idx] == world[start]:
                return False
            if abs(world[start]-world[idx]) == start - idx:
                return False

    return True

bfs(0)

print(rst)
