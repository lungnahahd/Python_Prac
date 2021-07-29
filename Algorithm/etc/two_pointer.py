# 투 포인터 알고리즘
## 리스트에 순차적으로 접근할 때, 두 개의 포인터의 위치를 기록하면서 처리하는 알고리즘
### 시작점과 끝점을 명시해서 진행(접근 범위를 표현)
### 이를  활용해서 주어진 수열에서 특정 합이 N인 연속 수열의 갯수 구하기 가능
#### 시작 포인트와 끝 포인트를 0으로 두고 시작하면서 시작점에서 끝점의 합이 찾는 것과 같다면 결과치를 하나 증가
#### 찾는 것보다 작다면 끝 포인트를 하나 증가하고 크다면 시작 포인트를 하나 증가시키면서 알고리즘을 진행
#### 위의 과정을 더 이상 진행할 수 없을 때까지 진행한다면 최적의 해를 얻을 수 있음

want = input("원하는 구간 합을 입력하시오 : ")
wantsum = int(want)

array = [1,2,3,2,5]
#array = [3,1,1,1,1]
big = False
startPointer = 0
endPointer = 0
checksum = 0
count = 0

while startPointer <= endPointer and endPointer < len(array):
    if startPointer == endPointer:
        checksum = array[startPointer]
        if endPointer == len(array):
            break
    elif big:
        checksum += array[endPointer]
        big = False
    if checksum == wantsum:
        count += 1
        if startPointer == endPointer:
            startPointer += 1
            endPointer += 1
        else:
            checksum -= array[startPointer]
            startPointer +=1
    elif wantsum > checksum:
        endPointer += 1
        big = True
        if endPointer > len(array):
            break
    elif wantsum < checksum:
        checksum -= array[startPointer]
        startPointer += 1

print(count)
# -----------------------------------------------------
## 참고 코드
# datanum, datasum = 5, 5
# data = [1,2,3,2,5]

# count = 0
# partial_sum = 0
# end = 0

# for start in range(datanum):
#     while partial_sum < datasum and end < datanum :
#         partial_sum += data[end]
#         end += 1
#     if partial_sum == datasum:
#         count += 1
#     partial_sum -= data[start]

# print(count)