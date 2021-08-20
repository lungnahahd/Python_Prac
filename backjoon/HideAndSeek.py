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

def FindMoveSize(num):
    global result
    global smallest
    count = 2
    for i in num:
        check = True
        while check:
            if i % smallest == 0:
                check = False
            else:
                while smallest % count != 0:
                    count += 1
                smallest = smallest / count
    return smallest

def FindSmall(list):
    small = 0 
    for i in list:
        if i < small or small == 0:
            small = i
        else:
            continue
    return small


distanceList = []

for i in range(playerNum):
    playerWhere = int(playerWhereList[i])
    if playerWhere > catcherWhere:
        distanceList.append(playerWhere - catcherWhere)
    else:
        distanceList.append(catcherWhere-playerWhere)
    smallest = FindSmall(distanceList)
print(FindMoveSize(distanceList))