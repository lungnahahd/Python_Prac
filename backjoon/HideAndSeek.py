# 숨바꼭질 6
## N명과 숨바꼭질을 진행하는 과정에서 현재 S의 위치에서 최대 몇 칸씩 이동하면 다 잡을 수 있는지 알아보는 문제
### 입력 : 첫 줄에 N과 현재 나의 위치가 입력되고 두 번째 줄에는 N명 각각의 위치가 입력
### 출력 : 최대 몇 칸씩 이동할 때, 다 잡을 수 있는지의 값이 출력

import sys
input = sys.stdin.readline

a,b = input().split()
playerNum = int(a)
catcherWhere = int(b)
playerWhereList = input().split()

result = 0
smallest = 0

def gcd(a,b): # 최대 공약수 구하는 공식 -> 제발 암기하기 !!!!!!!!
    while b:
        mod = b
        b = a % b
        a = mod
    return a

distanceList = []

for i in range(playerNum):
    playerWhere = int(playerWhereList[i])
    if playerWhere > catcherWhere:
        distanceList.append(playerWhere - catcherWhere)
        if smallest < playerWhere - catcherWhere:
            smallest = playerWhere - catcherWhere
    else:
        distanceList.append(catcherWhere - playerWhere)
        if smallest < catcherWhere - playerWhere:
            smallest = catcherWhere - playerWhere
for i in distanceList:
    smallest = gcd(i,smallest)

print(int(smallest))