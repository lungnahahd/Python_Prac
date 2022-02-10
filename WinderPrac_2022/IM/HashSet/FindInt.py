# 정수 찾기
## 수열 a와 수열 b가 주어졌을 때, 수열 b의 각 원소가 수열 a에 포함되는지 알아보는 프로그램을 작성해보세요.
### Set 사용 이유 : 중복을 허용하지 않고, 단순히 원소의 유무만 빠르게 확인하면 되므로 사용

numSize = int(input())
numList = list(map(int, input().split()))
numSet = set(numList)

findSize = int(input())
findList = list(map(int,input().split()))

for i in findList:
    if i in numSet:
        print(1)
    else:
        print(0)