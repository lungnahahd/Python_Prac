import sys
input = sys.stdin.readline

num = int(input())

def Factorial(num):
    if num == 1:
        return num
    else:
        return Factorial(num - 1) * num

if num == 0:
    print(1)
elif num == 1:
    print(0)
else:
    resultFac = Factorial(num)
    stringResult = list(map(int,str(resultFac))) # 정수를 리스트로 형변환하는 과정
    countResult = 0
    for i in stringResult:
        if i == 0:
            countResult += 1
    print(countResult)