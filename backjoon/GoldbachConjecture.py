# 골드바흐의 추측
## 추측 : 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있음
## 위의 추측을 검증하는 프로그램
### 입력 : 6 이상의 짝수를 한 줄씩 작성하고 마지막 줄에는 0으로 끝내기
### 출력 : 각 테스트 케이스에 대해서 n = a + b 형태로 출력
### 출력 : 경우가 여러 가지이면 b - a 가 가장 큰 것을 출력하며 나타낼 수 없는 경우는 "Goldbach's conjecture is wrong."

import sys
import math
from collections import deque


input = sys.stdin.readline
# 소수 판별 함수
def CheckPrime(checkNum):
    count = 2
    result = True
    num = int(math.sqrt(checkNum)) + 1
    list = [True for i in range(num)]
    while count < num :
        if list[count]:
            if checkNum % count == 0:
                result = False
                break
        point = count
        multi = 1
        while point < num :
            list[point] = False
            multi += 1
            point = point * multi
        count += 1
    return result
# 판별할 숫자를 처음 받는 부분
num = int(input())

goldbach = deque()

# 예제를 반복하는 부분
while num != 0:
    conjectureFalse = True
    goldbach.append(num)
    point = num - 2
    while point > num/2:
        if CheckPrime(point) and CheckPrime(num - point):
            goldbach.append(num-point)
            goldbach.append(point)
            conjectureFalse = False
            break
        else:
            point -= 1
    if conjectureFalse:
        goldbach.append("No")
    num = int(input())
# 결과를 출력하는 부분
while goldbach:
    if goldbach[0] == "No":
        goldbach.popleft()
        print("Goldbach's conjecture is wrong.")
    else:
        print(str(goldbach.popleft()) + " = " + str(goldbach.popleft())+ " + " + str(goldbach.popleft()))