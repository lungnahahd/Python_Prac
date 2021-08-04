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

tempSave = [] # 임시적으로 연산자를 저장하는 배열 
priSave = []  # 괄호 나왔을 때, 저장하는 우선순위 높은 배열

priResult = ""

priCount = 0  # 괄호의 열고 닫음을 나타내주는 변수
progress = 0  # 현재 진행상황을 알려주는 변수
result = ""   # 결과를 담는 변수
count = 0

while progress < len(expression):
    if expression[progress] == "(":
        while expression[progress + count] != ")":
            priResult


    elif expression[progress] == "*" or expression[progress] == "/":
        if expression[progress+1] == "(":
            priSave.append(expression[progress])
        else:
            result += expression[progress+1]
            result += expression[progress]
            progress += 2
    elif expression[progress] == "+" or expression[progress] == "-":
        