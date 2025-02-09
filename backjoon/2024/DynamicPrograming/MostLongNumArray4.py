# 가장 긴 증가하는 부분 수열 4
## 이전에는 길이만 출력했다면 이제는 가장 긴 수열도 출력
### 입력 : 첫 줄에 수열의 크기가 주어지고, 둘 째줄에 실제 수열이 입력
### 출력 : 첫 줄에 가장 긴 수열이 출력되고, 둘 째줄에 가장 긴 증가하는 부분 수열이 출력되는데, 수열이 여러가지이면 아무거나 출력

import sys
input = sys.stdin.readline
size = int(input())
numList = []
getList = input().split()
for i in getList:
    numList.append(int(i)) # 여기까지 모든 입력을 처리

cost = [1 for i in range(size)]
numResult = [[numList[i]] for i in range(size)] # 각 인덱스에 리스트 하나씩 추가
index = 0 # 최종적인 리스트를 출력하기 위해 위치값을 기록하는 변수
result = 1 # 크기 결과를 담을 변수 

# 하나씩 비교해 주면서 크기 뿐만 아니라, 배열도 출력하는 부분
for i in range(size):
    for j in range(i+1, size):
        if numList[i] < numList[j]:
            if cost[i] + 1 > cost[j]:
                cost[j] = cost[i] + 1
                numResult[j] = numResult[i][:] # 주의할 것이 이렇게 안하면 주소값도 같이 복사되어서 수정 시 해당하는 모든 리스트가 같이 수정됨
                numResult[j].append(numList[j])
        if result < cost[j]:
            result = cost[j]
            index = j

print(result) # 크기 출력
for i in numResult[index]: # 최종 리스트 출력
    print(i , end=' ')
