# 연속합2
## 수열이 주어지고, 연속된 몇 개의 수를 선택해서 구할 수 있는 가장 큰 합 구하기
## 단, 수는 한 개 이상 선택해야하고, 수열에서 수를 하나 제거할 수도 있음(제거하지 않아도 됨)
### 입력 : 첫 줄에 수열의 길이, 두번 쨰 줄에 수열이 입력
### 출력 : 첫 줄에 가장 큰 합을 출력

import sys
input = sys.stdin.readline

size = int(input())
list = input().split()

if size == 1:
    print(int(list[0]))
else:
    strait = [0 for i in range(size)] # 중간에 비는 것 없는 수열
    jump = [0 for i in range(size)] # 중간에 비는 것이 존재하는 수열
    
    strait[0] = int(list[0])

    for i in range(1,size):
        strait[i] = max(strait[i-1] + int(list[i]), int(list[i]))
        jump[i] = max(strait[i-1],jump[i-1] + int(list[i]))

    # 각 경우에서 나오는 최대 수열의 합
    max_strait = max(strait)
    max_jump = max(jump[1:])

    print(max(max_jump,max_strait)) # 경우를 나눈 수열의 합 중 가장 큰 것을 선택해서 출력