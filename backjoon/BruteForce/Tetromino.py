# 테트로미노
## 4개의 정사각형을 연결한 테트로미노를 놓아 최대의 합을 구하는 프로그램
### 입력 : 첫 줄에 세로의 크기와 가로의 크기가 입력 둘째 줄부터 정수판을 입력
### 출력: 테트로미노가 놓여서 얻을 수 있는 최대값을 출력

from cgitb import reset
import sys
import heapq
input = sys.stdin.readline

col, row = tuple(map(int, input().split())) # 세로, 가로의 크기를 입력 받음

numMatirx = [[-1 for _ in range(row + 2)] for _ in range(col + 2)]
chekcMatrix = [[-1 for _ in range(row + 2)] for _ in range(col + 2)]


# 정수판에 해당하는 정수를 받기
# 정수판에 전체를 -1로 한번 감아주기
for i in range(1,col+1):
    get = list(map(int,input().split()))
    idx = 1
    for k in get:
        numMatirx[i][idx] = k
        chekcMatrix[i][idx] = 0
        idx += 1

result = 0

# checkSet = set()

def checkDFS(nowCol, nowRow, count, val):
    global result
    global numMatirx
    global chekcMatrix
    if count == 4:
        result = max(result, val)
    #if count == 1:
    else:
        count += 1
        if chekcMatrix[nowCol][nowRow+1] != -1:
            # val += numMatirx[nowCol][nowRow+1]
            chekcMatrix[nowCol][nowRow+1] = -1
            checkDFS(nowCol,nowRow+1,count,val + numMatirx[nowCol][nowRow+1])
            chekcMatrix[nowCol][nowRow+1] = 0
        if chekcMatrix[nowCol][nowRow-1] != -1 :
            # val += numMatirx[nowCol][nowRow-1]
            chekcMatrix[nowCol][nowRow-1] = -1
            checkDFS(nowCol,nowRow-1,count,val +  numMatirx[nowCol][nowRow-1])
            chekcMatrix[nowCol][nowRow-1] = 0
        if chekcMatrix[nowCol+1][nowRow] != -1 :
            #val += numMatirx[nowCol+1][nowRow]
            chekcMatrix[nowCol+1][nowRow] = -1

            checkDFS(nowCol+1,nowRow,count,val+numMatirx[nowCol+1][nowRow])
            chekcMatrix[nowCol+1][nowRow] = 0
        if chekcMatrix[nowCol-1][nowRow] != -1:
            #val += numMatirx[nowCol-1][nowRow]
            chekcMatrix[nowCol-1][nowRow] = -1
            checkDFS(nowCol-1,nowRow,count,val + numMatirx[nowCol-1][nowRow])
            chekcMatrix[nowCol-1][nowRow] = 0


for i in range(1,col+1):
    for j in range(1,row+1):
        count = 1
        checkDFS(i,j, count,numMatirx[i][j])
        chekcMatrix[i][j] = 0

print(result)




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