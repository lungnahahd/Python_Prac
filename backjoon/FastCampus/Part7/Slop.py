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

for idx in range(size):
    before = area[idx][0]
    cnt = 0
    for row_idx in range(size):
        if before == area[idx][row_idx]:
            cnt += 1
        else:
            row_dq.append((before, cnt))
            before = area[idx][row_idx]
            cnt = 1
    row_dq.append((before,cnt))
    before_val = -1
    before_long = 0
    no_way_go = False
    while row_dq:
        pass_val = False
        now_val, now_long = row_dq.popleft()
        if now_long == size:
            break
        if before_val != -1 and now_val - before_val == 1:
            if before_long >= slop_long:
                pass_val = True
        before_val = now_val
        before_long = now_long
        if (pass_val):
            continue
        if len(row_dq) == 0:
            no_way_go = True
            break
        else:
            if before_val - row_dq[0][0] == 1:
                if row_dq[0][1] >= slop_long:
                    before_val, before_long = row_dq.popleft()
                    continue
                else:
                    no_way_go = True
                    break
            else:
                if row_dq[0][0] - before_val == 1:
                    if before_long >= slop_long:
                        before_val, before_long = -1, 0
                        continue
                no_way_go = True
                break
    if not no_way_go:
        result += 1

for idx in range(size):
    before = area[0][idx]
    cnt = 0
    for col_idx in range(size):
        if before == area[col_idx][idx]:
            cnt += 1
        else:
            col_dq.append((before, cnt))
            before = area[col_idx][idx]
            cnt = 1
    col_dq.append((before, cnt))
    before_val = -1
    before_long = 0
    no_way_go = False
    remain = 0
    while col_dq:
        pass_val = False
        now_val, now_long = col_dq.popleft()
        if now_long + remain == size:
            break
        if before_val != -1 and now_val - before_val == 1:
            if before_long >= slop_long:
                pass_val = True
        before_val = now_val
        before_long = now_long
        remain += now_long
        if (pass_val):
            continue
        if len(col_dq) == 0:
            no_way_go = True
            break
        else:
            if before_val - col_dq[0][0] == 1:
                if col_dq[0][1] >= slop_long:
                    before_val, before_long = col_dq.popleft()
                    continue
                else:
                    no_way_go = True
                    break
            else:
                if col_dq[0][0] - before_val == 1:
                    if before_long >= slop_long:
                        before_val, before_long = -1, 0
                        continue
                no_way_go = True
                break
    if not no_way_go:
        print(col_idx, idx)
        result += 1
    


print(result)
    