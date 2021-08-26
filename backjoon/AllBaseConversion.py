# 진법 변환기
## 입력으로 주어진 특정 진법의 수를 내가 원하는 진법의 수로 변경
### 입력 : 첫 줄에 이전 진법 A와 변환할 진법 B가 공백을 구분으로 입력되고
###        둘째 줄에는 A진법으로 나타낼 숫자의 갯수가 입력되고 마지막 줄에는 변환 전 수가 입력
### 출력 : 입력으로 주어진 A 진법 수를 B 진법으로 변환

import sys
input = sys.stdin.readline

getFirst = input()
a,b = getFirst.split()
beforeMethod = int(a)
afterMethod = int(b)

caseCount = int(input())

getFinal = input().split()


cal = 1
result = 0
# 주어진 특정 진법의 수를 10진수로 변환하는 코드 부분
while getFinal:
    temp = getFinal.pop()
    result = result + int(temp) * cal
    cal = beforeMethod * cal

changeResult = []
while result != 0:
    changeResult.append(result % afterMethod)
    result = result // afterMethod
changeResult.reverse()

for i in changeResult:
    print(i, end=' ')