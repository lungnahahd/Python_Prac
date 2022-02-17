# 정수 두 개의 합
## n개의 정수 주어졌을 때, 이 중 두 개의 원소를 골라 그 합이 k 이하가 되는 경우의 수를 구하는 프로그램을 작성해보세요.
### 테크닉 : Two Pointer 테크닉




numCount, mostBig = input().split()
numCount, mostBig = int(numCount), int(mostBig)

nums = []
for i in range(numCount):
    num = int(input())
    nums.append(num)

nums.sort()
goPoint = 0
resultCount =0

for standPoint in range(numCount-1):
    goPoint = standPoint + 1
    temp = nums[standPoint] # 여기서 이것이 아니라 배열 값을 바로 이용하면 시간 초과 발생 -> 배열은 조회할수록 시간복잡도 증가
    if temp >= mostBig:
        break
    while goPoint < numCount and nums[goPoint] <= mostBig - temp:
        resultCount += 1
        goPoint += 1

print(resultCount)