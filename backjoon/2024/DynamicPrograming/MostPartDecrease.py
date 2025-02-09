# 가장 긴 감소하는 부분 수열
## 수열이 주어졌을 때, 가장 긴 감소하는 부분 수열 구하기
### 입력 : 첫 줄에 수열이 입력되고, 두번째 줄에 수열 전체가 주어짐
### 출력 : 가장 긴 감소하는 부분 수열의 길이 출력

import sys

input = sys.stdin.readline

size = int(input())
list = input().split() # 수열 입력 받기

# 각 수열에서 감소하는 수열을 세는 경우
result = [1 for i in range(size)]
temp = 0
# 각 수열의 수에서 최대 감소 부분 수열을 세기
# 각 수열에서 최대 부분을 카운트해서 그것보다 작은 경우에서는 수열을 +1을 카운트해서 세주기
for i in range(1,size):
    temp +=1
    stand = int(list[i])
    for j in range(i):
        if int(list[j]) > int(list[i]):
            temp = result[j] + 1
            if result[i] < temp:
                result[i] = temp
print(max(result))