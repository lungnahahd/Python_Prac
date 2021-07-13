# 퀵 정렬 : 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
# 피벗(기준)을 설정하고 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 작은 데이터를 찾는다.
# 왼쪽에서 찾은 큰 데이터와 오른쪽에서 찾은 작은 데이터를 교환하는데 교차가 되는 순간에는 작은 데이터와 피벗과 교환
# 이전 피벗을 기준으로 위의 과정들을 다시 반복해서 각 리스트가 하나만 남을때까지 반복
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(array, start, end):
    if start >= end:
        return array
    right = end
    left = start + 1
    done_left = False
    done_right = False
    done = False
    while left < right:
        if array[left] < array[start] and not done_left:
            left = left + 1
            done
        else:
            done_left = True
        if array[right] > array[start] and not done_right:
            right = right - 1
        else:
            done_right = True
        if done_right and done_left:
            done_left = False
            done_right = False
            array[left],array[right] = array[right],array[left]
            break
    if not done_right or not done_left:
        array[left],array[start] = array[start],array[left]
        quicksort(array, start, left - 1)
        quicksort(array,left + 1, end)
result = quicksort(array,0,len(array))
print(result)
