# 계수 정렬 : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
# 데이터의 크기 범위가 제한 되어 정수 형태로 표현할 수 있을 때만 사용
# 가장 큰 데이터와 가장 작은 데이터의 차이가 너무 크면 사용하기 어려움
# 별도의 리스트를 선언하고 데이터를 하나식 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시키고 이를 이용해 데이터를 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

countnum = [0 for i in range(max(array) + 1)]

for i in range(len(array)):
    countnum[array[i]] += 1

point = 0
for i in range(max(array) + 1):
    for j in range(countnum[i]):
        array[point] = i
        point += 1
print(array)