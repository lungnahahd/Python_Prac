# 1,2,3 더하기 3
## 정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 구하기
## 합을 나타낼 때는 수를 1개 이상 사용
### 입력 : 첫 줄에 테스트 케이스의 개수 T가 입력되고 각 테스트 케이스가 한 줄로 입력
### 출력 : n을 1,2,3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력

import sys
input = sys.stdin.readline

divide = 1000000009

caseSize = int(input())

sum = [0 for i in range(1000001)]

sum[1] = 1
sum[2] = 2
sum[3] = 4

for i in range(4,1000001):
    sum[i] = sum[i-1] + sum[i-2] + sum[i-3]

result = []

for i in range(caseSize):
    n = int(input())
    result.append(sum[n])

print(result)