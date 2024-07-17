
import sys
import heapq
input = sys.stdin.readline


row_size, col_size = list(map(int, input().split()))

move_r = [-1,0,+1,0]
move_c = [0,-1,0,+1]
water_location = []
# 0이면 비어있는 경우,-1 이면 돌이기에 막기, 1 이면 물 처리, 2이면 비버굴(도착지)
world_map = [[0 for _ in range(col_size)] for _ in range(row_size)]


result = sys.maxsize
start_row, start_col, end_row, end_col = 0,0,0,0
for row_idx in range(row_size):
    temp = list(input())
    for col_idx in range(col_size):
        if temp[col_idx] == "X":
            world_map[row_idx][col_idx] = -1
        elif temp[col_idx] == "D":
            world_map[row_idx][col_idx] = 2
            end_row, end_col = row_idx, col_idx
        elif temp[col_idx] == "*":
            world_map[row_idx][col_idx] = 1
            water_location.append((row_idx, col_idx))
        elif temp[col_idx] == "S":
            start_row, start_col = row_idx, col_idx

def water_move(location):
    global world_map
    new_location = []
    for now_r, now_c in location:
        for m_idx in range(4):
            next_r, next_c = now_r + move_r[m_idx], now_c + move_c[m_idx]
            if 0 <= next_r < row_size and 0 <= next_c < col_size:
                if world_map[next_r][next_c] == 0:
                    world_map[next_r][next_c] = 1
                    new_location.append((next_r, next_c))
    return new_location

def bfs(row, col):
    global water_location, result
    visited = []
    animal_move_list = []
    visited.append((row, col))
    heapq.heappush(animal_move_list, (0, row, col))
    while animal_move_list:
        water_location = water_move(water_location)
        now_time, now_r, now_c = heapq.heappop(animal_move_list)
        for m in range(4):
            next_r, next_c = move_r[m] + now_r, move_c[m] + now_c
            if 0 <= next_r < row_size and 0 <= next_c < col_size:
                if world_map[next_r][next_c] == 2:
                    result = min(result, now_time + 1)
                elif world_map[next_r][next_c] == 0:
                    if (next_r, next_c) not in visited:
                        visited.append((next_r, next_c))
                        heapq.heappush(animal_move_list, (now_time+1, next_r, next_c))

bfs(start_row, start_col)

if (result == sys.maxsize):
    print("KAKTUS")
else:
    print(result)