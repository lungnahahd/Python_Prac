# 알파벳
from collections import deque
import copy

r_size, c_size = map(int, input().split())
can_go = []
moves = [[+1, 0], [0, +1], [-1, 0], [0, -1]]
visited = [[False for _ in range(c_size)] for _ in range(r_size)]
answer = 0
for _ in range(r_size):
    temp = list(input())
    can_go.append(temp)


def bfs(r, c, before, val):
    global visited
    global answer
    n_before = copy.deepcopy(before)
    for move in moves:
        next_r, next_c = move[0] + r, move[1] + c
        if 0 <= next_r < r_size and 0 <= next_c < c_size:
            if can_go[next_r][next_c] in n_before:
                print(before)
                answer = max(answer, val)
                return
            #visited[next_r][next_c] = True
            n_before.add(can_go[next_r][next_c])
            print(next_r, next_c)
            bfs(next_r, next_c, n_before, val+1)
            #visited[next_r][next_c] = False
            n_before.remove(can_go[next_r][next_c])


before = set()
before.add(can_go[0][0])
visited[0][0] = True
bfs(0, 0, before, 1)
print(answer)
