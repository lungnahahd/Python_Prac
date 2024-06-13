# 골드바흐의 추측 (6588)
## 난이도 : 실버 1

import sys

input = sys.stdin.readline
max_num = 1000000
eratos = [True for _ in range(max_num + 1)]



for num in range(2, max_num+1):
    if eratos[num]:
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
    for num in range(2, find_num // 2 + 1):
        if eratos[num] and eratos[find_num-num]:
            result_a = num
            result_b = find_num - num
            break
    if (result_a == 0 or result_b == 0):
        print("Goldbach's conjecture is wrong.")
    else:
        print(str(find_num) + " = " + str(result_a) + " + " + str(result_b))