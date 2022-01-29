# 타일 채우기
## 3XN 크기의 벽을 2X1, 1X2 크기의 타일로 채우는 경우의 수 구하기
### 입력 : 첫 줄에 N 입력
### 출력 : 경우의 수를 출력

import sys
input = sys.stdin.readline

size = int(input())

if size % 2 != 0:
    print(0)
elif size == 2:
    print(3)
else:
    result = 0
    result += (3 ** (size / 2))
    result += (3**((size/2) - 1)) * 2
    print(int(result))