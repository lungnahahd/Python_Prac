# 1로 만들기
## 정수가 3으로 나눠지면 3으로 나누기/정수가 2로 나눠지면 2로 나누기/1빼기
## 위의 3개의 연산 중 하나를 수행해서 주어진 정수를 1로 만드는 연산의 최소 횟수 구하기
### 입력 : 첫 줄에 1로 만들고자 하는 정수를 입력
### 출력 : 첫 줄에 입력된 정수를 1로 만드는 연산 횟수의 최소 값 출력

import sys
input = sys.stdin.readline

beforeOne = int(input())

countList = [0 for i in range(beforeOne + 1)]

for i in range(2, beforeOne + 1):
    countList[i] = countList[i-1] + 1

    if i % 3 == 0:
        countList[i] = min(countList[i], countList[i // 3] + 1)
    if i % 2 == 0:
        countList[i] = min(countList[i], countList[i // 2] + 1)

print(countList[beforeOne])