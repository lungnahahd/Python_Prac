# 삽입 정렬 : 특정 데이터를 적절한 위치에 '삽입'한다는 의미
# 특정한 데이터의 왼쪽에 있는 데이터들은 이미 정렬되어있으므로 자기보다 작은 데이터를 만나면 그 자리에 바로 삽입
# 특정한 데이터가 적절한 위치에 들어가기 전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
from collections import deque

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    i = i+1
    while i >0 and i < len(array) :
        if array[i-1] < array[i]:
            break
        else:
            array[i-1],array[i] = array[i],array[i-1]
            i = i -1
print(array)