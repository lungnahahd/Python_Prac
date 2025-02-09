# N과 M
## 자연수 N과 M이 주어진 경우, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 구하는 프로그램'
### 입력 : 자연수 N과 M이 입력
### 출력 : 수열을 출력

# N과 M은 8 이하인 자연수이므로, 반복문으로 시간 초과 없이 구현 가능

import sys
input = sys.stdin.readline

numLargest, numCount = tuple(map(int,input().split()))
checkNumIn = [False for _ in range(numLargest+1)] # 해당 숫자가 리스트 내에 저장되어 있는지를 판별하는 배열

save = [] # 숫자 저장 리스트

def MakeNumArr(num):
    if num == numCount: # 리스트가 가득 차면 바로 출력
        for k in save:
            print(k, end=' ')
        print()
        return

    for i in range(1,numLargest+1):
        if not checkNumIn[i]: # 해당 숫자가 이미 리스트에 있는지 판별
            checkNumIn[i] = True
            save.append(i) # 없는 숫자는 리스트에 넣기
            MakeNumArr(num+1) # 리스트에 넣고 BFS 재실행
            checkNumIn[i] = False # 리스트에서 해당 숫자 바로 빼기 -> 바로 빼도 재귀함수로 인해 처리가 바로 가능
            save.pop()



MakeNumArr(0)
