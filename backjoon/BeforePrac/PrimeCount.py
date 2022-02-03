# 소수 찾기
## 주어진 N개의 정수 중에서 소수가 몇 개인지 찾아서 갯수를 출력하는 프로그램
### 입력 : 첫 줄에는 몇개의 정수를 입력할지가 주어지고, 다음 줄 부터는 정수가 한 줄로 입력
### 출력 : 주어진 수 들 중에서 소수가 몇 개인지 갯수가 출력

import sys
input = sys.stdin.readline

numCount = int(input())
numCheck = input()

numCheckList = []
for i in range(numCount):
    numCheckList.append(int(numCheck.split()[i])) # 입력 받는 숫자들을 배열에 넣는 과정

result = []
for i in numCheckList:
    check = True
    pointNum = 2
    while pointNum <= i / 2 or i == 1:
        if i % pointNum == 0 or i == 1:
            check = False
            break
        else:
            pointNum += 1
    if check:
        result.append(i)

print(len(result))