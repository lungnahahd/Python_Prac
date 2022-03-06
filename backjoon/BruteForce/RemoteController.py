# 리모컨
## 고장난 리모컨이 주어졌을 때, 특정 채널로 이동하기 위한 최소의 버튼 클릭 횟수를 구하는 프로그램
## 참고로 현재 보고 있는 채널은 100번
### 입력 : 첫 줄에 원하는 채널, 두 번째 줄에 고장난 버튼의 개수, 마지막에 고장난 버튼의 종류가 입력
### 출력 : 버튼 클릭의 최소 횟수

import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

channel = int(input()) # 원하는 채널
channelList = list(map(int, str(channel))) # 채널은 한글자씩 처리하기 위해 리스트로 관리 
num = int(input()) # 고장난 버튼의 개수
notWork = set() # 고장난 버튼을 set으로 빠르게 찾기 가능
if num != 0:
    kindBut = list(map(int,input().split())) # 고장난 버튼을 받기
    for i in kindBut:
        notWork.add(i)

minVal = abs(channel - 100)
check = True

for i in range(1000001): # 1억 번을 도는 for문이 1초가 걸리므로 이 정도의 시간 복잡도는 충분히 for문으로 감당 가능
    iList = list(map(int,str(i)))
    for j in iList:
        if int(j) in notWork:
            check = False
    if check:
        minVal = min(minVal,abs(channel - i) +len(channelList) )
    check = True 

print(minVal)