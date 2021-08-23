# 8진수 2진수
## 8진수가 주어졌을 경우, 이를 2진수로 변환하는 프로그램
### 출력 : 첫 줄에 8진수가 입력
### 입력 : 첫 줄에 입력된 8진수를 2진수로 변환한 결과를 출력(입력이 0인 경우를 제외하고는 반드시 1로 시작)

import sys
input = sys.stdin.readline

#입력을 받고 이를 변환하기 쉽게 변형하는 부분
octalNumString =  input()
if int(octalNumString) == 0:
    print(0)
else:
    octalNumString = list(octalNumString)
    octalNumString = octalNumString[:-1]
    octalNumString.reverse()

    chageResult = [] # 결과를 받을 리스트
    for i in octalNumString:
        num = int(i)
        if num == 7:
            chageResult.append(1)
            chageResult.append(1)
            chageResult.append(1)
        elif num == 6:
            chageResult.append(0)
            chageResult.append(1)
            chageResult.append(1)
        elif num == 5 :
            chageResult.append(1)
            chageResult.append(0)
            chageResult.append(1)
        elif num == 4:
            chageResult.append(0)
            chageResult.append(0)
            chageResult.append(1)
        elif num == 3:
            chageResult.append(1)
            chageResult.append(1)
            chageResult.append(0)
        elif num == 2:
            chageResult.append(0)
            chageResult.append(1)
            chageResult.append(0)
        elif num == 1:
            chageResult.append(1)
            chageResult.append(0)
            chageResult.append(0)
        else:
            chageResult.append(0)
            chageResult.append(0)
            chageResult.append(0)

    chageResult.reverse()
    front = True
    for i in chageResult:
        if front and i == 0:
            continue
        elif front and i != 0:
            front = False
            print(i, end='')
        else:
            print(i, end='')