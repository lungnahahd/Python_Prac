# 1,2,3 더하기
## 정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수 구하기
### 입력 : 첫 줄에 테스트의 갯수가 입력되고, 차례로 정수 n 이 입력 (입력은 11보다 작은 양수)
### 출력 :  줄에 정수 n 을 1,2,3의 합으로 나타내는 방법의 수를 출력

##### 생각 : 타일링 DP와 유사한 개념으로 문제 접근하기 -> 주어진 수로 이루어진 크기에서 1,2,3 타일을 가지고 채우는 경우의 수

import sys
input = sys.stdin.readline

size = int(input())

sumList = [0 for i in range(12)]
sumList[1] = 1
sumList[2] = 2
sumList[3] = 4

for i in range(4,12):
    sumList[i] = sumList[i - 1] + sumList[i - 2] + sumList[i - 3] 


resultList = []

for i in range(size):
    n = int(input())
    resultList.append(sumList[n])

for i in resultList:
    print(i)