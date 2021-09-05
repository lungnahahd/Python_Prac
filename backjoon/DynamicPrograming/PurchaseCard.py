# 카드 구매하기
## 8 가지의 카드가 존재
## 구매 가능한 카드팩의 종류는 1 부터 N개의 카드가 포함된 N가지의 카드팩이 존재
## 각 카드팩은 가격이 지정되어 있고, 해당 가격의 합의 최대를 만족하도록 구매할 예정
### 입력 : 첫 줄에 구매하려는 카드의 갯수, 두 번째 줄에는 각 카드팩의 가격이 나열되어서 입력
### 출력 : 첫 줄에 카드팩 구매의 최대값이 출력

import sys
input = sys.stdin.readline

purchaseNum = int(input()) # 구매하려는 카드의 개수 입력
getList = list(input().split())

costList = [0 for i in range(purchaseNum + 1)]
for i in range(purchaseNum ):
    costList[i + 1] = int(getList[i])

for i in range(1,purchaseNum + 1):
    check = 1
    while check <= (i // 2):
        if costList[i] < costList[check] + costList[i - check]:
            costList[i] = costList[check] + costList[i-check]
        check += 1

print(costList[purchaseNum])