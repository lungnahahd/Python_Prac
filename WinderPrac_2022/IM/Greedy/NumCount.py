# 수 채우기
## 주어진 금액을 2원과 5원 동전을 이용해서만 만들려고 합니다.
## 사용하는 동전의 총 개수를 최소로 하려고 할 때, 2원 동전과 5원 동전은 총 몇 개가 필요한지를 구하는 프로그램을 작성하세요.
### 테크닉 : 그리디 알고리즘


import sys
INT_MAX = sys.maxsize

cost = int(input())

start = cost // 5

result = INT_MAX
while start >= 0:
    temp = cost
    temp -= start*5
    if temp % 2 == 0:
        nowCount = start + (temp//2)
        result = min(result,nowCount)
    start -= 1
if result == INT_MAX:
    print(-1)
else:
    print(result)