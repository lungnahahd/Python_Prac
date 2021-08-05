# 후위 표기식으로 변환
## 식이 주어지면 이를 후위표기식으로 바꾸는 것
### 입력은 단순히 식 하나
#### 

import sys
from typing import Protocol
input = sys.stdin.readline

expression = input()
expression = list(expression)
expression = expression[:-1]
# 중위 표현식에서 우선순위를 나타내는 딕셔너리
priArray = {'(' : 0, ')' : -1, '*' : 1, '/' : 1, '+' : 2, '-' : 2}
# 결과를 담는 변수
result = ""
# 연산자를 임시적으로 담는 변수
tempSave = []
# 현재 진행 상황을 나타내는 변수
progress = 0

while progress < len(expression):
    if expression[progress].isupper():
        result += expression[progress]
    else:
        if expression[progress+1].isupper():
            if tempSave:
                if priArray[tempSave[-1]] >= priArray[expression[progress]]:
                    result += expression[progress + 1]
                    result += expression[progress]
                    progress += 1
                else:
                    result += expression[progress + 1]
                    result += tempSave.pop()
                    tempSave.append(expression[progress])
            else:
                tempSave.append(expression[progress])        
    progress += 1

if tempSave:
    while len(tempSave) != 0:
        result += tempSave.pop()

print(result)