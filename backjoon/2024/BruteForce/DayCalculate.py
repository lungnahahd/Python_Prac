# 날짜 계산
## 이상한 나라의 이상한 달력 체계를 현실의 달력으로 변경하면 몇 년도인지 구하는 프로그램
### 입력 : E S M 즉 이상한 달력 체계가 한 줄에 입력
### 출력 : 현실의 달력으로 출력(가장 빠른 연도를 출력)

import sys
input = sys.stdin.readline

# e는 1부터 15, s는 1부터 28, m은 1부터 19 까지의 숫자
e,s,m = tuple(map(int,input().split()))

count = 0
resultNum = 0
while True:
    resultNum = count * 28 + s
    # 혹시나 나누었을 때, 0이 나와도 15나 19로 표기가 가능하므로 해당 부분도 고려해서 처리가 필요
    if resultNum  % 15 == e  or resultNum % 15 == e - 15:
        if resultNum % 19 == m or resultNum % 19 == m - 19:
            break
    count += 1
print(resultNum)