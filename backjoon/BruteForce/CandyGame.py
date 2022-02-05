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

# 중복된 부분을 카운트 해주는 함수 -> 해당 동작을 반복 수행해야 될 것 같기에 함수로 구현
def countCandy(sample):
    global boardSize
    temp = 1
    multiCandy = 1
    for i in range(boardSize-1):
        if sample[i] == sample[i+1]:
            temp +=1
            multiCandy = max(multiCandy,temp)
        else:
            temp = 1
    return multiCandy

eatting = 0

colMax = 1
rowMax = 1
# 초기 보드에서 먹을 수 있는 사탕의 개수 세기

for i in range(boardSize):
    colMax = max(colMax,countCandy(col[i]))
    rowMax = max(rowMax,countCandy(row[i]))


# for i in range(boardSize):
#     colMax = max(colMax,col[i].count("P"),col[i].count("Y"),col[i].count("Z"),col[i].count("C"))
#     rowMax = max(rowMax,row[i].count("P"),row[i].count("Y"),row[i].count("Z"),row[i].count("C"))
eatting = max(rowMax,colMax)

# 한 칸씩 변경하면서 경우의 수를 따져주기
if eatting != boardSize:
    colMax = 0
    rowMax = 0
    for i in range(boardSize):
        for j in range(boardSize-1):
            rowtempBefore = row[j].copy()
            rowtempAfter = row[j+1].copy()
            coltemp = col[i].copy()

            if col[i][j] != col[i][j+1]:
                coltemp[j],coltemp[j+1] = coltemp[j+1],coltemp[j]
                rowtempBefore[i],rowtempAfter[i] = rowtempAfter[i],rowtempBefore[i]
                colMax = max(colMax, countCandy(coltemp))
                rowMax = max(rowMax, countCandy(rowtempAfter),countCandy(rowtempBefore))

                # colMax = max(colMax,col[i].count("P"),col[i].count("Y"),col[i].count("Z"),col[i].count("C"))
                # rowMax = max(rowMax,row[j].count("P"),row[j].count("Y"),row[j].count("Z"),row[j].count("C"),row[j+1].count("P"),row[j+1].count("Y"),row[j+1].count("Z"),row[j+1].count("C"))
    
    eatting = max(rowMax,colMax,eatting)

    if eatting != boardSize:
        colMax = 0
        rowMax = 0
        for i in range(boardSize):
            for j in range(boardSize-1):
                rowtemp = row[i].copy()
                coltempBefore = col[j].copy()
                coltempAfter = col[j+1].copy()
                if row[i][j] != row[i][j+1]:
                    rowtemp[j],rowtemp[j+1] = rowtemp[j+1],rowtemp[j]
                    coltempBefore[i],coltempAfter[i] = coltempAfter[i],coltempBefore[i]
                    rowMax = max(rowMax,countCandy(rowtemp))
                    colMax = max(colMax, countCandy(coltempBefore), countCandy(coltempAfter))

                    # rowMax = max(rowMax,row[i].count("P"),row[i].count("Y"),row[i].count("Z"),row[i].count("C"))
                    # colMax = max(colMax,col[j].count("P"),col[j].count("Y"),col[j].count("Z"),col[j].count("C"),col[j+1].count("P"),col[j+1].count("Y"),col[j+1].count("Z"),col[j+1].count("C"))
        eatting = max(rowMax,colMax,eatting)
print(eatting)

