# 문자열 분석
## 문자열 N개가 주어질 때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 갯수를 구하는 프로그램
## 각 문자열은 소문자, 대문자, 숫자, 공백으로 구성
### 입력 : 첫째 줄부터 N번쨰 줄까지 입력이 주어짐
### 출력은 소문자, 대문자, 숫자, 공백 순으로 제시


import sys
input = sys.stdin.readline
# 결과를 입력 받는 배열
result = [0 for i in range(4)]
resultString = []
count = 0

while True:
    getString = input()
    # 오른쪽에 엔터 입력을 지워주고 문자열에 담기
    getString = getString.rstrip('\n')
    # 엔터 입력만, 즉 더 이상 입력을 안 주었을 경우 실행
    if not getString:
        # 배열을 문자열로 하는 부분
        # 엔터랑 공백은 문자열에 들어가지 않으므로 str로 문자열로 받아들일 수 있도록 처리하는 과정이 필요
        print("".join(map(str,resultString)))
        break
    while count != len(getString):
        # 아스키코드를 활용해서 구분하는 부분 -> 이 외에도 .isUpper 등으로 처리할 수 있는 것도 고려하기
        if ord(getString[count]) >= 65 and ord(getString[count]) <= 90:
            result[1] += 1
        elif ord(getString[count])>= 97 and ord(getString[count]) <= 122:
            result[0] += 1
        elif ord(getString[count])>= 48 and ord(getString[count]) <= 57:
            result[2] += 1
        else : 
            result[3] += 1
        count += 1
    # 소문자, 대문자, 숫자, 공백을 순서대로 배열에 담는 부분
    for i in result:
        resultString.append(i)
        resultString.append(' ')
    # 공백을 기준으로 문자열 결과를 나누어서 담기
    resultString.append('\n')
    # 다시 문자열을 시작하므로 count랑 문자열 count 배열을 초기화 하는 부분
    count = 0
    result = [0 for i in range(4)]