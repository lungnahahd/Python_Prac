# 거리두기 확인하기
# 2021 카카오 채용연계형 인턴십
from collections import deque

xMove = [1,-1,0,0]
yMove = [0,0,1,-1]
#visited = [[False for _ in range(5)] for _ in range(5)]

def solution(places):
    answer = []
    for i in range(5):
        room = places[i]
        answer.append(bfs(room,0,0))
        # for j in range(5):
        #     sit = room[j]
        #     for k in range(5):
        #         if sit[k] == "P":
        #             midResult = bfs(room,j,k)
        #             if midResult == 0:
        #                 #$print(j,k)
        #                 break
        #     if midResult == 0:
        #         break
        #answer.append(midResult)



    return answer

def bfs(room,x,y):
    visited = [[False for _ in range(5)] for _ in range(5)]
    for i in range(5):
        sitLine = room[i]
        for j in range(5):
            if sitLine[j] == "P":
                save = deque




    save = deque([(x,y)])
    visited[x][y] = True
    while save:
        xTemp, yTemp = save.popleft()
        for idx in range(4):
            xNow, yNow = xTemp + xMove[idx], yTemp + yMove[idx]
            dist = abs(x-xNow) + abs(y-yNow)
            if 0 <= xNow < 5 and 0 <= yNow < 5 and not visited[xNow][yNow] and dist <= 2:
                visited[xNow][yNow] = True
                sitLine = room[xNow]
                if sitLine[yNow] == "P":
                        # print(xNow,yNow)
                        # print("----------------------")
                        return 0
                elif sitLine[yNow] == "O":
                    # xDouble, yDouble = xNow + xMove[idx], yNow + yMove[idx]
                    # if 0 <= xDouble < 5 and 0 <= yDouble < 5 and not visited[xDouble][yDouble]:
                    #     visited[xDouble][yDouble] = True
                    #continue
                    save.append((xNow,yNow))
    return 1





a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(a)) 
