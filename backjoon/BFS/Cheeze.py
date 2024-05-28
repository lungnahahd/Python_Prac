# 치즈 (2636)
## 난이도 : 골드 4

import sys
import copy
from collections import deque

input = sys.stdin.readline
move_r = [0,-1,0,+1]
move_c = [-1,0,+1,0]

row_size, col_size = list(map(int, input().split()))

area = []
time = 0
total_cheeze = 0
out_cheeze_cnt = 0

for _ in range(row_size):
    temp = list(map(int, input().split()))
    total_cheeze += temp.count(1)
    area.append(temp)

# 바깥 쪽에서 공기와 닿아있는 부분을 체크하는 함수
def find_air(graph, start_r, start_c):
    global visited
    #out_case = copy.deepcopy(graph) # 벽과 닿아 있는 경우 : -1

    can_go = deque([(start_r, start_c)])

    while can_go:
        now_r, now_c = can_go.popleft()
        for idx in range(4):
            next_r, next_c = now_r + move_r[idx], now_c + move_c[idx]
            if 0 <= next_r < row_size and 0 <= next_c < col_size:
                if graph[next_r][next_c] == 0 and not visited[next_r][next_c] :
                    graph[next_r][next_c] = -1
                    visited[next_r][next_c] = True
                    can_go.append((next_r, next_c))
    
    return graph


def get_rid_cheeze(graph, start_r, start_c):
    global visited, time, out_cheeze_cnt
    
    out_cheeze = set()
    can_go = deque([(start_r, start_c)])


    while can_go:
        now_r, now_c = can_go.popleft()
        for chk_idx in range(4):
            chk_r, chk_c = now_r + move_r[chk_idx], now_c + move_c[chk_idx]
            if 0 <= chk_r < row_size and 0 <= chk_c < row_size:
                if graph[chk_r][chk_c] == -1:
                    out_cheeze.add((now_r, now_c))
                if graph[chk_r][chk_c] == 1 and not visited[chk_r][chk_c]:
                    visited[chk_r][chk_c] = True
                    can_go.append((chk_r, chk_c))
    
    out_cheeze_cnt += len(out_cheeze)
    for out_r, out_c in out_cheeze:
        graph[out_r][out_c] = -1
    return graph




for idx in range(col_size):
    area[0][idx] = -1
    area[row_size-1][idx] = -1
for idx in range(row_size):
    area[idx][0] = - 1
    area[idx][col_size-1] = -1

while total_cheeze > 0:
    out_cheeze_cnt = 0
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    for r in range(row_size):
        for c in range(col_size):
            if area[r][c] == -1 and not visited[r][c]:
                visited[r][c] = True
                area = find_air(area, r,c)
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    for r in range(row_size):
        for c in range(col_size):
            if area[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                area = get_rid_cheeze(area,r,c)
    total_cheeze -= out_cheeze_cnt
    time += 1
                

print(time)
print(out_cheeze_cnt)