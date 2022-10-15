# 숫자의 개수
## n개의 숫자가 오름차순으로 정렬된 상태로 주어집니다.
## 이후 m개의 숫자가 추가적으로 주어졌을 때, 각각의 숫자가 처음 주어진 n개의 숫자 중 몇 번 나왔는지를 구하는 프로그램을 작성해보세요.
### 테크닉 : 이진탐색을 응용해서 lowerBound, upperBound, CustomBound 활용

n,m = input().split()
numCount, cmdCount = int(n),int(m)

numArr = list(map(int,input().split()))

def lowerBound(target,numArr):
    right = len(numArr)-1
    left = 0
    minNum = len(numArr)

    while left <= right:
        mid = (right + left) // 2
        if numArr[mid] >= target:
            minNum = min(minNum,mid)
            right = mid -1
        else:
            left = mid + 1

    return minNum

def upperBound(target,numArr):
    right = len(numArr)-1
    left = 0
    minNum = len(numArr)

    while left <= right:
        mid = (right + left) // 2
        if numArr[mid] > target:
            minNum = min(minNum,mid)
            right = mid -1
        else:
            left = mid +1
    return minNum

for i in range(cmdCount):
    want = int(input())
    lowerNum = lowerBound(want,numArr)
    upNum = upperBound(want,numArr)
    print(upNum-lowerNum)


## 모범 코드
#     # 변수 선언 및 입력
# n, m = tuple(map(int ,input().split()))
# arr = list(map(int, input().split()))


# def lower_bound(target):
#     left, right = 0, n - 1
#     min_idx = n

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] >= target:
#             min_idx = min(min_idx, mid)
#             right = mid - 1
#         else:
#             left = mid + 1
    
#     return min_idx


# def upper_bound(target):
#     left, right = 0, n - 1
#     min_idx = n

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] > target:
#             min_idx = min(min_idx, mid)
#             right = mid - 1
#         else:
#             left = mid + 1
    
#     return min_idx


# for _ in range(m):
#     x = int(input())
#     count = upper_bound(x) - lower_bound(x)

#     print(count)
