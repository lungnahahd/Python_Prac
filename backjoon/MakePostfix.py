 #후위 표기식으로 변환
## 식이 주어지면 이를 후위표기식으로 바꾸는 것
### 입력은 단순히 식 하나
#### 


import sys
input = sys.stdin.readline

expression = input()
expression = list(expression)
expression = expression[:-1]

tempSave = []
priSave = []
next = False
result = ""
priCount = 0
for i in range(len(expression)):
    if expression[i].isupper():
        result += expression[i]
        if next:
            result += tempSave.pop()
            next = False
    elif expression[i] == "+" or expression[i] == "-" or expression[i] == "*" or expression[i] == "/":
        if priCount != 0:
            priSave.append(expression[i])
        else:
            if expression[i] == "*" or expression[i] == "/":
                next = True
            tempSave.append(expression[i])
    elif expression[i] == "(":
        priCount += 1
    else:
        if len(priSave) != 0:
            result += priSave.pop()
        priCount-=1
while tempSave:
    result += tempSave.pop()

print(result)