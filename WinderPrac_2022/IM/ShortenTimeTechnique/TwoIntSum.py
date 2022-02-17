numCount, mostBig = input().split()
numCount, mostBig = int(numCount), int(mostBig)

nums = []
for i in range(numCount):
    num = int(input())
    nums.append(num)


goPoint = 0
resultCount =0

for standPoint in range(numCount-1):
    goPoint = standPoint + 1
    if nums[standPoint] >= mostBig or nums[goPoint] >= mostBig:
        continue
    while goPoint < numCount:
        if nums[standPoint] + nums[goPoint] <= mostBig:
            resultCount += 1
        goPoint += 1

print(resultCount)