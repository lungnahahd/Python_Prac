# 소수의 곱 (2014)
## 난이도 : 골드 1

import sys 
input = sys.stdin.readline

decimal_count, find_location = list(map(int, input().split()))
decimal_nums = list(map(int, input().split()))
check_decimal = set()
check_decimal.add(1)

for target in range(2, 2**31 + 1):
    for num in decimal_nums:
        if target % num == 0:
            if target // num in check_decimal:
                check_decimal.add(target)
                find_location -= 1
                break
    if find_location == 0:
        print(target)
        break
