# 돌의 소속
## 1부터 N까지 번호가 붙은 N개의 돌이 있습니다. 각 돌은 그룹 1, 2, 3 중 하나에 무조건 속합니다.
## 각 돌이 어떤 그룹에 속하는지 주어졌을 때, Q개의 돌 번호 범위마다 각 그룹의 돌이 몇개씩 있는지 구하는 프로그램을 작성해보세요.

onePrefix = [0]
twoPrefix = [0]
ThreePrefix = [0]

stoneSize, rangeSize = input().split()
stoneSize = int(stoneSize)
rangeSize = int(rangeSize)

for i in range(1,stoneSize+1):
    num = int(input())
    if num == 1:
        onePrefix.append(onePrefix[i-1] + 1)
        twoPrefix.append(twoPrefix[i-1])
        ThreePrefix.append(ThreePrefix[i-1])
    elif num == 2:
        twoPrefix.append(twoPrefix[i-1] + 1)
        onePrefix.append(onePrefix[i-1])
        ThreePrefix.append(ThreePrefix[i-1])
    else:
        ThreePrefix.append(ThreePrefix[i-1] + 1)
        onePrefix.append(onePrefix[i-1])
        twoPrefix.append(twoPrefix[i-1])

for i in range(rangeSize):
    getRange = list(map(int, input().split()))
    print(onePrefix[getRange[1]] - onePrefix[getRange[0] - 1],end=' ')
    print(twoPrefix[getRange[1]] - twoPrefix[getRange[0] - 1],end=' ')
    print(ThreePrefix[getRange[1]] - ThreePrefix[getRange[0] - 1])