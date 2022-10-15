#  이진탐색 활용 -> 숫자 빠르게 찾기
## n개의 숫자가 오름차순으로 정렬된 상태로 주어집니다. 이후 m개의 숫자가 추가적으로 주어졌을 때, 각각의 숫자가 처음 주어진 n개의 숫자 중 몇 번째로 나온 숫자인지를 구하는 프로그램을 작성해보세요
### 테크닉 : 이진탐색

numCount, cmdCount = input().split()
numCount,cmdCount = int(numCount), int(cmdCount)

nums = list(map(int, input().split()))

def findNum(want,nums):
    right = len(nums) - 1
    left = 0
    while left <= right:
        mid = (left+right) // 2 # 몫을 중간 값으로 활용
        if nums[mid] == want:
            return mid + 1
        elif nums[mid] > want:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

for i in range(cmdCount):
    want = int(input())
    where = findNum(want,nums)
    print(where)



## 모범코드
#     # 변수 선언 및 입력:
# n, m = tuple(map(int, input().split()))
# arr = list(map(int, input().split()))


# def find(target):
#     left, right = 0, n - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid

#         if arr[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
    
#     return -1


# for _ in range(m):
#     x = int(input())
#     index = find(x) # 이진탐색을 진행합니다.

#     print(-1 if index < 0 else index + 1)
