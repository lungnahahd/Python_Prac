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
nowDrink = [[] for i in range(drinkNum)]

large = 0
# 포도주 술 양 받기
for i in range(drinkNum):
    get= int(input())
    drinkCost[i] = get
    nowDrink[i].append([drinkCost[i],1])
    

# print(nowDrink[0][0][0]) # 포도주 자체의 양을 카운트
# print(nowDrink[0][0][1]) # 포도주 연속 마신 것 카운트 


# 포도주 마시는 것 카운트
for i in range(1,drinkNum):
    for a in range(len(nowDrink[i-1])):
        if nowDrink[i-1][a][1] == 2:
            nowDrink[i].append([nowDrink[i-1][a][0],0])
            if large < nowDrink[i-1][a][0]:
                large = nowDrink[i-1][a][0]
        else:
            nowDrink[i].append([drinkCost[i]+nowDrink[i-1][a][0],nowDrink[i-1][a][1]+1])
            if drinkCost[i]+nowDrink[i-1][a][0] > large:
                large = drinkCost[i]+nowDrink[i-1][a][0]
            nowDrink[i].append([nowDrink[i-1][a][0],0])
            if nowDrink[i-1][a][0] > large:
                large = nowDrink[i-1][a][0]

# 만들어진 포도주 배열에서 최대를 선택해서 출력
# large = 0
# for i in range(len(nowDrink[drinkNum-1])):
#     if large < nowDrink[drinkNum-1][i][0]:
#         large = nowDrink[drinkNum-1][i][0]
print(large)

# print(nowDrink[drinkNum-1])

