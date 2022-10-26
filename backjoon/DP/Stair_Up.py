# 계단 오르기

size = int(input())

stairs = []
for _ in range(size):
    s = int(input())
    stairs.append(s)


two_step = False
if size == 1:
    answer = stairs[0]
else:
    dp = [[0,0,0] for _ in range(size-1)]
    dp[0][1] = stairs[0]
    for step in range(1,size-1):
        if two_step:
            dp[step][0] = max(dp[step-1][1:])
            two_step = False
        else:
            dp[step][0] = max(dp[step-1])
            if dp[step][0] == dp[step-1][2] and dp.count(dp[step-1]) == 1:
                two_step = True
            else:
                two_step = False
        dp[step][1] = dp[step-1][0] + stairs[step]
        dp[step][2] = dp[step-1][1] + stairs[step]

    # print(dp)
    if two_step:
        answer = stairs[-1] + dp[size-2][1]
    else:
        answer = stairs[-1] + max(dp[size-2][0],dp[size-2][1])
print(answer)
print(dp)
## 반례
# 10
# 3
# 5
# 10 
# 9
# 2
# 1
# 2
# 5
# 2
# 9
# 38
