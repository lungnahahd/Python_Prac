# N-Queen (9663)
## 난이도 : 중

import sys
input = sys.stdin.readline

n = int(input())
rst = 0

def get_node(before_x, before_y):
    if before_x >= n:
        return (before_y + 1, 0)
    else:
        return (before_y, before_x + 1)

def meet_quene(x, y, game_map):
    for y_idx in range(0, y):
        for x_idx in range(0, n):
            

def chk_queen(node_x, node_y, game_map, how_many):
    if (not game_map[node_x][node_y]):

        how_many += 1
        game_map[node_x][node_y] = True
    if how_many == n:
        return rst+1
    else:
        next_y, next_x = get_node(node_x, node_y)
        if next_y >= n:
            return rst
        return chk_queen(node_x, node_y, game_map)