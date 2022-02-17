# 화재 진압
## 1차 수직전 상 위에 화재가 발생할 가능성이 있는 서로 다른 n개의 위치와 소방서 m개의 위치가 주어집니다. 
## 화재는 정확히 한 곳에서만 발생하며, 가장 근처에 있는 소방서에서 출동하여 진입한다고 합니다.
## 거리 1을 이동하는 데 시간이 1초가 소요된다고 했을 때, 각 위치에서 화재가 발생하는 데 이를 진압하는 데 걸리는 시간 중 가장 오래 걸리는 시간을 구하는 프로그램을 작성해보세요.
### 테크닉 : Two Pointer

event, fireman = input().split()
event, fireman = int(event), int(fireman)

hotPlace = list(map(int, input().split()))
hotPlace.sort()
manPlace = list(map(int, input().split()))
manPlace.sort()

goTime = 0
resultLong = 0
nearPlace = 0

for i in range(event):
    goTime = 0
    hot = hotPlace[i] # 불이 난 위치를 선택
    while goTime < fireman and manPlace[goTime] < hot:
        goTime += 1
    nearPlace = hot - manPlace[goTime -1] # 불난 위치 이전에 가장 가까운 소방서 거리 계산
    if goTime < fireman: # 불난 위치 이후에 가장 가깡누 소방서 거리 계산(없다면 넘어가기)
        nearPlace = min(nearPlace, manPlace[goTime] - hot)
    resultLong = max(resultLong,nearPlace)
print(resultLong)