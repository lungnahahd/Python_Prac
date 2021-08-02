# 백준 오큰수 문제
## 첫째 줄에 수열의 크기 N이 주어지고, 둘째 줄부터는 수열 자체가 입력
### 수열이 하나씩 모두 대상이 되면서 대상보다 오른쪽에서 큰 수를 확인
### 그 중 가장 대상이랑 가까운, 즉 가장 왼쪽에 있는 수를 선택

import sys

input = sys.stdin.readline
size = int(input())

# 결과를 담는 배열
result = [-1 for i in range(size)]
# 숫자열을 나열 받는 부분
num_list = input()
num_array = num_list.split()

# 배열을 숫자로 형변환하는 부분
for i in range(size):
    num_array[i] = int(num_array[i])

tempSave = []
tempSave.append(0)

for i in range(1, size):
    for i in range(len(tempSave)):
        if num_array[tempSave[-1]] < num_array[i]:
            result[tempSave.pop()] = num_array[i]
        else:
            break
    tempSave.append(i)
print(tempSave)