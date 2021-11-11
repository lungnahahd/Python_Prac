# RGB 거리
## 1번 집부터 N번 집이 순서대로 존재할 때, 집은 빨강, 파랑, 초록 중 하나의 색을 칠해야 함
## 해당 색들을 칠하는 비용이 주어졌을 경우, 아래 규칙을 만족하면서 모든 집을 칠하는 최솟값 구하기
## 규칙 : 1번 집과 2번 집의 색은 달라야 함
## 규칙 : N번 집의 색은 N-1번 집의 색과 달라야 함
## 규칙 : i번 집의 색은 i-1번, i+1번 집의 색과 달라야 함
### 입력 : 첫 줄에 집의 수가 입력되고 그 이후에 줄부터 R,G,B의 색으로 칠할 때의 비용에 입력
### 출력 : 첫 줄에 모든 집을 칠하는 최소 비용이 출력

import sys 
input = sys.stdin.readline

houseSize = int(input())

red = [0 for i in range(houseSize)]
green = [0 for i in range(houseSize)]
blue = [0 for i in range(houseSize)]
result = [0 for i in range(3)]

for i in range(houseSize):
    r,g,b = input().split()
    red[i] = int(r)
    green[i] = int(g)
    blue[i] = int(b)

result[0] = red[0]
result[1] = green[0]
result[2] = blue[0]

for i in range(1,houseSize):
    temp1 = result[0]
    temp2 = result[1]
    temp3 = result[2]
    result[0] = min(temp2,temp3) + red[i]
    result[1] = min(temp1,temp3) + green[i]
    result[2] = min(temp1,temp2) + blue[i]

print(min(result[0],result[1],result[2]))