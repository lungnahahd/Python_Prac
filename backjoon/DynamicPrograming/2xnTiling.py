# 2xn 타일링
## 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법을 구하는 프로그램
### 입력 : 첫 줄에는 n이 입력
### 출력 : 첫 줄에는 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력

import sys
input = sys.stdin.readline

n = int(input()) # n을 입력 받는 부분
count = 1 # 결과를 count하는 부분으로 모두 1로 채우는 경우는 항상 존재하므로 1부터 시작

def CountCheck(num):
    check = 0
    if num < 2:
        return 0 
    elif num >= 2:
        check += num - 1
        for i in range(num-1):
            check += CountCheck(num -2 -i)
        return check

print((CountCheck(n) + 1) % 10007)