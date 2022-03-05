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

firstCheck = abs(channel - 100)

idx = len(channelList)

secondCheck = INT_MAX
multi = 1
for i in range(idx):
    nowIdx = idx - i - 1
    check = int(channelList[nowIdx])
    count = 0
    while check in notWork:
        right = min(check + count, 9)
        left = max(check - count, 0)
        if right not in notWork or left not in notWork:
            secondCheck += count * multi
            break
        count += 1
    multi = multi * 10
    secondCheck += 1

big = 0
bigF = True
nobig = False
nosmall = False
smallF = True
small = 0
while bigF or smallF:
    right = check + count
    left = check - count
    if right not in  notWork and bigF:
        if right <= 9:
            big = right
        else:
            nobig = True
        bigF = False
    if left not in notWork and smallF:
        if left >= 0:
            small = left
        else:
            nosmall = True
        smallF = False
    count += 1



bigNum = multi * big
smallNum = multi * small
multi = multi / 10

third = INT_MAX
forth = INT_MAX

while multi >= 1:
    if not nobig:
        bigNum += multi * small
    if not nosmall:
        smallNum += multi * big
    multi = multi  / 10
if not nobig:
    third = bigNum - channel + idx
if not nosmall:
    forth = channel - smallNum + idx

print(third, forth)
print(min(firstCheck, secondCheck, third, forth))