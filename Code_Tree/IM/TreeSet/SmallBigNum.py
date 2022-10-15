# 작지만 큰 숫자
## n개의 숫자로 이루어진 수열이 하나 주어지고, 그 이후 m개의 질의가 주어집니다
##  각 질의마다 하나의 숫자가 주어진다 했을 때, 순서대로 수열 내에서 주어진 숫자보다 같거나 작은 숫자들 중 최댓값을 하나 골라 제거하는 것을 반복하는 프로그램을 작성해보세요
## 단, 같거나 작은 숫자가 없는 경우에는 제거하지 않고 넘어갑니다.

from sortedcontainers import SortedSet

s = SortedSet()      # treeset

numSize = list(map(int,input().split()))
numList = list(map(int,input().split()))
numSet = SortedSet(numList)

cmd = list(map(int,input().split()))

for i in cmd:
    if i in numSet:
        print(i)
        numSet.remove(i)
    else:
        idx = numSet.bisect_right(i) - 1
        if idx < 0:
            print(-1)
        else:
            print(numSet[idx])
            numSet.remove(numSet[idx])