# 쉬운 계단 수
## 모든 인접한 자리수의 차이가 1인 수를 계단수라고 하며, N이 주어질 때, 길이가 N인 계단 수가 총 몇개인지 구하기
### 입력 : 첫 줄에 원하는 자리수 N 이 입력 (N은 1과 100 사이에 수)
### 출력 : 첫 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력

import sys
input = sys.stdin.readline
N = int(input()) # 자리수 입력 받기

MAX = 1000000000 # 최종으로 나누어 줄 수

starNumList = [[0] * 10 for i in range(N+1)] # 각 자릿수의 끝자리 수의 개수를 체크해서 작성될 배열

# 초기에 한자리 수는 0이 안들어가는 특별한 경우 이므로 초기 설정으로 처리 해주기
for i in range(1,10):
    starNumList[1][i] = 1


for col in range(2, N+1):
    for row in range(10):
        if row == 0:
            starNumList[col][row] = starNumList[col-1][1] # 0일 경우는 이전 자리수가 1인 경우만 올 수 있음
        elif row == 9: 
            starNumList[col][row] = starNumList[col-1][8] # 9일 경우는 이전 자리수가 8인 경우만 올 수 있음
        else:
            starNumList[col][row] = starNumList[col-1][row-1] + starNumList[col-1][row+1] # 1~8인 경우는 이전에 일을 빼고 일을 더한 경우에 가능
result = 0
for i in range(10):
    result += starNumList[N][i]
print(result % MAX) 