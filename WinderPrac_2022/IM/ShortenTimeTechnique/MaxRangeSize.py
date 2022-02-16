# 최대 구간의 크기
## 수직선 상에 n개의 구간이 주어졌을 때, 모든 구간을 합친 이후 남아 있는 구간들 중 가장 큰 구간의 크기를 구하는 프로그램을 작성해보세요
### 테크닉 : +1-1 테크닉

caseSize = int(input())

numRanges = []

for i in range(caseSize):
    start, end = input().split()
    numRanges.append((int(start),+1))
    numRanges.append((int(end),-1))

numRanges.sort()

bigRange = -1
sumDistance = 0
start = 0
end = 0
count = 0
passCheck = True # 종료와 시작이 겹치는 경우 범위를 이어가기 위한 변수
for point,value in numRanges:
    if sumDistance == 0 and passCheck:
        end = point
        sumDistance += value
    else:
        sumDistance += value
        if sumDistance == 0:
            if count+1 < len(numRanges):
                beforePoint,beforeValue = numRanges[count+1]
                if beforePoint == point and beforeValue != -1:
                    passCheck = False # 범위를 이어가도록 변수 설정
                else:
                    passCheck = True
                    start = point
                    distance = start - end
                    bigRange = max(bigRange,distance)
            else:
                passCheck = True
                start = point
                distance = start - end
                bigRange = max(bigRange,distance)
    count += 1

print(bigRange)