# 마법사 상어와 파이어볼 (20056)
## 난이도 : 골드 4

import sys
from collections import deque
input = sys.stdin.readline

area_size, cnt_fire_ball, cnt_doing = list(map(int, input().split()))
area = [[deque([]) for _ in range(area_size)] for _ in range(area_size)]


row_move = [-1,-1, 0,+1,+1,+1, 0,-1]
col_move = [ 0,+1,+1,+1, 0,-1,-1,-1]


# 파이어볼 입력 정보
# (row, col, weight, speed, distance)

for _ in range(cnt_fire_ball):
    row, col, weight, speed, distance = list(map(int, input().split()))
    area[row-1][col-1].append([weight, speed, distance])

def fire_sperate(area):
    new_area = [[deque([]) for _ in range(area_size)] for _ in range(area_size)]
    for r in range(area_size):
        for c in range(area_size):
            if len(area[r][c]) != 0:
                if len(area[r][c]) == 1:
                    new_area[r][c].append(area[r][c][0])
                else:
                    fire_count = len(area[r][c])
                    odd = 0
                    even = 0
                    sum_weight, sum_speed, sum_dist = 0,0,0
                    for weight, speed, distance in area[r][c]:
                        sum_weight += weight
                        sum_speed += speed
                        if distance % 2 == 0:
                            even += 1
                        else:
                            odd += 1
                        sum_dist += distance
                    new_weight = sum_weight // 5
                    new_speed = sum_speed // fire_count
                    if new_weight != 0:
                        if ( even != 0 and odd == 0 ) or (even ==0 and odd != 0):
                            for new_dist in range(0,7,2):
                                new_area[r][c].append([new_weight, new_speed, new_dist])
                        else:
                            for new_dist in range(1,8,2):
                                new_area[r][c].append([new_weight, new_speed, new_dist])    
    return new_area


def fire_move(area):
    new_area = [[deque([]) for _ in range(area_size)] for _ in range(area_size)]
    for r in range(area_size):
        for c in range(area_size):
            if len(area[r][c]) != 0:
                for weight, speed, dist in area[r][c]:
                    next_row = (r + row_move[dist] * speed) % area_size
                    next_col = (c + col_move[dist] * speed) % area_size
                    new_area[next_row][next_col].append([weight, speed, dist])
    return new_area


for _ in range(cnt_doing):
    area = fire_move(area)
    area = fire_sperate(area)

result = 0
for r in range(area_size):
    for c in range(area_size):
        if len(area[r][c]) != 0:
            for weight, _, _ in area[r][c]:
                result += weight
print(result)