# -2진수
## 부호가 없는 2진수로 표현
### 입력 : 10진법으로 표현된 수가 입력 
### 출력 : 입력된 수를 -2진법 수로 변환한 결과를 출력

import sys
input = sys.stdin.readline

decimalNum = int(input()) # 10진수를 받는 부분

getBinaryNum = [] 
count = 1 # 횟수를 나타내는 변수
binary = 1 # 각 이진수 값을 나타내는 변수

# -2진수 해결을 위한 배열을 생성하는 과정
while True:
    if decimalNum > 0:
        if count % 2 != 0:
            if binary >= decimalNum:
                getBinaryNum.append(binary)
                break
        getBinaryNum.append(binary)
        binary = binary * -2
    elif decimalNum < 0:
        if count % 2 == 0:
            if binary <= decimalNum:
                getBinaryNum.append(binary)
                break
        getBinaryNum.append(binary)
        binary = binary * -2
    else:
        getBinaryNum.append(0)
        break
    count += 1

listSize = len(getBinaryNum) - 1
result = getBinaryNum[listSize]
binaryResult = []
binaryResult.append(1)


if result > 0:
    minus = False
else:
    minus = True
check = abs(decimalNum - result)

for i in range(1,len(getBinaryNum)):
    if result > decimalNum:
        if getBinaryNum[listSize - i] < 0:
            result += getBinaryNum[listSize - i]
            binaryResult.append(1)
        else:
            binaryResult.append(0)
    elif result < decimalNum:
        if getBinaryNum[listSize - i] > 0:
            result += getBinaryNum[listSize -i]
            binaryResult.append(1)
        else:
            binaryResult.append(0)
    else:
        binaryResult.append(0)
for i in binaryResult:
    print(i, end='')