# 가장 긴 증가하는 부분 수열
## 수열이 주어진 경우, 가장 긴 증가하는 부분 수열을 구하는 프로그램
### 입력 : 첫 줄에 수열의 크기가 주어지고, 둘째 줄에 수열이 입력
### 출력 : 첫 줄에 수열이 가장 긴 증가하는 부분 수열 길이 출력 

import sys
input = sys.stdin.readline

size = int(input()) # 수열의 크기
getList = input().split() # 수열을 입력
numList = []
for i in getList: # 그냥 split()만 해주면 문자열이 담긴 수열이 생기므로 이를 숫자로 변환하는 과정 필요 !! -> 이것을 안해서 오류 발생
    numList.append(int(i))

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


# 1 5 10 3 13 18 15 16 이 왜