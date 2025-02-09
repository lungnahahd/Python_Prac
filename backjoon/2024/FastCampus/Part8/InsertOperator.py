# 연산자 끼워넣기 (14888)
## 난이도 : 실버 1

import sys
input = sys.stdin.readline

operator = ["+", "-", "*", "/"]
num_cnt = int(input())
num_list = list(map(int, input().split()))
temp_list = list(map(int, input().split()))
operator_list = []

for idx in range(4):
    for _ in range(temp_list[idx]):
        operator_list.append(idx)

big_num, small_num = -1000000000, 1000000000

def calculate(op, num_one, num_two):
    result = 0
    if op == 0:
        result = num_one + num_two
    elif op == 1:
        result = num_one - num_two
    elif op == 2:
        result = num_one * num_two
    else:
        if num_one < 0 and num_two > 0:
            result = -(-num_one // num_two)
        else:
            result = num_one // num_two
    return result

def operate(already_use, mid_rst):
    global big_num, small_num
    if len(already_use)+1 == num_cnt:
        big_num = max(big_num, mid_rst)
        small_num = min(small_num, mid_rst)
    else:
        for idx in range(len(operator_list)):
            if idx not in already_use:
                already_use.add(idx)
                operate(already_use, calculate(operator_list[idx], mid_rst, num_list[len(already_use)]))
                already_use.remove(idx)
operate(set(), num_list[0])

print(big_num)
print(small_num)