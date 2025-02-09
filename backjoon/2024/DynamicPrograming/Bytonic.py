# 가장 긴 바이토닉 부분 수열
## 수열이 입력되었을 때, 가장 긴 바이토닉 부분 수열의 길이를 출력
### 입력 : 첫 줄의 수열의 길이와 두번 째 줄에 수열을 입력
### 출력 : 주어진 수열의 가장 긴 바이토닉 부분 수열의 길이를 출력

import sys
input = sys.stdin.readline

size = int(input())
list = input().split()
reverseList = list[:] # 파이썬 리스트를 똑같이 복사 -> 이렇게 안 하고 대입하면 주소가 복사!
reverseList.reverse() # 복사한 리스트를 순서 뒤집기

increase = [1 for i in range(size)] # 원래 순서대로 진행하는 카운트
reIncrease = [1 for i in range(size)] # 뒤로 진행하는 카운트

result = [0 for i in range(size)] # 결과를 담을 배열

# 앞에서 증가하는 것, 거꾸로 증가하는 것 카운트
for i in range(1,size):
    big = 0 # 각 경우에 가장 큰 카운트를 담을 변수
    reverseBig = 0 # 뒤집어서 각 경우 처리
    for j in range(i):
        if int(list[i]) > int(list[j]):
            if big < increase[j]:
                big = increase[j]
        if int(reverseList[i]) > int(reverseList[j]):
            if reverseBig < reIncrease[j]:
                reverseBig = reIncrease[j]
    increase[i] = big + 1
    reIncrease[i] = reverseBig + 1
reIncrease.reverse()

for i in range(size):
    result[i] = reIncrease[i] + increase[i] - 1

print(max(result))

