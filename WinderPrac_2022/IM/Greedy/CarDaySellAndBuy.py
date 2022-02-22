# 자동차 단일 거래 이익 최대화하기
## 향후 n년 간의 자동차 가격 정보가 미리 주어졌을 때, 자동차를 단 한 번 사서 되팔 때의 이익을 최대화하고자 합니다.
## 낼 수 있는 최대 이익을 출력하는 프로그램을 작성해보세요. 
## 단, 자동차를 사기 전에는 팔 수 없습니다.
### 테크닉 : 그리디 알고리즘

count = int(input())
costDay = list(map(int, input().split()))

buy = costDay[0]
getMoney = 0
for i in range(1,count):
    now = costDay[i] - buy
    if now >= 0:
        getMoney = max(getMoney, now)
    else:
        buy = costDay[i]
print(getMoney)