# 팩토리얼
## 0보다 크거나 같은 정수 N이 주어질 때, N!을 출력하는 프로그램
### 입력 : 첫 줄에는 정수 N이 입력
### 출력 : N!을 출력

import sys
input = sys.stdin.readline

num = int(input())

def Factorial(num):
    if num == 1:
        return 1
    else :
        return Factorial(num - 1 ) * num

if num == 1 or num == 0:
    print(1)
else:
    print(Factorial(num))