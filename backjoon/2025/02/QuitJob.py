# 퇴사 (14501)
## 난이도 : 실버 3

import sys
input = sys.stdin.readline 

day_cnt = int(input())
detail = [[]]
answer = [0 for _ in range(day_cnt + 2)]

for _ in range(day_cnt):
    now_long, now_val = list(map(int, input().split()))
    detail.append([now_long, now_val])


for day in range(1,day_cnt+1):
    now_day = detail[day][0] + day
    if now_day <= day_cnt + 1:
        for next_day in range(now_day, day_cnt + 2):
            answer[next_day] = max(answer[next_day], answer[day] + detail[day][1])

#print(answer)
print(max(answer))