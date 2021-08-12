# 소수 구하기
## M 이상, N 이하의 소수를 모두 출력하는 프로그램
### 입력 : 첫 줄에 M과 N 즉, 범위를 나타내는 두 수를 입력 -> 단 해당 범위 내에는 소수가 하나 이상 존재
### 출력 : 한 줄에 하나씩 전체 소수를 출력
#### 에라토스의 체 알고리즘을 활용해서 문제 해결 가능

import sys
import math

input = sys.stdin.readline


min, max = input().split()
min = int(min)
max = int(max)

checkBool = [True for i in range(max+1)]
checkBool[0] = False
checkBool[1] = False
# 소수 여부를 판단하는 함수
def FindPrime(num):
    check = 2
    result = True
    while check <= num / 2:
        if num % check == 0:
            result = False
            break
        else:
            check += 1
    return result


result = []
# 제곱근으로 처리해서 시간 줄이기!!!! 중요
for i in range(2, int(math.sqrt(max))+1):
    if checkBool[i]:
        resultCheck = FindPrime(i)
        if resultCheck:
            count = 2
            while i * count <= max:
                checkBool[i * count] = False
                count += 1

for i in range(2,max+1):
    if checkBool[i] and i >= min:
        print(i)