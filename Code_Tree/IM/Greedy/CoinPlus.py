# 동전 더하기
## 서로 다른 동전 n 종류로 금액 k를 완성시키기 위해 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하세요.
## 단, 2번째부터 주어지는 동전의 가치값은 항상 바로 전 동전의 가치의 배수로 주어집니다.
### 테크닉 : 그리디 알고리즘

n, k = input().split()
kind, cost = int(n), int(k)

coin = []
for i in range(kind):
    get = int(input())
    coin.append(get)

result = 0
now = kind - 1

# 큰 동전부터 처리하는 그리디 적용
while cost != 0:
    num = cost // coin[now]
    cost = cost - num*coin[now]
    result += num
    now -= 1

print(result)