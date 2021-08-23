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
            chageResult(0)
            chageResult(0)
            chageResult(0)

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