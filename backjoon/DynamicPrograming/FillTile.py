# 타일 채우기
## 3XN 크기의 벽을 2X1, 1X2 크기의 타일로 채우는 경우의 수 구하기
### 입력 : 첫 줄에 N 입력 (1 ~ 30)
### 출력 : 경우의 수를 출력

import sys
input = sys.stdin.readline

size = int(input())
count = [0 for i in range(31)] # 배열의 크기는 30까지의 입력을 받을 수 있게 설정
count[2] = 3 # 2일 경우는 케이스를 나누기 보다는 특이 케이스로 처리
if size >= 4: # 4일 때부터 반복문 시작
    for i in range(4,size+1):
        if i % 2 == 0: # 짝수일 경우만 점화식 적용
            multi = 2 
            for j in range(i):
                if j % 2 == 0 and j != 0:
                    if j == (i-2):
                        multi = 3 # 바로 이전 짝수의 값은 X3을 해주어야 하므로 이를 처리
                    count[i] += count[j] * multi
                    multi = 2
            count[i] +=2 # 마지막 시나리오를 처리
print(count[size]) # 결과 출력