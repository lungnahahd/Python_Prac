# 쉬운 계단 수
## 모든 인접한 자리수의 차이가 1인 수를 계단수라고 하며, N이 주어질 때, 길이가 N인 계단 수가 총 몇개인지 구하기
### 입력 : 첫 줄에 원하는 자리수 N 이 입력 (N은 1과 100 사이에 수)
### 출력 : 첫 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력

import sys
input = sys.stdin.readline
N = int(input()) # 자리수 입력 받기

MAX = 1000000000 # 최종으로 나누어 줄 수

starNumList = [0 for i in range(101)]

starNumList[1] = 9
for i in range(2,101):
    starNumList[i] = ((starNumList[i-1] * 2) - 1) % MAX

print(starNumList[N])