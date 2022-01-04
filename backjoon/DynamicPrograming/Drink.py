# 포도주 시식
## 포도주 시식의 두가지 규칙
## 포도주 잔을 선택하면 그 잔에 포도주를 모두 마시고, 마신 후에 다시 원래 위치에 놓아야 함
## 연속으로 놓여 있는 3잔을 마실수는 없음
## 1부터 n 까지 포도주 잔이 있고, 각 포도주의 술 양이 주어졌을 때, 가장 많은 양의 포도주를 마실 수 있는 경우를 구하기
### 입력 : 첫 줄에 포도주 잔의 개수 n 이 주어지고 두 번째 줄부터 포도주 잔에 들어 있는 술의 양을 입력
### 출력 : 첫 줄에 최대로 마실 수 있는 포도주 양을 출력

import sys  

input = sys.stdin.readline
drinkNum = int(input())

drinkCost = [0 for i in range(drinkNum)]
drinkArr = [[0,0,0] for i in range(drinkNum)]
large = 0

# 포도주 술 양 받기
for i in range(drinkNum):
    get= int(input())
    drinkCost[i] = get
if drinkNum >= 3:
    drinkArr[0][0] = drinkCost[0]
    drinkArr[1][0] = drinkCost[1]
    drinkArr[1][1] = drinkCost[1] + drinkCost[0]
    drinkArr[2][0] = drinkCost[2] + drinkCost[0]
    drinkArr[2][1] = drinkCost[2] + drinkCost[1]
    drinkArr[2][2] = drinkArr[1][1]
    if drinkNum > 3:
        for i in range(3,drinkNum):
            drinkArr[i][0] = drinkArr[i-2][1] + drinkCost[i]
            drinkArr[i][1] = drinkArr[i-1][0] + drinkCost[i]
            drinkArr[i][2] = drinkArr[i-1][1]
else:
    if drinkNum == 1:
        drinkArr[0][0] = drinkCost[0]
    else:
        drinkArr[1][0] = drinkCost[0] + drinkCost[1]



resultDrink = print(max(drinkArr[drinkNum-1]))