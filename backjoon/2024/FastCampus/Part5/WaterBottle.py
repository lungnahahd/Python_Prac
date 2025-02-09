# 물통 (14867)
## 골드 2

import sys
from collections import deque
input = sys.stdin.readline

A_bottle, B_bottle, a_remain, b_remain = list(map(int, input().split()))

already_make = set()
def bfs_get_water(a_water, b_water, count):
    global already_make

    save = deque([(a_water, b_water, count)])
    already_make.add((a_water, b_water))

    while save:
        now_a, now_b, now_cnt = save.popleft()
        if now_a == a_remain and now_b == b_remain:
            return now_cnt
        
        ## 1번 동작
        if now_a < A_bottle and (A_bottle, now_b) not in already_make:
            already_make.add((A_bottle, now_b))
            save.append((A_bottle, now_b, now_cnt+1))
        if now_b < B_bottle and (now_a, B_bottle) not in already_make:
            already_make.add((now_a, B_bottle))
            save.append((now_a, B_bottle, now_cnt+1))
        ## 1번 동작

        ## 2번 동작
        if now_a != 0 and (0, now_b) not in already_make:
            already_make.add((0,now_b))
            save.append((0,now_b, now_cnt+1))
        if now_b != 0 and (now_a, 0) not in already_make:
            already_make.add((now_a, 0))
            save.append((now_a, 0, now_cnt+1))        
        ## 2번 동작
        
        ## 3번 동작
        if now_b < B_bottle and now_a != 0:
            max_remain = B_bottle - now_b
            if max_remain >= now_a and (0, now_b+now_a) not in already_make:
                already_make.add((0, now_b + now_a))
                save.append((0, now_a+now_b, now_cnt+1))
            elif max_remain < now_a and (now_a-max_remain, B_bottle) not in already_make:
                already_make.add((now_a-max_remain, B_bottle))
                save.append((now_a-max_remain, B_bottle, now_cnt+1))
        if now_a < A_bottle and now_b != 0:
            max_remain = A_bottle - now_a
            if max_remain >= now_b and (now_a+now_b, 0) not in already_make:
                already_make.add((now_a + now_b, 0))
                save.append((now_a+now_b, 0, now_cnt+1))
            elif max_remain < now_b and (A_bottle, now_b- max_remain) not in already_make:
                already_make.add((A_bottle, now_b-max_remain))
                save.append((A_bottle, now_b-max_remain, now_cnt+1))
        
        ## 3번 동작 
    return -1

result = bfs_get_water(0,0,0)
print(result)