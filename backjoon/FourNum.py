# 네 수 프로그램
## 네 자연수 a,b,c,d가 주어지고, a와 b를 붙인 수와 c와 d를 이어 붙인 수의 합을 구하는 프로그램
### 입력 : 네 자연수 입력
### 출력 : a와 b를 이어붙인 수와 c와 d를 이어붙인 수의 합을 출력

import sys
input = sys.stdin.readline

A,B,C,D = input().split()
sumFront = str(A) + str(B)
sumBack = str(C) + str(D)
result = int(sumFront) + int(sumBack)
print(result)