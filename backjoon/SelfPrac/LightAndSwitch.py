# 전구와 스위치 (2138)
## 난이도 : 골드 4

import sys
import copy

count_light = int(input())
now_light = list(input())
want_light = list(input())

answer = sys.maxsize

for now_case in range(2):
    temp = 0
    temp_light = copy.deepcopy(now_light)
    if now_case == 1:
        temp_light[0] = "0" if temp_light[0] == "1" else "1"
        temp_light[1] = "0" if temp_light[1] == "1" else "1"
        temp += 1
    for idx in range(1, count_light):
        if temp_light[idx-1] != want_light[idx-1]:
            temp_light[idx-1] = want_light[idx-1]
            temp_light[idx] =  "0" if temp_light[idx] == "1" else "1"
            if (idx+1  < count_light):
                temp_light[idx+1] = "0" if temp_light[idx+1] == "1" else "1"
            temp += 1
    if temp_light[-1] == want_light[-1]:
        answer = min(answer, temp)
    
if answer == sys.maxsize:
    answer = -1
print(answer)