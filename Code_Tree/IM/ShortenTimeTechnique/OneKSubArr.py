# 1이 k개 이상 존재하는 부분 수열
## 1과 2로 이루어진 크기가 n인 수열에서, 1이 k개 이상 존재하는 가장 짧은 연속된 부분 수열의 길이를 구하는 프로그램을 작성해보세요.
### 테크닉 : Two Pointer 테크닉

import sys
INT_MAX = sys.maxsize

numSize, subSize = input().split()
numSize, subSize = int(numSize), int(subSize)

subNums = list(map(int,input().split()))
whereOne = []

# 1인 위치만 뽑아서 배열에 담기
for i in range(numSize):
    if subNums[i] == 1:
        whereOne.append(i)


distance = INT_MAX
point = 0

for i in range(len(whereOne)):
    point = i + subSize - 1 # 해당 i 위치에서 가장 짧게 떨어진 위치를 지정
    if point < len(whereOne):
        distance = min(distance,whereOne[point] - whereOne[i] + 1) # 가장 짧은 길이를 갱신

if distance == INT_MAX:
    print(-1)
else:
    print(distance)