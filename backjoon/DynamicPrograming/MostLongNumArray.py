# 가장 긴 증가하는 부분 수열
## 수열이 주어진 경우, 가장 긴 증가하는 부분 수열을 구하는 프로그램
### 입력 : 첫 줄에 수열의 크기가 주어지고, 둘째 줄에 수열이 입력
### 출력 : 첫 줄에 수열이 가장 긴 증가하는 부분 수열 길이 출력 

import sys
input = sys.stdin.readline

size = int(input()) # 수열의 크기
numList = input().split() # 수열을 입력
count = [1 for i in range(size)] # 각 수열의 크기를 카운트 해줄 리스트

result = 1 # 최종 크기를 나타낼 변수
for i in range(1,size):
    nowWhere = size - i
    move = nowWhere
    while move != 0:
        if numList[nowWhere] > numList[move-1]:
            if count[nowWhere] < count[move-1]:
                move -= 1
                continue
            count[move-1] = count[nowWhere] + 1
            if count[move-1] > result:
                result = count[move-1]
            move -= 1
        else:
            move -= 1
print(result)
print(count)


# 1 5 10 3 13 18 15 16 이 왜 6이 안되는가?