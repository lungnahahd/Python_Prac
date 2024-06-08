# 01 타일 (1904)
## 난이도 : 실버 3

import sys
input = sys.stdin.readline

value = [0,1,2]
N = int(input())

if (N < 3):
    print(value[N])
else:
    for idx in range(2,N):
        next_val = (value[idx] + value[idx-1]) % 15746
        value.append(next_val)
    print(value[N])