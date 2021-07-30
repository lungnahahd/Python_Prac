# 백준 오큰수 문제
## 첫째 줄에 수열의 크기 N이 주어지고, 둘째 줄부터는 수열 자체가 입력
### 수열이 하나씩 모두 대상이 되면서 대상보다 오른쪽에서 큰 수를 확인
### 그 중 가장 대상이랑 가까운, 즉 가장 왼쪽에 있는 수를 선택

import sys

input = sys.stdin.readline
size = int(input())

num_array = []
result = []
num_list = input()
num_array = num_list.split()

# 한 칸씩 이동시킬 변수
count = 1

if size != 1:
    for i in num_array:
        check = count
        while check < len(num_array):
            if int(i) < int(num_array[check]):
                result.append(int(num_array[check]))
                break
            else:
                if check == (len(num_array) - 1):
                    result.append(-1)
                    break
                check += 1
        count += 1
result.append(-1)

for i in result:
    print(i, end=' ')