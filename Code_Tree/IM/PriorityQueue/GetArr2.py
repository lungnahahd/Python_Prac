# 배열 추출 2
## 우선순위 큐 사용 이유 : 절대값이 가장 작은 것을 단순하게 뽑으면 되므로 적은 시간 복잡도를 위해 사용

import heapq

numHeap = []
size = int(input())

for i in range(size):
    num = int(input())
    if num == 0:
        if numHeap:
            _,smallNum = heapq.heappop(numHeap)
            print(smallNum)
        else:
            print(0)
    else:
        absNum = abs(num)
        heapq.heappush(numHeap,(absNum,num))