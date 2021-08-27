# 골드바흐 파티션
## 골드바흐의 추측 : 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있음
## 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션
## 짝수 N이 주어졌을 경우 골드바흐 파티션의 개수 구하기
### 입력 : 첫 줄에 케이스의 갯수가 입력되며 그 다음 한 줄씩 짝수 입력
### 출력 : 각 케이스마다의 파티션의 수를 출력

import math
import sys
input = sys.stdin.readlinea

caseNum = int(input()) # 케이스의 갯수를 받는 변수
bigNum = 1000000 # 문제에서 주어진 최대 범위

# 에라토스의 체를 활용하는 함수 -> 에라토스의 체를 사용하는 경우는 소수 판별 함수 필요 X
def Eratos(num):
    checkList = [True for i in range(num+1)]
    checkList[0] = False
    checkList[1] = False
    standard = int(math.sqrt(num))
    for i in range(2,standard + 1):
        if checkList[i]:
            count = 2
            check = i
            while check * count <= num:
                checkList[check * count] = False
                count += 1
    return checkList

result = [] # 각 케이스의 결과를 받을 리스트
checkList = Eratos(bigNum) # 시간 초과를 막기 위해 미리 소수 리스트를 구해놓기

# 골드바흐 파티션 시작
for i in range(caseNum):
    getNum = int(input()) # 숫자를 하나씩 받기
    count = 0 # 소수 쌍을 카운트하는 변수
    for j in range(2, int(getNum/2) + 1):
        if checkList[j] and checkList[getNum - j]: # 소수 쌍을 확인
            count += 1
    result.append(count)

# 출력하는 부분
for i in result:
    print(i)