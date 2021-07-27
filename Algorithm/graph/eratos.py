# 에라토스의 체
## 하나의 소수가 아닌 특정 범위에서 소수가 몇 개 있는지 판별하는 알고리즘
## 2부터 N까지의 모든 자연수를 나열하고 매번 아직 처리하지 않은 소수 i를 이용해서 제거하지 않고, i의 배수를 모두 제거하는 과정으로 소수 갯수 구하기

import math
num_range = input("원하는 숫자를 입력해주세요! : ")
num_range = int(num_range)

result_count = 0
result_list = []
check1 = [False for i in range(0,2)]
check2 = [True for i in range(2, num_range + 1)]
check = check1 + check2

for i in range(2,num_range + 1):
    if check[i]:
        check[i] = False
        num = i
        result_count += 1
        result_list.append(i)
        count = 2
        num = i * count
        while num <= num_range:
            check[num] = False
            count += 1
            num = i * count
            
    else:
        continue

print(result_count)
print(result_list)