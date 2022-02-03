# 후위 표기식으로 변환
## 식이 주어지면 이를 후위표기식으로 바꾸는 것
### 입력은 단순히 식 하나
#### 

import sys
input = sys.stdin.readline

expression = input()
expression = list(expression)
expression = expression[:-1]
stack = []
result = ""

for x in expression:
    if x.isalpha():
        result += x
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                result += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != '(' :
                result += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()
print(result)