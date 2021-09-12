# 가장 긴 증가하는 부분 수열
## 수열이 주어진 경우, 가장 긴 증가하는 부분 수열을 구하는 프로그램
### 입력 : 첫 줄에 수열의 크기가 주어지고, 둘째 줄에 수열이 입력
### 출력 : 첫 줄에 수열이 가장 긴 증가하는 부분 수열 길이 출력 

import sys
input = sys.stdin.readline

size = int(input()) # 수열의 크기
numList = input().split() # 수열을 입력

result = 0
for i in range(size):
    count = 1
    bigNum = int(numList[i])
    for j in range(i + 1,size):
        if bigNum < int(numList[j]):
            bigNum = int(numList[j])
            count += 1
    if count > result:
        result = count

print(result)