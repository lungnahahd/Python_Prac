# 계단 오르기

size = int(input())

stairs = []
for _ in range(size):
    s = int(input())
    stairs.append(s)

dp = [[0,0,0] for _ in range(size-1)]
dp[0][1] = stairs[0]
for step in range(1,size-1):
    dp[step][0] = max(dp[step-1])
    dp[step][1] = dp[step-1][0] + stairs[step]
    dp[step][2] = dp[step-1][1] + stairs[step]

# print(dp)

answer = stairs[-1] + max(dp[size-2][0],dp[size-2][1])
print(answer)