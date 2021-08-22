# 2진수 8진수
## 2진수가 주어졌을 경우 8진수로 변환하는 프로그램
### 입력 : 첫 줄에 2진수
### 출력 : 첫 줄에 8진수 변환

import sys
input = sys.stdin.readline

binary = list(input())
binary = binary[:-1]
numSize = len(binary)
binary.reverse()

count = 0 # 3개씩 인덱스를 묶는 경우 이를 확인해주는 체크 변수
middleResult = 0
result = []
for i in binary:
    i = int(i)
    if count == 0:
        if i == 0:
            count += 1
        else:
            middleResult = 1
            count += 1
    elif count == 1:
        if i == 0:
            count += 1
        else:
            middleResult += 2
            count += 1
    elif count == 2:
        if i == 0:
            count = 0
            result.append(middleResult)
            middleResult = 0
        else:
            middleResult += 4
            result.append(middleResult)
            middleResult = 0
            count = 0

if middleResult != 0 or count != 0:
    result.append(middleResult)

result.reverse()
for i in result:
    print(i, end='')