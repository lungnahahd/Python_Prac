# 합분해
## 0 부터 N 까지의 정수 K 개를 더해서 그 합이 N 이 되는 경우의 수를 구하기
## 덧셈의 순서가 바뀐 경우는 다른 경우로 인정하며 또한 한 개의 수를 여러 번 쓸 수 있음
### 입력 : 첫 줄에 두 정수 N 과 K 가 입력
### 출력 : 첫 줄에 답을 1,000,000,000 으로 나눈 나머지를 출력

import sys
input = sys.stdin.readline

largeResult = 1000000000

resultArray = [[0] * 201 for i in range(201)]

for j in range(1,201):
    resultArray[1][j] = 1
for i in range(1,201):
    resultArray[i][1] = i

for i in range(2,201):
    for j in range(2, 201):
        resultArray[i][j] = resultArray[i][j-1] + resultArray[i-1][j]


n, k = input().split()
n = int(n)
k = int(k)

print(resultArray[k][n] % largeResult)