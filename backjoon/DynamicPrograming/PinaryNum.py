# 이친수
## 0과 1로 이루어진 수를 이진수라고 부르는 데, 이 중 특별한 성질을 갖는 수를 이친수라고 칭함
## 이친수는 0으로 시작하지 않으며, 1이 두 번 연속으로 나타나지 않음
### 입력 : 첫 줄에 자릿수 N이 입력
### 출력 : 첫 줄에 N자리 이친수를 출력

import sys
input = sys.stdin.readline

N = int(input()) # 이친수 자릿수 입력

count = [[0] * 2 for i in range(N+1)] # 각 자리가 0인지 1인지 확인하는 배열

count[1][1] = 1

for col in range(2,N+1):
    for row in range(2):
        if row == 0: # 이전 자릿수가 0인 경우는 어떤 수라도 올 수 있음
            count[col][0] += count[col - 1][0]
            count[col][1] += count[col - 1][0]
        elif row == 1 : # 이전 자릿수가 1인 경우는 1이 다시 올 수 없어서 0만 와야 함
            count[col][0] += count[col-1][1]

result = 0
for i in range(2):
    result += count[N][i] # 원하는 자릿수의 0 또는 1로 끝나는 경우를 모두 카운트

print(result) # 결과 출력
