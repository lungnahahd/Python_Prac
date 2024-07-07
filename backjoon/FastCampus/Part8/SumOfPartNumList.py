# 부분수열의 합 (1182)
## 난이도 : 실버 2

import sys
input = sys.stdin.readline 

count, target = list(map(int, input().split()))
num_list = list(map(int, input().split()))

result = 0

def check_target(sum_num, start):
    global result
    if sum_num == target:
        result += 1
    else:
        for idx in range(start, len(num_list)):
            check_target(sum_num+num_list[idx], idx+1)

check_target(0,0)
print(result)