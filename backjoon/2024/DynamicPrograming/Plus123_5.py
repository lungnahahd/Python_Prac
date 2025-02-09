# 1,2,3 더하기 5
## 주어진 정수를 1,2,3 합으로 나타내는 방법의 수를 구하기
## 단, 같은 수를 두 번 이상 연속 사용해서는 안됨
### 입력 : 첫 줄에 테스트 개수가 입력되고, 그 이후에 차례로 구할 정수가 입력
### 출력 : 각 테스트 마다 결과를 한 줄에 출력

import sys
input = sys.stdin.readline

caseCount = int(input())
countList = [[0 for col in range(4)] for row in range(100001)]
countList[1][1] = 1
countList[2][2] = 1
countList[3][1] = 1
countList[3][2] = 1
countList[3][3] = 1

for i in range(4,100001):
    # 파이썬은 정수의 크기에 제한이 없음 
    # 만약 나누어 주는 경우라면, 한번에 나누어 주는 것이 아니라 중간 중간 나누어 주는 연산을 하는 것이 시간 초과 해결 가능
    countList[i][1] = (countList[i-1][3] + countList[i-1][2]) %1000000009
    countList[i][2] = (countList[i-2][1] + countList[i-2][3]) %1000000009
    countList[i][3] = (countList[i-3][1] + countList[i-3][2]) %1000000009

result = []
for i in range(caseCount):
    num = int(input())
    # 결과적으로 다시 한 번 나누어 주어야 원하는 값 도출 가능
    result.append((countList[num][1] + countList[num][2] + countList[num][3]) % 1000000009)

for i in result:
    print(i)