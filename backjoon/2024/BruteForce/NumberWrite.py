# 수 이어 쓰기1
## 1부터 N 까지의 수를 이어 작성해서 새로운 수를 얻을 때, 해당 수가 몇 자리인지 구하는 프로그램
### 입력 : 첫 줄에 N이 입력
### 출력 : 첫 줄에 자리수를 출력

import sys
input = sys.stdin.readline

num = int(input())
checkCount = 1
plus = 0
while True:
    temp = num - (10**checkCount)
    if temp <0:
        plus = checkCount
        break
    checkCount += 1

if plus == 1:
    print(num)
else:
    # 가장 먼저 해당 부분을 처리해주는 것
    result = 0
    temp = num - 10 ** (plus-1)
    result += (temp+1) * plus
    plus -= 1
    while plus != 0:
        # 그 이후 자리를 끝까지 계산해서 처리
        temp = 10**plus - 10**(plus-1)
        result += temp * plus
        plus -= 1

    print(result)