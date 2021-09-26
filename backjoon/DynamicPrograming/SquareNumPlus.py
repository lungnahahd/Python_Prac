# 제곱수의 합
## 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타 낼 수 있을때, 해당 제곱수 항의 최소 갯수를 구하는 프로그램
### 입력 : 자연수 N이 입력
### 출력 : N을 나타내는 제곱수 항의 최소 개수를 출력

import math
import sys
input = sys.stdin.readline

num = int(input())

result = [i for i in range(num+1)]
for i in range(1,num+1):
    for j in range(1,i):
        if j*j > i:
            break
        else:
            if result[i] > result[i - j*j] + 1: # DP를 활용해서 작은 수부터 처리해서 점점 큰 수로 나아가는 것
                result[i] = result[i - j*j] + 1
print(result[num])