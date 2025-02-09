# 골드바흐의 추측 (6588)
## 난이도 : 실버 1

import sys
import math

input = sys.stdin.readline
max_num = 1000000
eratos = [True for _ in range(max_num + 1)]
time_short = []

#for num in range(2, int(math.sqrt(max_num)) + 1):
for num in range(2, max_num+1):
    if eratos[num]:
        time_short.append(num)
        multi = 2
        next_num = num * multi
        while next_num <= max_num:
            eratos[next_num] = False
            multi += 1
            next_num = num * multi
while True:
    find_num = int(input())
    if find_num == 0:
        break
    result_a, result_b = 0, 0
    for num in time_short:
        if num >= find_num:
            break
        if eratos[find_num- num]:
            result_a, result_b = num, find_num - num
            break

    if (result_a == 0 or result_b == 0):
        print("Goldbach's conjecture is wrong.")
    else:
        print(str(find_num) + " = " + str(result_a) + " + " + str(result_b))