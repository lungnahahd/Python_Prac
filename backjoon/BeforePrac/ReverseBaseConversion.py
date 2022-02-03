# 역진법 변환
## B진법 수 N이 주어지면 이를 10진수로 변환
## 10진법을 넘어가는 진법의 10 이상 숫자는 알파벳 대문자로 대체
### 입력 : 첫 줄에 N이 주어지고, B진법이 입력
### 출력 : 입력된 N을 10진수로 변환한 결과를 출력

import sys
input = sys.stdin.readline

getString = input()
a, b = getString.split()

BeforeNum = list(a) # 변환하기 전 숫자
changeMethod = int(b) # 진법

result = 0
cal = 1
while BeforeNum:
    temp = BeforeNum.pop()
    check = ord(temp)
    if check < 65:
        result += (check-48) * cal
        cal = cal * changeMethod
    else:
        result += (check - 55) * cal
        cal = cal * changeMethod

print(result)