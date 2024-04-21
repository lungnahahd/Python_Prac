# Byte Coin (17521)
## 난이도 : 실버 4

import sys
input = sys.stdin.readline

cnt_day, money = list(map(int, input().split()))
chart = []
for _ in range(cnt_day):
    val = int(input())
    chart.append(val)
chart.append(0)

buy_coin = 0
for idx in range(cnt_day):
    now_val, next_val = chart[idx], chart[idx+1]
    if now_val < next_val and buy_coin ==0 :
        buy_coin = money // now_val
        money -= (now_val * buy_coin)
    elif now_val > next_val and buy_coin != 0:
        money += buy_coin * now_val
        buy_coin = 0
        
print(money)