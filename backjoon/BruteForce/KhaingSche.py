# 카잉 달력
## 카잉 제국만의 달력을 표시할 필요가 있음
### 입력 : 첫 줄에 입력 데이터 수가 주어지고, 각 테스트 데이터는 한 줄로 구성되며, 각 줄에는 4개의 정수가 입력
### 출력 : 유효하지 않으면 -1, 바꿀 수 있다면 현재로 몇년인지를 출력

import sys
input = sys.stdin.readline

caseSize = int(input()) # 전체 경우의 수를 받기

result = []
for _ in range(caseSize):
    m,n,x,y = tuple(map(int, input().split())) # 각 케이스 별로 달력 입력 받기
    # 달력상 기준과 동일한 값이 나왔다면 나머지 처리를 위해 변경해주기
    if m == x:
        x = 0
    if n == y:
        y = 0
    # 큰 숫자를 기준으로 처리해야 깔끔하게 처리가 되므로 큰 숫자에 따라 경우 나누기
    if m >= n:
        count = 0
        while True:
            temp = count * m + x
            if temp > m*n: # 두 수를 곱한 경우가 최대이므로, 해당 숫자를 초과하면 표현 불가 상태로 처리
                result.append(-1)
                break
            if temp % n ==  y:
                result.append(temp)
                break
            else:
                count += 1
    else:
        count = 0
        while True:
            temp = count * n + y
            if temp > m*n:
                result.append(-1)
                #print(-1)
                break
            if temp % m ==  x:
                result.append(temp)
                #print(temp)
                break
            else:
                count += 1

for i in result:
    print(i)