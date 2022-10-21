# 부분 수열의 합이 m
## 답이 도저히 안 나올 때는 "역전" 하는 것 잊지 말기!!!

import sys

INT_MAX = sys.maxsize

num, plus_sum = map(int,input().split())
l_num = list(map(int,input().split()))

result = [INT_MAX for _ in range(plus_sum+1)]

for i in l_num:
    result[i] = 1

for n in l_num:
    for idx in range(plus_sum,0,-1):
        if idx - n > 0:
            result[idx] = min(result[idx],result[idx-n] + 1)

print(result[plus_sum])