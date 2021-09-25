# 제곱수의 합
## 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타 낼 수 있을때, 해당 제곱수 항의 최소 갯수를 구하는 프로그램
### 입력 : 자연수 N이 입력
### 출력 : N을 나타내는 제곱수 항의 최소 개수를 출력

import math
import sys
input = sys.stdin.readline

num = int(input())

count = 1

def checkSqure(N):
    global count
    if int(math.sqrt(N)) == math.sqrt(N):
        #count += 1
        return count
    else:
        count += 1
        temp = N - int(math.sqrt(N)) * int(math.sqrt(N))
        return checkSqure(temp)

print(checkSqure(num))