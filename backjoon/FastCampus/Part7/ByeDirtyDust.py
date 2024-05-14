# 미세먼지 안녕 ! (17144)
## 골드 4

import sys
input = sys.stdin.readline

row_size, col_size, time = list(map(int, input().split()))
room = []
find_machine = False
machine_up_row, machine_up_col, machine_down_row, machine_down_col = 0,0,0,0
up_spin =   ["right", "up", "left", "down"]
down_spin = ["right", "down", "left", "up"]
spin_dict_row = {"right": 0, "up": -1, "down": +1, "left": 0}
spin_dict_col = {"right": +1, "up": 0, "down": 0, "left": -1}


for row in range(row_size):
    temp = input()
    mid = list(map(int, temp.split()))
    room.append(temp)
    if not find_machine:
        if temp.find('-1') != -1:
            col = mid.index(-1)
            machine_up_row, machine_down_row = row, row + 1
            machine_up_col, machine_down_col = col, col
            find_machine = True



def spin_clean_wind(row, col, room, spin_array):
    after_room = [[0 for _ in range(col_size)] for _ in range(row+1)]
    after_room[row][col] = -1
    next_r, next_c = row, col
    for move_idx in range(4):
        way = spin_array[move_idx]
        move_r, move_c = spin_dict_row[way], spin_dict_col[way]
        while 0 <= move_r + next_r < row + 1 and 0 <= move_c + next_c < col_size:
            if next_r != row and next_c != col :
                after_room[next_r + move_r][next_c + move_c] = room[next_r][next_c]
            next_r += move_r
            next_c += move_c
    after_room[row][col] = -1
    return after_room

def spread_dust(room, m_r, m_c):
    after_room = [[0 for _ in range(col_size)] for _ in range(row_size)]
    move_row = [-1,0,+1,0]
    move_col = [0,+1,0,-1]
    for r_idx in range(row_size):
        for c_idx in range(col_size):
            if room[r_idx][c_idx] != 0 and room[r_idx][c_idx] != -1:
                count = 0
                move_val = room[r_idx][c_idx] // 5
                for m_idx in range(4):
                    next_r, next_c = r_idx + move_row[m_idx], c_idx + move_col[m_idx]
                    if 0 <= next_r < row_size and 0 <= next_c < col_size:
                        after_room[next_r][next_c] += move_val
                        count += 1
                after_room[r_idx][c_idx] = room[r_idx][c_idx] - move_val * count
    after_room[m_r][m_c] = -1
    after_room[m_r+1][m_c] = -1