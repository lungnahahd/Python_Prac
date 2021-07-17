# 퀵 정렬 : 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
# 피벗(기준)을 설정하고 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 작은 데이터를 찾는다.
# 왼쪽에서 찾은 큰 데이터와 오른쪽에서 찾은 작은 데이터를 교환하는데 교차가 되는 순간에는 작은 데이터와 피벗과 교환
# 이전 피벗을 기준으로 위의 과정들을 다시 반복해서 각 리스트가 하나만 남을때까지 반복
from abc import abstractproperty


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(array, start, end):
    if start >= end:
        return 
    right = end
    left = start + 1
    while left <= right:
        while left <= end:
            if array[start] < array[left]:
                break
            left = left + 1
        while right > start:
            if array[start] > array[right]:
                break
            right = right - 1
        if left > right:
            array[right],array[start] = array[start], array[right]
            break
        else:
            array[right],array[left] = array[left], array[right]
    print(array)
    quicksort(array,start,right -1)
    quicksort(array,right+1,end)

quicksort(array,0,len(array)-1)
print(array)

# 참고 답안
# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array, start, end):
#     if start >= end: # 정렬 시에 남는 원소가 하나이면 종료
#         return
#     pivot = start # 피벗은 start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left],array[right] = array[right], array[left]
#     quick_sort(array,start, right -1)
#     quick_sort(array,right + 1, end)
# quick_sort(array,0,len(array)-1)
# print(array)