# 오르막 수
## 수의 자리가 오름차순을 아루는 수를 의미하며 인접한 수가 같아도 오름차순으로 인정
## 수의 길이 N 이 주어졌을 때, 오르막 수의 개수를 구하기
### 입력 : 첫 줄에 N 입력
### 출력 : 첫 줄에 길이가 N 인 오르막 수으 개수를 10,007로 나눈 나머지를 출력

import sys

input = sys.stdin.readline

divideNum = 10007
getNum = int(input())

case = [[1 for i in range(10)] for j in range(1001)]

for i in range(2,1001):
    for j in range(1,10):
        case[i][j] = (case[i-1][j] % divideNum) + (case[i][j-1] % divideNum)
result = 0
for i in range(10):
    result = result + case[getNum][i]

print(result % divideNum)