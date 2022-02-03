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

# 9 난쟁이의 키의 합
totalSum = sum(height)

# 제거할 난쟁이들을 선별하는 과정
for i in range(9):
    for j in range(i+1,9):
        tempSum = totalSum - (height[i] + height[j])
        if tempSum == 100:
            height.pop(j)
            height.pop(i)
            break
    if tempSum == 100:
        break
    
height.sort() # 파이썬에서 제공하는 리스트 정렬(기본이 오름차순)
for i in range(7):
    print(height[i])