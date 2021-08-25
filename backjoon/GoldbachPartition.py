import math
import sys
input = sys.stdin.readline

caseNum = int(input()) # 케이스의 갯수를 받는 변수

# 소수를 판별하는 함수
def checkPrime(num):
    standard = int(math.sqrt(num))
    for i in range(2,standard + 1):
        if num % i == 0 or num == 1:
            return False
    return True

# 골드바흐 파티션 시작
result = [] # 각 케이스의 결과를 받을 리스트
for i in range(caseNum):
    getNum = int(input()) # 숫자를 하나씩 받기
    standard = int(getNum/2)
    count = 0 # 각 케이스의 결과를 카운트 시킬 변수
    for i in range(2, standard + 1):
        if checkPrime(i) and checkPrime(getNum - i):
            count += 1
    result.append(count)

for i in result:
    print(i)