import sys

input = sys.stdin.readline
# 모든 입력을 받는 부분
numSize = int(input())
realNum = [0 for i in range(numSize)]
expression = input()
expression = list(expression)

for i in range(numSize):
    realNum[i] = int(input())


# 수식을 알파벳에서 실질적인 수로 변화시키기
# 문자열을 입력 받은걸 그대로 리스트로 변환해서 사용하려는 경우, 마지막에 공백(엔터)이 들어가므로 범위 -1 해주기
for i in range(len(expression) - 1):
    if expression[i] == "+" or expression[i] == "-" or expression[i] == "*" or expression[i] == "/":
        continue
    else:
        expression[i] = realNum[ord(expression[i])-65]

# 피연산자를 잠시 저장할 스택
tempNum = [] 
tempNum.append(expression[0])

# 후위표기식 계산
#result = 0
# 문자열을 입력 받은걸 그대로 리스트로 변환해서 사용하려는 경우, 마지막에 공백(엔터)이 들어가므로 범위 -1 해주기
for i in range(1,len(expression) -1 ):
    if expression[i] == "+" or expression[i] == "-" or expression[i] == "*" or expression[i] == "/":
        b = tempNum.pop()
        a = tempNum.pop()
        if expression[i] == "+":
            c = a + b
        elif expression[i] == "-":
            c = a - b
        elif expression[i] == "*":
            c = a * b
        elif expression[i] == "/":
            c = a/b
    else:
        c = expression[i]
    if i < len(expression) - 2:
        tempNum.append(c)
    else:
        result = c

print("%.2f"%result)