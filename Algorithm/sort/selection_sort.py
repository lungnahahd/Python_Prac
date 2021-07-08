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
