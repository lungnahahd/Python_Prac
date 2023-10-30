# 둘 중 하나 잘 고르기
## Red 나 Blue를 적절하게 N개 씩만 선택해서 최대의 크기를 구하시오

n = int(input())
do_cnt = 2*n
reds, blues = [], []

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]


for _ in range(do_cnt):
    cards = list(map(int,input().split()))
    reds.append(cards[0])
    blues.append(cards[1])

for cnt in range(1, do_cnt+1):
    for chose in range(n+1):
        if (chose > cnt):
            break
        red, blue = chose, cnt - chose
        if (red > n or blue > n):
            continue
        if (red != 0):
            dp[red][blue] = max(dp[red][blue], dp[red-1][blue] + reds[cnt-1])
        if (blue != 0):
            dp[red][blue] = max(dp[red][blue], dp[red][blue-1] + blues[cnt-1])

print(dp[n][n])
