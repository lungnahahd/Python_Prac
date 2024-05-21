# 마법사 상어와 비바라기 (21610)
## 난이도 : 골드 5

import sys

input = sys.stdin.readline

area_size, move_cnt = list(map(int, input().split()))
area = []

# 구름의 움직임 배열 
move_row = [0,-1,-1,-1,0,1,1,1]
move_col = [-1,-1,0,1,1,1,0,-1]

row_water_copy = [-1, +1, -1, +1]
col_water_copy = [-1, -1, +1, +1]

for _ in range(area_size):
    road = list(map(int, input().split()))
    area.append(road)
# 초기 구름
cloud = [(area_size-1, 0), (area_size-1, 1), (area_size-2, 0), (area_size-2, 1)]

for _ in range(move_cnt):
    way, dist = list(map(int, input().split()))
    way -= 1
    next_cloud = []
    for r, c in cloud:
        next_r, next_c = r, c
        for _ in range(dist):
            next_r, next_c = next_r + move_row[way], next_c + move_col[way]
            if 0 > next_c:
                next_c += area_size
            elif next_c >= area_size:
                next_c -= area_size
            if 0 > next_r:
                next_r += area_size
            elif next_r >= area_size:
                next_r -= area_size
        if 0 <= next_r < area_size and 0 <= next_c < area_size:
            area[next_r][next_c] += 1
            next_cloud.append((next_r, next_c))

    cloud = next_cloud
    for r, c in cloud:
        for idx in range(4):
            copy_r, copy_c = r + row_water_copy[idx], c + col_water_copy[idx]
            if 0 <= copy_r < area_size and 0 <= copy_c < area_size and area[copy_r][copy_c] != 0:
                area[r][c] += 1
    now_cloud = []
    cloud = set(cloud)
    for r in range(area_size):
        for c in range(area_size):
            if (r,c) not in cloud and area[r][c] >= 2:
                now_cloud.append((r,c))
                area[r][c] -= 2
    cloud = now_cloud

result = 0
for r in range(area_size):
    for c in range(area_size):
        result += area[r][c]
print(result)