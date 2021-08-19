# 조합 0의 개수
## 조합 nCm의 끝자리 0의 갯수를 출력하는 프로그램
### 입력 : 첫 줄에 정수 n,m 2개 입력
### 출력 : 첫 줄에 nCm의 끝자리 0의 갯수를 출력 
#### 처음에는 팩토리얼로 처리를 진행했는데, 팩토리어을 이용하면 입력 수가 커졌을 때, 컴파일 에러 발생
#### 단순하게 0의 갯수만 구하면 되므로 그것만 구하도록 유도하기!
#### 조합 : (N!) / ((N-M)! * (M!))


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
# 분자, 분모를 구분해서 계산하지 말고, 먼저 2 따로 5 따로 각각 전체 계산 후, 결과 도출!
result = min(findTwo(N) - findTwo(N-M) -findTwo(M), findFive(N) - findFive(N-M) - findFive(M))
print(result)