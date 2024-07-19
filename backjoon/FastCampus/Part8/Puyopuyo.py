# 뿌요뿌요 (11559)
## 난이도 : 골드 4


import sys
from collections import deque
#input = sys.stdin.readline


# col 6 줄, row 12개 
puyo_map = []
for _ in range(12):
    line = list(input())
    puyo_map.append(line)

move_r = [-1,0,+1,0]
move_c = [0,-1,0,+1]
total_visited = [[False for _ in range(6)] for _ in range(12)]


# 연속된 색상의 뿌요뿌요를 제거하는 부분 
def find_same_puyo(start_row, start_col):
    global total_visited

    visited = [[False for _ in range(6)] for _ in range(12)] # 뿌요뿌요 방문 여부를 확인하는 배열
    visited[start_row][start_col] = True
    total_visited[start_row][start_col] = True
    same_color = []
    same_color.append((start_row, start_col))
    go_list = deque([(start_row, start_col)])
    now_color = puyo_map[start_row][start_col]
    while go_list:
        now_r, now_c = go_list.popleft()
        for m_idx in range(4):
            next_r, next_c = now_r + move_r[m_idx], now_c + move_c[m_idx]
            if (0 <= next_r < 12 and 0 <= next_c < 6):
                if not visited[next_r][next_c] and now_color == puyo_map[next_r][next_c]:
                    visited[next_r][next_c] = True
                    total_visited[start_row][start_col] = True
                    go_list.append((next_r, next_c))
                    same_color.append((next_r, next_c))
    return same_color

# 뿌요뿌요의 연속된 같은 색상을 제거하는 함수
def remove_same_puyo(same_list):
    global puyo_map
    
    for row, col in same_list:
        puyo_map[row][col] = "X"    # 연속된 뿌요뿌요를 제거

# 뿌요뿌요를 중력의 영향으로 빈칸을 이동시키는 함수
def move_down_puyo():
    global puyo_map

    for col in range(6):
        for row in range(11, 0, -1):
            if puyo_map[row][col] == "X":
                puyo_map[row][col] = "."
                for idx in range(row-1,0,-1):
                    if puyo_map[idx][col] != "X" and puyo_map[idx][col] != "." :
                        puyo_map[row][col] = puyo_map[idx][col]
                        puyo_map[idx][col] = "."
                        break
        if puyo_map[0][col] == "X":
            puyo_map[0][col] = "."
    
    
keep_going = True
answer = 0
while keep_going:
    keep_going = False
    for row in range(12):
        for col in range(6):
            if not total_visited[row][col] and puyo_map[row][col] != ".":
                same_list = find_same_puyo(row, col)
                if len(same_list) >= 4:
                    remove_same_puyo(same_list)
                    move_down_puyo()
                    answer += 1
                    keep_going = True
                if keep_going:
                    break
        if keep_going:
            break
print(answer)