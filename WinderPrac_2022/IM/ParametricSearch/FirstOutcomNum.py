# 가장 먼저 나오는 숫자
## 오름차순으로 정렬되어있는 n개의 숫자가 주어집니다
## 이후 m개의 질의가 주어지며 각 질의마다 하나의 숫자 x가 주어졌을 때, 주어진 x 중에서 최초로 등장하는 위치를 출력하는 프로그램을 작성해보세요.
### 테크닉 : 이진탐색

a,b = input().split()
numCount, cmdCount = int(a),int(b)

numS = list(map(int, input().split()))
cmdNum = list(map(int, input().split()))


for i in cmdNum:
    right = numCount - 1
    left = 0
    findWhere = numCount
    while left <= right:
        mid = (left+right) // 2
        if numS[mid] >= i:
            findWhere = min(findWhere,mid)
            right = mid - 1
        else:
            left = mid + 1
    if findWhere == numCount or numS[findWhere] != i:
        print(-1)
    else:
        print(findWhere + 1)