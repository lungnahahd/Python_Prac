# 조합 0의 개수
## 조합 nCm의 끝자리 0의 갯수를 출력하는 프로그램
### 입력 : 첫 줄에 정수 n,m 2개 입력
### 출력 : 첫 줄에 nCm의 끝자리 0의 갯수를 출력 

import sys
input = sys.stdin.readline

N, M = input().split()
N = int(N)
M = int(M)

def Factorial(num):
    if num == 1 or 0:
        return 1
    else:
        return Factorial(num-1) * num

facN = Factorial(N)
facM = Factorial(M)
facNM = Factorial(N - M)

resultNum = int(facN / (facNM * facM)) # 조합을 구하는 수식
stringResult = list(map(int,str(resultNum)))
stringResult.reverse()
count = 0
check = True
for i in stringResult:
    if i == 0 and check:
        count += 1
    elif i != 0 and count != 0:
        check = False
print(count)