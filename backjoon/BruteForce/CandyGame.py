# 사탕 게임
## 캔디크러시 사가 같은 게임 단, 인접 사탕 위치 교환은 한 번만 가능
### 입력 : 첫 줄에 보드의 크기가 입력되고, 다음 줄부터 보드의 크기와 형태대로 색을 채워 넣기
### 출력 : 먹을 수 있는 사탕의 최대 개수를 출력

import sys
input = sys.stdin.readline

boardSize = int(input())

row = [[] for i in range(boardSize)] # 열(세로) 부분 리스트
col = [[] for i in range(boardSize)] # 행(가로) 부분 리스트

for i in range(boardSize):
    color = input()
    for j in range(boardSize):
        col[i].append(color[j])
        row[j].append(color[j])

eatting = 0

colMax = 0
rowMax = 0
# 초기 보드에서 먹을 수 있는 사탕의 개수 세기
for i in range(boardSize):
    colMax = max(colMax,col[i].count("P"),col[i].count("Y"),col[i].count("Z"),col[i].count("C"))
    rowMax = max(rowMax,row[i].count("P"),row[i].count("Y"),row[i].count("Z"),row[i].count("C"))

eatting = max(rowMax,colMax)
if eatting == boardSize:
    print(boardSize)
else:
    colMax = 0
    rowMax = 0
    for i in range(boardSize):
        for j in range(boardSize-1):
            if col[i][j] != col[i][j+1]:
                col[i][j],col[i][j+1] = col[i][j+1],col[i][j]
                row[j][i],row[j+1][i] = row[j+1][i],row[j][i]
                colMax = max(colMax,col[i].count("P"),col[i].count("Y"),col[i].count("Z"),col[i].count("C"))
                rowMax = max(rowMax,row[j].count("P"),row[j].count("Y"),row[j].count("Z"),row[j].count("C"),row[j+1].count("P"),row[j+1].count("Y"),row[j+1].count("Z"),row[j+1].count("C"))
    eatting = max(rowMax,colMax,eatting)
    if eatting == boardSize:
        print(eatting)
    else:
        colMax = 0
        rowMax = 0
        for i in range(boardSize):
            for j in range(boardSize-1):
                if row[i][j] != row[i][j+1]:
                    row[i][j],row[i][j+1] = row[i][j+1],row[i][j]
                    col[j][i],col[j+1][i] = col[j+1][i],col[j][i]
                    rowMax = max(rowMax,row[i].count("P"),row[i].count("Y"),row[i].count("Z"),row[i].count("C"))
                    colMax = max(colMax,col[j].count("P"),col[j].count("Y"),col[j].count("Z"),col[j].count("C"),col[j+1].count("P"),col[j+1].count("Y"),col[j+1].count("Z"),col[j+1].count("C"))
        eatting = max(rowMax,colMax,eatting)
        print(eatting)

