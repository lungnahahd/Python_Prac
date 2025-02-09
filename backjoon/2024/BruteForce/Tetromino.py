# 테트로미노
## 4개의 정사각형을 연결한 테트로미노를 놓아 최대의 합을 구하는 프로그램
### 입력 : 첫 줄에 세로의 크기와 가로의 크기가 입력 둘째 줄부터 정수판을 입력
### 출력: 테트로미노가 놓여서 얻을 수 있는 최대값을 출력


import sys
import heapq
input = sys.stdin.readline

col, row = tuple(map(int, input().split())) # 세로, 가로의 크기를 입력 받음

numMatirx = [[-1 for _ in range(row + 2)] for _ in range(col + 2)]
chekcMatrix = [[-1 for _ in range(row + 2)] for _ in range(col + 2)]


# 정수판에 해당하는 정수를 받기
# 정수판에 전체를 -1로 한번 감아주기

maxNum = -1
for i in range(1,col+1):
    get = list(map(int,input().split()))
    idx = 1
    for k in get:
        numMatirx[i][idx] = k
        maxNum = max(k, maxNum)
        chekcMatrix[i][idx] = 0
        idx += 1

result = -1

# DFS 연산을 효율적으로 처리하기 위해 사용되는 배열
cCol = [0,0,+1,-1]
cRow = [+1,-1,0,0]


# DFS 를 처리하는 함수
def valDFS(nowCol, nowRow, val,  count):
    global result
    if val + (4-count)*maxNum >= result: # 미리 사전에 처리하기 위해 거치는 조건 -> 불필요한 반복 연산 줄이기
        if count == 4: # 4개의 숫자가 차면 종료
            result = max(result, val)
        else:
            for i in range(4): # 4면을 붙이기 위해 인덱스를 처리
                tempCol = nowCol + cCol[i]
                tempRow = nowRow + cRow[i]
                if 0< tempCol < col + 1 and 0 < tempRow < row + 1: # 정수판에 범위에 들어오는 경우만 연산
                    if chekcMatrix[tempCol][tempRow] != -1:
                        chekcMatrix[tempCol][tempRow] = -1
                        valDFS(tempCol,tempRow,val + numMatirx[tempCol][tempRow],count + 1)
                        chekcMatrix[tempCol][tempRow] = 0
                    elif count == 2: # 2번째 처리를 하는 경우 ㅓ,ㅏ,ㅗ,ㅜ 방향을 더 이상 반복문을 진행하지 않고 바로 결과를 내버리기 -> 불필요한 반복 연산 줄이기
                        if nowCol == tempCol:
                            result = max(result, val + numMatirx[nowCol+1][nowRow] + numMatirx[nowCol-1][nowRow])
                        else:
                            result = max(result, val + numMatirx[nowCol][nowRow+1] + numMatirx[nowCol][nowRow-1])
                        

for i in range(1, col +1):
    for j in range(1, row + 1):
        count = 1
        chekcMatrix[i][j] = -1
        valDFS(i,j,numMatirx[i][j],count)
        chekcMatrix[i][j] = 0

print(result)















# def checkDFS(nowCol, nowRow, count, val,shapeCheck):
#     global result
#     global numMatirx
#     global chekcMatrix
#     if count == 4 and not shapeCheck:
#         result = max(result, val)
#     elif count == 5 and shapeCheck:
#         result = max(result,val)
#     #if count == 1:
#     else:
#         #count += 1
#         if count == 2 and not shapeCheck:
#             if 0 < nowCol < col+1 and 0 < nowRow + 1 < row+1 and chekcMatrix[nowCol][nowRow+1] == -1  :
#                 checkDFS(nowCol,nowRow+1,5,val+numMatirx[nowCol+1][nowRow+1]+numMatirx[nowCol-1][nowRow+1],True)
#                 chekcMatrix[nowCol][nowRow-1] = -1
#                 checkDFS(nowCol,nowRow-1,count+1,val +  numMatirx[nowCol][nowRow-1],shapeCheck)
#                 chekcMatrix[nowCol][nowRow-1] = 0
#                 chekcMatrix[nowCol+1][nowRow] = -1
#                 checkDFS(nowCol+1,nowRow,count+1,val+numMatirx[nowCol+1][nowRow],shapeCheck)
#                 chekcMatrix[nowCol+1][nowRow] = 0
#                 chekcMatrix[nowCol-1][nowRow] = -1
#                 checkDFS(nowCol-1,nowRow,count+1,val + numMatirx[nowCol-1][nowRow],shapeCheck)
#                 chekcMatrix[nowCol-1][nowRow] = 0

#             elif 0 < nowCol < col+1 and 0 < nowRow - 1 < row+1 and chekcMatrix[nowCol][nowRow-1] == -1:
#                 checkDFS(nowCol,nowRow-1,5,val+numMatirx[nowCol+1][nowRow-1]+numMatirx[nowCol-1][nowRow-1], True)
#                 chekcMatrix[nowCol][nowRow+1] = -1
#                 checkDFS(nowCol,nowRow+1,count+1,val + numMatirx[nowCol][nowRow+1],shapeCheck)
#                 chekcMatrix[nowCol][nowRow+1] = 0
#                 chekcMatrix[nowCol+1][nowRow] = -1
#                 checkDFS(nowCol+1,nowRow,count+1,val+numMatirx[nowCol+1][nowRow],shapeCheck)
#                 chekcMatrix[nowCol+1][nowRow] = 0
#                 chekcMatrix[nowCol-1][nowRow] = -1
#                 checkDFS(nowCol-1,nowRow,count+1,val + numMatirx[nowCol-1][nowRow],shapeCheck)
#                 chekcMatrix[nowCol-1][nowRow] = 0
                
