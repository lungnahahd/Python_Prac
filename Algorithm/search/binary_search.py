# 이진 탐색
## 정렬된 상태에서 탐색 필요

array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

wantnum = 4
center = len(array) // 2
result = -1

def binarysearch(want, array, center):
    if want > array[center]:
        center = center + (center//2)
        binarysearch(want, array, center)
    elif want <array[center]:
        center = center // 2
        binarysearch(want, array, center)
    elif want == array[center]:
        global result
        result = center
binarysearch(wantnum, array, center)
print(array[result])