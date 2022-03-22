# 다음 순열
## 사전순으로 다음에 오는 순열을 구하는 프로그램
## 이미 순열의 마지막인 경우는 -1 출력
### 입력 : 첫 줄에 N 이 입력, 둘째 줄에 순열이 입력
### 출력 : 첫 줄에 다음으로 오는 순열을 출력

import sys
input = sys.stdin.readline

numLarge = int(input())
nowArr = list(map(int,input().split()))
check = [False for _ in range(numLarge+1)]
next = False
save = []


def FindArr(count):
    global next
    if count == numLarge:
        if next:
            for j in save:
                print(j,end=' ')
            next = False
        if save == nowArr:
            next = True
        return
    
    for i in range(1,numLarge+1):
        if not check[i]:
            check[i] = True
            save.append(i)
            FindArr(count+1)
            check[i] = False
            save.pop()


FindArr(0)
if next:
    print("-1")