# 초콜릿 식사(2885)
## 난이도 : 실버 2 

import sys
import math
input = sys.stdin.readline

want_size = int(input())

#print(math.sqrt(want_size))
#print(int(math.sqrt(want_size)))

answer = 0

def find_two_power(num):
    idx = 0
    while True:
        if num <= 2**idx:
            return idx
            break
        idx += 1

def solve_diet(want):
    global answer
    now_two_value = find_two_power(want)
    if 2**now_two_value == want:
        answer += 1
        return
    big_two_value = now_two_value - 1
    big_value = 2**(big_two_value)
    now_two_value = find_two_power(want - big_value)
    if 2**now_two_value == (want-big_value):
        small_two_value = now_two_value
    else:
        small_two_value = now_two_value - 1
    #print(big_two_value, small_two_value)
    answer += (big_two_value - small_two_value)
    solve_diet(want - big_value)

big_num_answer = find_two_power(want_size)
if 2**big_num_answer == want_size:
    print(2**big_num_answer, 0)
else:
    solve_diet(want_size)
    print(2**big_num_answer, answer)