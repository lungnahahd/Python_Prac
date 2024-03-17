# 등수 매기기 (2012)
## 난이도 : 하

import sys

input = sys.stdin.readline

cnt = int(input())

max_int = 0
for num in range(1, cnt+1):
    max_int += num

for _ in range(cnt):
    temp = int(input())
    max_int -= temp

print(max_int)