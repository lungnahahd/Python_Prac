# 마법사 상어와 토네이도 (20057)
## 난이도 : 골드 3

import sys
import math
input = sys.stdin.readline

cnt = int(input())
now_row, now_col = cnt // 2, cnt // 2
land = []
for _ in range(cnt):
    temp = list(map(int, input().split()))
    land.append(temp)

move_row = [0,+1,0,-1]
move_col = [-1,0,+1,0]
move_cnt = 0
direction = 0
left = [(0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02), (-1, 1, 0.01), (1, 1, 0.01)]
down = [(-y,x,cost) for x, y, cost in left]
right = [(x,-y,cost) for x, y, cost in left]
up = [(-x,y,cost) for x,y,cost in left]
way = {0: left, 1 : down , 2: right, 3: up}


out_result = 0
while cnt > now_row >= 0 and cnt > now_col >= 0:
    if direction > 3 :
        direction = 0
    end_row = now_row + move_row[direction] * (move_cnt // 2 + 1)
    end_col = now_col + move_col[direction] * (move_cnt // 2 + 1)
    #print(end_row, end_col)
    while end_row != now_row or end_col != now_col:
        now_row += move_row[direction]
        now_col += move_col[direction]

        if now_row < 0 or now_col < 0 or now_row >= cnt or now_col >=  cnt:
            break

        
        remain = 0
        for range_row, range_col, cost in way[direction]:
            temp_row = range_row + now_row
            temp_col = range_col + now_col
            temp_cost = math.floor(land[now_row][now_col] * cost)
            remain += temp_cost
            if 0 <= temp_row < cnt and 0 <= temp_col < cnt:
                land[temp_row][temp_col] += temp_cost
            else:
                out_result += temp_cost
        remain_row = now_row + move_row[direction] 
        remain_col = now_col + move_col[direction] 
        if 0 <= remain_row < cnt and 0 <= remain_col < cnt :
            land[remain_row][remain_col] += (land[now_row][now_col] - remain)
        else:
            out_result += (land[now_row][now_col] - remain)
        land[now_row][now_col] = 0

    move_cnt += 1
    direction += 1

print(out_result)