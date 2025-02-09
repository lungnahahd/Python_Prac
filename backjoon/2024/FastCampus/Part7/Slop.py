# 경사로 (14890)
## 난이도 : 골드 4

import sys
from collections import deque
input = sys.stdin.readline 


size, slop_long = list(map(int, input().split()))
area = []
for _ in range(size):
    temp = list(map(int, input().split()))
    area.append(temp)

row_dq = deque([])
col_dq = deque([])

result = 0 

def checkCanGo(road):
    dq = deque([])
    before = road[0]
    cnt = 0
    for idx in range(size):
        if before == road[idx]:
            cnt += 1
        else:
            dq.append((before, cnt))
            before = road[idx]
            cnt = 1
    dq.append((before, cnt))
    before_val = -1
    before_long = 0
    if len(dq) == 1:
        return True
    else:
        before_slop_have = False
        while dq:
            now_val, now_long = dq.popleft()
            if before_val != -1:
                if now_val - before_val == 1:
                    if before_long >= slop_long and not before_slop_have:
                        before_val = now_val
                        before_long = now_long
                        before_slop_have = False
                    else:
                        return False
                elif before_val - now_val == 1:
                    if now_long >= slop_long :
                        if now_long - slop_long >= slop_long:
                            before_slop_have = False
                        else:
                            before_slop_have = True
                        before_val = now_val
                        before_long = now_long
                    else:
                        return False
                else:
                    return False
            else:
                before_long = now_long
                before_val = now_val
        return True
            
for r in range(size):
    now_road = area[r]
    if checkCanGo(now_road):
        result += 1
new_area = []
for c in range(size):
    temp = []
    for r in range(size):
        temp.append(area[r][c])
    new_area.append(temp)
  

for r in range(size):
    now_road = new_area[r]
    if checkCanGo(now_road):
        result += 1

print(result)