# 이상한 폭탄
## 이상한 폭탄이 N개 있습니다
## 이 이상한 폭탄은 각자에게 부여된 번호가 있고, 같은 번호가 부여된 폭탄끼리 거리가 K안에 있다면 폭발하게 됩니다. 
## 폭탄의 개수 N, 특정 거리인 K, 그리고 폭탄을 나열한 순서가 주어지면, 폭발 할 폭탄중에 부여된 번호가 가장 큰 번호를 출력하는 프로그램을 작성해보세요.
### 테크닉 : 전처리 테크닉 -> 배열을 활용해서 값을 간단학 처리

bombCount, safeDistance = input().split()
bombCount, safeDistance = int(bombCount),int(safeDistance)

check = 0 # 거리에 근접한 폭탄을 처리하기 위한 인덱스로 활용 예정
temp = [-1 for i in range(safeDistance)] # 해당 거리에 있는 폭탄 번호 기입
bigBomb = -1 # 터지는 최대 폭탄 번호르 받는 변수
for i in range(bombCount):
    bombNum = int(input())
    if check == safeDistance: # 특정 거리로만 폭탄 받기
        check = 0
    if bombNum in temp: # 특정 거리 내에 해당 폭탄 번호가 있는지 확인
        bigBomb = max(bigBomb, bombNum)
    temp[check] = bombNum
    check += 1
print(bigBomb)