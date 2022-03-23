# 다음 순열
## 사전순으로 다음에 오는 순열을 구하는 프로그램
## 이미 순열의 마지막인 경우는 -1 출력
### 입력 : 첫 줄에 N 이 입력, 둘째 줄에 순열이 입력
### 출력 : 첫 줄에 다음으로 오는 순열을 출력



import sys
import copy
input = sys.stdin.readline

numLarge = int(input())
nowArr = list(map(int,input().split()))

frontIdx, backIdx = -1, -1

# C++ 활용 시에는 next_permutation을 이용하면 수비게 구할 수 있으나, Python은 해당 알고리즘을 지원해주지 않아 직접 구현 필요
# 아래의 알고리즘을 통해 바로 다음 순열을 구할 수 있음
def NextArr():
    global frontIdx, backIdx
    for i in range(numLarge-1,0,-1): # 리스트를 거꾸로 출력하는 방법
        if nowArr[i] > nowArr[i-1]: # 바로 다음 숫자가 더 큰 경우를 뒤에서부터 찾고 해당 인덱스를 기록
            frontIdx = i-1
            backIdx = i
            break # 발견 즉시 동작 멈추기
    
    if frontIdx == -1 or backIdx == -1: # 위에서 찾는 경우의 수가 단 하나도 존재하지 않는다면,  주어진 순열이 마지막 경우이므로 -1 출력
        print(-1)
    else: # 마지막 순열이 아닌 경우 아래의 동작 
        for i in range(numLarge-1,frontIdx,-1):
            if nowArr[frontIdx] < nowArr[i]: # backIdx까지 뒤에서부터 확인해서 frontIdx 위치의 값보다 큰 값이 나오면 바로 swap하기
                # 리스트의 두 값의 인덱스 위치를 변경하는 코드 작성
                temp = copy.deepcopy(nowArr[frontIdx]) # 변수 값을 주소가 아닌 깊은 복사 진행
                nowArr[frontIdx] = nowArr[i]
                nowArr[i] = temp
                break # 발견 즉시 동작 멈추기
        frontTemp = nowArr[:backIdx]    
        backTemp = nowArr[backIdx:]
        backTemp.sort() # backIdx부터 마지막까지 부분을 오름차순 정렬하고 앞 부분과 이어 붙이기
        result = frontTemp + backTemp
        for i in result:
            print(i, end=' ')


NextArr()






















# ########### 다음 순열 재귀함수 1차 구현 => 런타임 에러
# import sys
# input = sys.stdin.readline

# numLarge = int(input())
# nowArr = list(map(int,input().split()))
# check = [False for _ in range(numLarge+1)]
# next = False
# save = []


# def FindArr(count):
#     global next
#     if count == numLarge:
#         if next:
#             for j in save:
#                 print(j,end=' ')
#             next = False
#         if save == nowArr:
#             next = True
#         return
    
#     for i in range(1,numLarge+1):
#         if not check[i]:
#             check[i] = True
#             save.append(i)
#             FindArr(count+1)
#             check[i] = False
#             save.pop()


# FindArr(0)
# if next:
#     print("-1")