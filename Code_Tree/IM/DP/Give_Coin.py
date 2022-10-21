# 동전 거슬러주기

import sys

INT_MAX = sys.maxsize

coin, money = map(int,input().split())

kind = list(map(int,input().split()))

num = [INT_MAX for _ in range(10001)]

for i in kind:
    num[i] = 1

for idx in range(1,money+1):
    for basic in kind:
        if idx - basic > 0:
            num[idx] = min(num[idx],num[basic] + num[idx-basic])

if num[money] == INT_MAX:
    print(-1)
else:
    print(num[money])