# 최솟값 3개
## n개의 숫자가 순서대로 하나씩 주어졌을 때, 숫자가 하나씩 주어질 때마다 지금까지 주어진 숫자들 중 가장 작은 숫자 3개의 곱을 출력하는 프로그램을 작성해보세요.
### 우선순위 큐 사용 이유 : 최소값을 빠르게 찾아야 하므로 사용

import heapq

size = int(input())
numList = list(map(int, input().split()))

numHeap = []

for i in numList:
    heapq.heappush(numHeap,i)
    if len(numHeap) < 3:
        print(-1)
    else:
        numA = heapq.heappop(numHeap)
        numB = heapq.heappop(numHeap)
        numC = heapq.heappop(numHeap)
        result = numA * numB * numC
        heapq.heappush(numHeap,numA)
        heapq.heappush(numHeap,numB)
        heapq.heappush(numHeap,numC)
        print(result)