# 최소공배수
## 두 자연수 A와 B가 주어지고, 그 두 자연수의 최소공배수를 구하는 프로그램
### 입력 : 첫째 줄에는 몇 번 실행할 것인지가 주어지고, 그 다음 줄부터는 각각 2개씩 자연수가 입력
### 출력 : 입력으로 주어진 두 자연수 쌍의 최소공배수를 # 최소공배수
## 두 자연수 A와 B가 주어지고, 그 두 자연수의 최소공배수를 구하는 프로그램
### 입력 : 첫째 줄에는 몇 번 실행할 것인지가 주어지고, 그 다음 줄부터는 각각 2개씩 자연수가 입력
### 출력 : 입력으로 주어진 두 자연수 쌍의 최소공배수를 구해서 출력

#### 최소공배수는 두 정수 간 곱에서 최대공약수를 나누는 과정으로 구할 수 있음

import sys
input = sys.stdin.readline

caseNum = int(input())
result = []
# 최대공약수를 빠르게 구하는 과정 -> 해당 과정은 반드시 암기해서 풀기

def GD(a,b):
    while b:
        a, b = b, a % b
    return a


# 최소공배수를 구하는 부분 -> 두 정수간 곱에서 최대공약수 나누기
for i in range(caseNum):
    smallNum, bigNum = map(int,input().split())
    gd = GD(smallNum, bigNum)
    result.append(bigNum * smallNum // gd)

for i in result:
    print(i)