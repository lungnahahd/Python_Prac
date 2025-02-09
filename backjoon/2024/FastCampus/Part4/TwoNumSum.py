# 두 수의 합 (실버 3)
## 난이도 : 실버 3

import sys

input = sys.stdin.readline

cnt = int(input())
num_list = list(map(int, input().split()))
answer = int(input())
result = 0

num_list.sort()
start, end = 0, cnt-1

while start < end:
    mid_answer = num_list[start] + num_list[end]
    if mid_answer == answer:
        result += 1
        end -= 1
    elif mid_answer < answer:
        start += 1
    else:
        end -= 1

print(result)