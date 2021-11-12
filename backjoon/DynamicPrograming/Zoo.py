# 동물원
## 동물원에 가로로 두칸 세로로 N 칸인 우리
## 우리에 사자를 배치할 때, 가로나 세로에서 붙어있게 배치를 못 할때, 사자를 배치하는 경우의 수 구하기
### 입력 : 첫 줄에 우리의 크기 N 을 입력
### 출력 : 첫 줄에 사자를 배치하는 경우의 수를 9901로 나눈 나머지를 출력

import sys  
input = sys.stdin.readline

division = 9901

zooSize = int(input())
 
cage = [0 for i in range(0,100001)]
cage[1] = 3
cage[2] = 7
cage[3] = 17

for i in range(4,100001):
    cage[i] = (cage[i-1] * 2)%division + cage[i-2] % division

print(cage[zooSize] % division)
