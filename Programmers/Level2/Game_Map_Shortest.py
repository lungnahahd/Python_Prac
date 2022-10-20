# 게임 맵 최단거리

from collections import deque
from copy import deepcopy

# (행, 열)
# BFS 활용!!
## 처음에는 DFS로 풀다가 꼬여버렸음...

row_move = [+1,0,-1,0]
col_move = [0,+1,0,-1]

def solution(maps):
    save_node = deque()
    row_max, col_max = len(maps)-1, len(maps[0])-1
    visited = set() # 방문 여부를 나타내는 set ->  시간 복잡도를 줄일 수 있음
    save_node.append((0,0)) # 큐를 활용한 BFS
    result_map = deepcopy(maps) # 정답을 위한 깊은 복사(안하고 그냥 파라미터 배열에 해도 무방할듯..)
    result_map[row_max][col_max] = -1
    visited.add((0,0))
    while save_node:
        row_now,col_now = save_node.popleft()
        for idx in range(4):
            row_next, col_next = row_now+row_move[idx], col_now+col_move[idx]
            if 0<=row_next<=row_max and 0<=col_next<=col_max and maps[row_next][col_next] == 1:
                if (row_next,col_next) not in visited:
                    visited.add((row_next,col_next))
                    result_map[row_next][col_next] = result_map[row_now][col_now] + 1
                    save_node.append((row_next,col_next))
    

    return result_map[row_max][col_max]

    

# 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

# -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))