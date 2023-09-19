# 매번 가장 작은 것을 선택하는 선택 정렬
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해서 앞에서 두 번째 데이터와 바꾸는 과정을 반복

# 선택 정렬 연습
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

size = len(array)
locate = 0

while size > 0:
    minnum = locate
    for i in range(size):
        if i != 0 and array[minnum] > array[locate + i]:
            minnum = locate + i
    if minnum != locate:
        array[minnum],array[locate] = array[locate],array[minnum]
    size = size -1
    locate = locate + 1
print(array)

# 모법 구현
# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i],array[min_index] = array[min_index], array[i]
# print(array)

########### 230920 버전 선택 정렬 구현
# Python 활용 선택 정렬 구현
## 리스트의 정렬되지 않은 부분에서 가장 최소를 찾고, 가장 왼쪽으로 이동하고 해당 부분은 정렬이 완료된 것으로 간주
## 위의 과정을 전부 정렬될 때까지 반복 수행 

n = int(input())
nums = list(map(int, input().split()))

for k in range(n-1):
    smallVal = nums[k] ## 사실 해당 부분은 굳이 값까지 가지고 다닐 필요는 없음 -> 인덱스로 직접 값 이용!
    smallIdx = k
    for idx in range(k, n):
        if (smallVal > nums[idx]):
            smallVal = nums[idx]
            smallIdx = idx
    nums[k], nums[smallIdx] = smallVal, nums[k]

for num in nums:
    print(num, end = ' ')
