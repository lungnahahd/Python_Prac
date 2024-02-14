# 가장 긴 증가하는 부분 수열 (11053)
## 난이도 : 하

import sys

input = sys.stdin.readline

cnt = int(input())
dp = [1 for _ in range(cnt)]
num_list = list(map(int, input().split()))

for i in range(cnt):
    for j in range(i):
        if num_list[j] < num_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))