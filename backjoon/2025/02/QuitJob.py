# 퇴사 (14501)
## 난이도 : 실버 3

import sys
input = sys.stdin.readline 

day_cnt = int(input())
detail = [[]]
answer = 0

for _ in range(day_cnt):
    now_long, now_val = list(map(int, input().split()))
    detail.append([now_long, now_val])


def back_track(now_time, now_val):
    global answer
    print(now_time, now_val)
    # if now_time > day_cnt:
    #     answer = max(answer, now_val)
    #     return
    
    if now_time == day_cnt:
        if detail[now_time][0] == 1:
            now_val += detail[now_time][1]
        answer = max(answer, now_val)
        return

    for idx in range(now_time, day_cnt+1):
        if now_time + detail[idx][0] > day_cnt+1:
            #answer = max(answer, now_val)
            continue
        else:
            back_track(now_time  + detail[idx][0], now_val + detail[idx][1])

back_track(1,0)
print(answer)
