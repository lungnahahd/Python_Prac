# 진법 변환
## 10진법 수 N이 제공될 때, 이를 B진법을 바꾸어주는 프로그램
## 10진법을 넘어가는 진법의 수는 알파벳 대문자를 이용해서 표현
### 입력 : N과 B가 입력
### 출력 : 10진법 수 N을 B진법으로 변환해서 출력

import sys
input = sys.stdin.readline
getString = input()
a,b = getString.split()
beforeNum = int(a)
changeMethod = int(b)


result = []
while beforeNum != 0:
    temp = beforeNum % changeMethod # 나누는 것으로 간단하게 진법 계산 가능
    if temp < 10:
        result.append(temp)
    else:
        temp += 55 # 아스키 코드로 변환하기 위해서 더해주고 밑에서 바로 변환
        result.append(chr(temp))
    beforeNum = beforeNum // changeMethod # 진법 계산

result.reverse() # 역으로 저장되므로 배열을 reverse 해주기
for i in result:
    print(i, end='')