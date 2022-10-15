# 구간 크기의 합
## 수직선 상에 n개의 구간이 주어졌을 때, 모든 구간을 합친 이후의 총 구간 크기의 합을 구하는 프로그램을 작성해보세요.
### 테크닉 : +1-1 테크닉

caseSize = int(input())

points = []

for i in range(caseSize):
    start, end = input().split()
    points.append((int(start),+1))
    points.append((int(end),-1))

points.sort()

sumValue = 0
end = 0
start = 0
totalLong = 0
for point,value in points:
    if sumValue == 0:
        end = point
        sumValue += value
    else:
        sumValue += value
        if sumValue == 0:
            start = point
            totalLong += (start - end)

print(totalLong)