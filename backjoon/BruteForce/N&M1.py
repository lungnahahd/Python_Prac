# N과 M
## 자연수 N과 M이 주어진 경우, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 구하는 프로그램'
### 입력 : 자연수 N과 M이 입력
### 출력 : 수열을 출력

# N과 M은 8 이하인 자연수이므로, 반복문으로 시간 초과 없이 구현 가능

import sys
input = sys.stdin.readline

numLargest, numCount = tuple(map(int,input().split()))


countList = []
for i in range(numCount):
    countList.append(i+1)

numList = []
for i in range(numLargest):
    numList.append(i+1)


now = numCount - 1
while countList[0] <= numLargest:
    print(countList)
    if countList[now] == numLargest:
        countList[now] = countList[now-1] - 1





start = 0




while start != len(numLargest):


    print(start,end=' ')

    
    start += 1