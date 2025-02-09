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
drinkArr = [[0,0,0] for i in range(drinkNum)] # 각 단계만다 카운트 할 배열
drinkCheck = [[False,False,False] for i in range(drinkNum)] # 이전까지 포도주를 어떻게 마셨는지를 체크할 배열

# 포도주 술 양 받기
for i in range(drinkNum):
    get= int(input())
    drinkCost[i] = get

drinkArr[0][1] = drinkCost[0]
drinkCheck[0][0] = True # 첫 잔을 마시지 않고 넘기기
drinkCheck[0][1] = True # 첫 잔을 마시고 넘기기
# 두 잔을 마시는 경우는 처음 경우에는 존재하지 않으므로 넘기기

# 경우를 나누어서 배열을 계산해주기!
for i in range(1, drinkNum):
    if drinkCheck[i-1][0]:
        drinkCheck[i][0] = True
        drinkArr[i][0] = max(drinkArr[i][0], drinkArr[i-1][0])
        drinkCheck[i][1] = True
        drinkArr[i][1] = max(drinkArr[i][1],drinkArr[i-1][0] + drinkCost[i])
    if drinkCheck[i-1][1]:
        drinkCheck[i][0] = True
        drinkArr[i][0] = max(drinkArr[i][0],drinkArr[i-1][1])
        drinkCheck[i][2] = True
        drinkArr[i][2] = max(drinkArr[i][2],drinkArr[i-1][1] + drinkCost[i])
    if drinkCheck[i-1][2]:
        drinkCheck[i][0] = True
        drinkArr[i][0] = max(drinkArr[i][0], drinkArr[i-1][2])

# 최종 생성 배열에서 최대 값만 출력하도록 하기!
print(max(drinkArr[drinkNum-1]))