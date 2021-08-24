# -2진수
## 부호가 없는 2진수로 표현
### 입력 : 10진법으로 표현된 수가 입력 
### 출력 : 입력된 수를 -2진법 수로 변환한 결과를 출력

import sys
input = sys.stdin.readline

decimalNum = int(input()) # 10진수를 받는 부분

############# 진수를 계산할 때, 우리가 아는 진수 계산법을 활용하면 보다 쉽게 구할 수 있음을 명심!!!!!!!!!!!!!!!!!!!!!!!!!!

if decimalNum == 0:
    print(0)
else:
    result = []
    while decimalNum != 0:
        if decimalNum % (-2) == 0:
            decimalNum = int(decimalNum // (-2))
            result.append(0)
        else:
            decimalNum = int(decimalNum // (-2)) + 1
            result.append(1)
    result.reverse()
    for i in result:
        print(i, end='')