# 가장 많이 겹치는 구간
## 일직선 위에 n개의 구간이 주어졌을 때, 구간이 가장 많이 겹치는 부분에서 몇 개의 구간이 겹치는지를 구하는 프로그램을 작성해보세요.
### 테크닉 : +1-1 테크닉


# 주어진 수의 범위가 크므로 리스트로 하면 안되고 튜플로 처리해야함
rangeSize = int(input())
getNum = []


for i in range(rangeSize):
    start, end = input().split()
    getNum.append((int(start),+1))
    getNum.append((int(end),-1))

getNum.sort()

temp = 0
result = 0
for i in range(len(getNum)):
    _,count = getNum[i]
    temp += count
    if temp > result:
        result = temp

print(result)