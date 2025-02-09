# 거스름돈 (5585)
## 난이도 : 하

import sys
input = sys.stdin.readline

money = int(input())

origin = 1000

back_money = origin - money
coins = [500, 100, 50, 10, 5, 1]

rst = 0 
for coin in coins:
    rst += (back_money // coin)
    back_money = back_money % coin

print(rst)