#             elif 0 < nowCol+1 < col+1 and 0 < nowRow  < row+1 and chekcMatrix[nowCol+1][nowRow] == -1 :
#                 checkDFS(nowCol+1,nowRow,5,val + numMatirx[nowCol+1][nowRow+1] + numMatirx[nowCol+1][nowRow-1], True)
#                 chekcMatrix[nowCol][nowRow+1] = -1
#                 checkDFS(nowCol,nowRow+1,count+1,val + numMatirx[nowCol][nowRow+1],shapeCheck)
#                 chekcMatrix[nowCol][nowRow+1] = 0
#                 chekcMatrix[nowCol][nowRow-1] = -1
#                 checkDFS(nowCol,nowRow-1,count+1,val +  numMatirx[nowCol][nowRow-1],shapeCheck)
#                 chekcMatrix[nowCol][nowRow-1] = 0
#                 chekcMatrix[nowCol-1][nowRow] = -1
#                 checkDFS(nowCol-1,nowRow,count+1,val + numMatirx[nowCol-1][nowRow],shapeCheck)
#                 chekcMatrix[nowCol-1][nowRow] = 0

#             elif 0 < nowCol-1 < col+1 and 0 < nowRow  < row+1 and chekcMatrix[nowCol-1][nowRow] == -1:
#                 checkDFS(nowCol-1,nowRow,5,val + numMatirx[nowCol-1][nowRow+1]+ numMatirx[nowCol-1][nowRow-1], True)
#                 chekcMatrix[nowCol][nowRow+1] = -1
#                 checkDFS(nowCol,nowRow+1,count+1,val + numMatirx[nowCol][nowRow+1],shapeCheck)
#                 chekcMatrix[nowCol][nowRow+1] = 0
#                 chekcMatrix[nowCol][nowRow-1] = -1
#                 checkDFS(nowCol,nowRow-1,count+1,val +  numMatirx[nowCol][nowRow-1],shapeCheck)
#                 chekcMatrix[nowCol][nowRow-1] = 0
#                 chekcMatrix[nowCol+1][nowRow] = -1
#                 checkDFS(nowCol+1,nowRow,count+1,val+numMatirx[nowCol+1][nowRow],shapeCheck)
#                 chekcMatrix[nowCol+1][nowRow] = 0


#         else:
#             if 0 < nowCol < col+1 and 0 < nowRow + 1 < row+1 and chekcMatrix[nowCol][nowRow+1] != -1:
#                 chekcMatrix[nowCol][nowRow+1] = -1
#                 checkDFS(nowCol,nowRow+1,count+1,val + numMatirx[nowCol][nowRow+1],shapeCheck)
#                 chekcMatrix[nowCol][nowRow+1] = 0
#             if 0 < nowCol < col+1 and 0 < nowRow - 1 < row+1 and chekcMatrix[nowCol][nowRow-1] != -1:
#                 chekcMatrix[nowCol][nowRow-1] = -1
#                 checkDFS(nowCol,nowRow-1,count+1,val +  numMatirx[nowCol][nowRow-1],shapeCheck)
#                 chekcMatrix[nowCol][nowRow-1] = 0
#             if 0 < nowCol+1 < col+1 and 0 < nowRow  < row+1 and chekcMatrix[nowCol+1][nowRow] != -1:
#                 chekcMatrix[nowCol+1][nowRow] = -1
#                 checkDFS(nowCol+1,nowRow,count+1,val+numMatirx[nowCol+1][nowRow],shapeCheck)
#                 chekcMatrix[nowCol+1][nowRow] = 0
#             if 0 < nowCol-1 < col+1 and 0 < nowRow  < row+1 and chekcMatrix[nowCol-1][nowRow] != -1:
#                 chekcMatrix[nowCol-1][nowRow] = -1
#                 checkDFS(nowCol-1,nowRow,count+1,val + numMatirx[nowCol-1][nowRow],shapeCheck)
#                 chekcMatrix[nowCol-1][nowRow] = 0


# for i in range(1,col+1):
#     for j in range(1,row+1):
#         count = 1
#         chekcMatrix[i][j] = -1
#         shapeCheck = False
#         checkDFS(i,j, count,numMatirx[i][j],shapeCheck)
#         chekcMatrix[i][j] = 0

# print(result)




# checkSet = set() # 현재 위치에서 무엇을 거쳤는지 체크하는 set
# result = 0
# for i in range(1,col+1):
#     for j in range(1,row+1):
#         checkSet = set() # 현재 위치에서 무엇을 거쳤는지 체크하는 set
#         tempSum = numMatirx[i][j]
#         tempQueue = []
#         count = 1
#         nowI = i
#         nowJ = j
#         checkSet.add((nowI,nowJ))
#         while count < 4:  # 4개의 칸을 지정시키면 종료   
#             heapq.heappush(tempQueue,(-numMatirx[nowI][nowJ-1],nowI,nowJ-1))
#             heapq.heappush(tempQueue,(-numMatirx[nowI][nowJ+1],nowI,nowJ+1))
#             heapq.heappush(tempQueue,(-numMatirx[nowI-1][nowJ],nowI-1,nowJ))
#             heapq.heappush(tempQueue,(-numMatirx[nowI+1][nowJ],nowI+1,nowJ))
#             val,x,y = heapq.heappop(tempQueue)
#             while (x,y) in checkSet:
#                 val,x,y = heapq.heappop(tempQueue)
#             tempSum += -val
#             nowI = x
#             nowJ = y
#             checkSet.add((x,y))
#             count += 1
#         result = max(result,tempSum)
# print(result)

# 4 4
# 5 1 1 5
# 2 1 1 2
# 2 1 1 2 
# 1 1 1 1
# 10