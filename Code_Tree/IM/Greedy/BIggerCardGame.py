# 높은 숫자의 카드가 이기는 게임
## A와 B가 카드게임을 하고 있습니다. 1부터 2N까지 번호가 쓰인 카드가 한 장씩 총 2N장 있으며, A와 B가 카드를 N개씩 나눠 가집니다. 
## A와 B는 한 번에 카드 한 장씩을 내고, 더 큰 숫자의 카드를 가진 사람이 점수를 1점 얻습니다
## 카드는 한 턴에 한 번 까지만 낼 수 있고, A와 B는 모든 카드를 다 낼 때 까지 이를 N번 반복합니다.
## B가 카드를 내는 순서가 주어졌을 때, A가 얻을 수 있는 점수의 최댓값을 구하는 프로그램을 작성해보세요.
### 테크닉 : 그리디 알고리즘


import heapq

n = int(input())
bCard = []
for i in range(n):
    get = int(input())
    bCard.append(get)

aCard = []
aCheck = []
for i in range(2*n):
    if i+1 not in bCard:
        aCard.append(i+1)
        aCheck.append(True)

aCard.sort()
bCard.sort()

result = 0
for i in bCard:
    noBig = True
    for j in aCard:
        if j > i:
            aCard.remove(j)
            noBig = False
            break
    
    if not noBig:
        result += 1
print(result)