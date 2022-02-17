# 정수 N 개의 합
## 크기가 n인 수열이 주어졌을 때, 이 중 연속하는 몇 개의 원소들의 합이 m이 되는 경우의 수를 구하는 프로그램을 작성해보세요.
### 테크닉 : Two Pointer 테크닉

numCount, destination = input().split()
numCount, destination = int(numCount), int(destination)

nums = list(map(int, input().split()))
prefix = []
prefix.append(0)
sumTemp = 0

# 누적합 배열 활용
for i in nums:
    sumTemp += i
    prefix.append(sumTemp)

resultCount = 0

for stand in range(numCount+1):
    for go in range(stand+1,numCount+1):
        nowSum = prefix[go] - prefix[stand]
        if nowSum == destination:
            resultCount += 1
            break

print(resultCount)