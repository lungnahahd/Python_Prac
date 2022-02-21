# 삼 오 무
## 1부터 차례대로 숫자를 적는데, 3이나 5의 배수는 숫자 대신 "Moo"라고 적습니다. 예를 들어 1부터 16까지의 숫자를 적는다면 아래와 같습니다.
## 1, 2, Moo, 4, Moo, Moo, 7, 8, Moo, Moo, 11, Moo, 13, 14, Moo, 16
## 이 때, N번째로 적히는 숫자는 무엇인지 구하는 프로그램을 작성해보세요.
### 테크닉 : 변형된 이진 탐색

where = int(input())

left = 0
right = 20**9
result = -1

while left <= right:
    mid = (left + right) // 2
    cal = mid - ((mid // 3) + (mid // 5) - (mid // 15)) # 해당 숫자가 몇 번째 인지 확인하는 과정
    if cal == where:
        result = mid
        while result % 3 == 0 or result % 5 == 0: # 혹시 골랐는데, 해당 숫자가 Moo인 경우 처리(ex) 5번째 숫자를 골랐느데 9가 나옴
            result -= 1
        break
    if cal > where:
        right = mid -1
    else:
        left = mid + 1


print(result) 