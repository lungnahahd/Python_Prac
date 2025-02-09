# 정수 삼각형
## 정수로 이루어진 삼각형이 주어지고, 맨 위에서 부터 시작해서 내려올 때까지 합의 최대 구하기
## 현재 층에서 선택된 수의 대각선 왼쪽 또는 오른쪽의 수만 선택 가능
### 입력 : 첫 줄에 삼각형의 크기가 입력되고 둘째 줄부터 n+1 번째 줄까지 삼각형 입력
### 출력 : 합의 최대를 출력

import sys
input = sys.stdin.readline

stair = int(input())
costStair = [[] for i in range(stair)]

# 정수 삼각형의 값 입력 받기
for i in range(stair):
    get = input().split()
    costStair[i] = get

result = [[] for i in range(stair)] # 결과를 담을 배열
result[0].append(int(costStair[0][0]))

# 경우를 나누어서 결과 배열을 생성
for i in range(1, stair):
    for j in range(len(costStair[i])):
        if j == 0:
            result[i].append(result[i-1][j] + int(costStair[i][j]))
        elif j == len(costStair[i])-1:
            result[i].append(result[i-1][j-1] + int(costStair[i][j]))
        else:
            result[i].append(max(result[i-1][j-1], result[i-1][j]) + int(costStair[i][j]))
# 마지막 결과 배열 중 최대를 출력
print(max(result[stair-1]))