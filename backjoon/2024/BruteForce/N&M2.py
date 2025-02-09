# N과 M(2)
## 1 부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열(수열은 오름 차순)
### 입력 : 첫 줄에 자연수 N과 M이 입력
### 출력 : 첫 줄에 수열을 출력

import sys
input = sys.stdin.readline

numLarge, numCount = tuple(map(int,input().split()))

check = [False for _ in range(numLarge + 1)]
finNum = [False for _ in range(numLarge + 1)]
save = []


def FindNumArr(count):
    if count == numCount:
        for k in save:
            print(k,end=' ')
        print()
        return
    
    for i in range(1, numLarge+1):
        if not check[i]:
            if len(save) != 0 and save[-1] > i: # 오름 차순 정렬된 경우만 출력하기 위한 조건, 리스트의 맨 마지막 수보다 넣을 수가 작을 경우 넣지 말기
                continue
            check[i] = True
            save.append(i)
            FindNumArr(count+1)
            save.pop()
            check[i] = False

FindNumArr(0)