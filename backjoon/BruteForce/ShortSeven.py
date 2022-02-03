# 일곱 난쟁이
## 키의 합이 100 이 되는 일곱 난쟁이를 찾는 프로그램
### 입력 : 아홉 개의 줄에 난쟁이들의 키가 입력
### 출력 : 키의 합이 100 이 되는 일곱 난쟁이의 키를 오름차순으로 출력

import sys
input = sys.stdin.readline

height = []
# 9명의 난쟁이의 높이 입력을 받기
for i in range(9):
    a = int(input())
    height.append(a)

for i in range(9):
    for j in range(i+1,9):
        temp = height[:] # 파이썬 리스트를 똑같이 복사 -> 이렇게 안 하고 대입하면 주소가 복사!
        print(temp)
        temp.pop(i)
        temp.pop(j)
        print(i)
        print(j)
        print(temp)
        sum = sum(temp)
        if sum == 100:
            break
    if sum == 100:
        break
print(temp)