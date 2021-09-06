# 카드 구매하기 2
## 8 가지의 카드가 존재
## 구매 가능한 카드팩의 종류는 1 부터 N개의 카드가 포함된 N가지의 카드팩이 존재
## 각 카드팩은 가격이 지정되어 있고, 해당 가격의 합의 최대를 만족하도록 구매할 예정
### 입력 : 첫 줄에 구매하려는 카드의 갯수, 두 번째 줄에는 각 카드팩의 가격이 나열되어서 입력
### 출력 : 첫 줄에  카드팩 구매를 위해 지불할 최소 금액이 출력

import sys
input = sys.stdin.readline

cardSum = int(input()) # 구매할 카드 개수 입력
getList = list(input().split()) # 입력을 리스트로 입력
cardCost = [0 for i in range(cardSum + 1)] 

for i in range(cardSum):
    cardCost[i+1] = int(getList[i]) # 카드 가격을 리스트로 다시 받기

for i in range(1, cardSum + 1): # 카드 가격을 최소로 갱신하는 반복문
    count = 1
    while count <= (i//2):
        if cardCost[i] > cardCost[count] + cardCost[i - count]:
            cardCost[i] = cardCost[count] + cardCost[i - count]
        count += 1

print(cardCost[cardSum])
