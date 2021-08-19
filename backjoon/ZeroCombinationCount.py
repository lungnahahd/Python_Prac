# 조합 0의 개수
## 조합 nCm의 끝자리 0의 갯수를 출력하는 프로그램
### 입력 : 첫 줄에 정수 n,m 2개 입력
### 출력 : 첫 줄에 nCm의 끝자리 0의 갯수를 출력 

import sys
input = sys.stdin.readline

N, M = input().split()
N = int(N)
M = int(M)

# 2로 몇 번 나눌 수 있는가?
def findTwo(num):
    count = 0
    while num != 0:
        num = num // 2
        count += num
    return count

# 5로 몇 번 나눌 수 있는가?
def findFive(num):
    count = 0
    while num != 0:
        num = num // 5
        count += num
    return count

# 조합의 0을 계산하는 부분
result = min(findFive(N),findTwo(N)) - min(findTwo(M)+findTwo(N-M),findFive(M)+findFive(N-M))
print(result)