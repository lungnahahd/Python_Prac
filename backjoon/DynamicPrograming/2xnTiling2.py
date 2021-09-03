# 2xn 타일링 2
## 이전의 타일링과 방법은 동일하고 타일은 1x2, 2x1, 2x2 존재
### 입력 : 첫 줄에 n이 입력
### 출력 : 2xn 직사각형을 채우고 가능한 방법의 수를 10,007로 나눈 나머지를 출력

import sys
input = sys.stdin.readline

n = int(input())

count = [0 for i in range(n + 1)]
count[1] = 1
count[2] = 3

for i in range(3,n+1):
    count[i] = count[i-2] * 2 + count[i-1]

print(count[n] % 10007)