# 스티커
## 스티커를 최대 점수를 뗄 수 있도록 하는 것
### 입력 : 첫 줄에 테스트 개수 T가 입력
### 입력 : 각 테스트 케이스 첫 줄에는 n, 다음부터는 n개의 위치 스티커 점수
### 출력 : 스티커 점수의 최댓값을 출력

import sys
from typing import Final
input = sys.stdin.readline

Size = int(input())

final = []

for a in range(Size):
    case = int(input())
    result=[]
    # sticker = [[0 for col in range(case)] for row in range(1)]
    inputSticker = []
    inputSticker.append(list(map(int,input().split())))
    inputSticker.append(list(map(int,input().split())))
    for i in range(2):
        check = 0
        up = False
        while check < case:
            if check ==0:
                result.append(inputSticker[i][0])
                if i != 0:
                    up = True
                check += 1
            else:
                if check == case-1:
                    if up:
                        result[i] += inputSticker[0][check]
                    else:
                        result[i] += inputSticker[1][check]
                    break
                if up:
                    if inputSticker[0][check] + inputSticker[1][check+1] >= inputSticker[0][check+1]:
                        result[i] += inputSticker[0][check]
                        check += 1
                        up = False
                    else:
                        result[i] += inputSticker[0][check+1]
                        check +=2
                        up = False
                else:
                    if inputSticker[1][check] + inputSticker[0][check+1] >= inputSticker[1][check+1]:
                        result[i] += inputSticker[1][check]
                        check += 1
                        up = True
                    else:
                        result[i] += inputSticker[1][check+1]
                        check += 2
                        up = True

    final.append(max(result[0],result[1]))

for i in range(Size):
    print(final[i])