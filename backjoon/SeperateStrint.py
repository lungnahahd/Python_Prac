# 문자열 분석
## 문자열 N개가 주어질 때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 갯수를 구하는 프로그램
## 각 문자열은 소문자, 대문자, 숫자, 공백으로 구성
### 입력 : 첫째 줄부터 N번쨰 줄까지 입력이 주어짐
### 출력은 소문자, 대문자, 숫자, 공백 순으로 제시


import sys
input = sys.stdin.readline

# while True:
#     getString = input()
#     getString = getString.rstrip('\n')
#     print(getString[1])

result = [0 for i in range(4)]
resultString = []
count = 0
while True:
    getString = input()
    getString = getString.rstrip('\n')
    if not getString:
        print("".join(map(str,resultString)))
        break
    while count != len(getString):
        if ord(getString[count]) >= 65 and ord(getString[count]) <= 90:
            result[1] += 1
        elif ord(getString[count]) and ord(getString[count]) <= 122:
            result[0] += 1
        elif ord(getString[count]) and ord(getString[count]) <= 57:
            result[2] += 1
        else : 
            result[3] += 1
        count += 1
    for i in result:
        resultString.append(i)
        resultString.append(' ')
    resultString.append('\n')
    count = 0
    result = [0 for i in range(4)]