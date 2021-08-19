# 팩토리얼 0의 갯수
## N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지의 0의 갯수를 구하는 프로그램
### 입력 : 첫 줄에 정수 N이 입력
### 출력 : 첫 줄에 구한 0의 갯수를 출력

import sys
input = sys.stdin.readline

num = int(input())

def Factorial(num):
    if num == 1:
        return num
    else:
        return Factorial(num - 1) * num

if num == 0 or num == 1:
    print(0)
else:
    resultFac = Factorial(num)
    stringResult = list(map(int,str(resultFac))) # 정수를 리스트로 형변환하는 과정
    stringResult.reverse()
    countResult = 0
    countCheck = True
    for i in stringResult:
        if i == 0 and countCheck:
            countResult += 1
        elif i != 0 and countCheck:
            if countResult != 0:
                countCheck = False
            continue
        elif i != 0:
            break
    print(countResult)