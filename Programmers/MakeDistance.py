# 거리두기 확인하기
# 2021 카카오 채용연계형 인턴십
from collections import deque

xMove = [1, -1, 0, 0]
yMove = [0, 0, 1, -1]

def solution(places):
    answer = []
    midResult = False
    for room in places:
        visited = [[False for _ in range(5)] for _ in range(5)]
        count = -1
        for sitLine in room:
            count += 1
            for i in range(5):
                
                if sitLine[i] == "P":
                    midResult = bfs(room,count,i,visited)
                    if midResult:
                        break
            if midResult:
                print(count,i)
                answer.append(0)
                break
        if not midResult:
            answer.append(1)
    return answer

def bfs(graph, x, y, visited):
    save = deque([(x,y)])
    visited[x][y] = True
    canGo = [True,True,True,True] # 중간에 가림막이 있으면 그쪽으로 못가게 하기
    result = False # 결과를 출력할 변수
    while save:
        xTemp, yTemp = save.popleft()
        if xTemp < x-3 or x+3 < xTemp or yTemp < y-3 or y+3 < yTemp: # 해당 위치를 벗어나면 맨허튼 거리가 넘으므로 할 필요가 없으므로 중지
            break
        for i in range(4):
            #if canGo[i] == False: # 해당 방향으로 못가면 다음 반복문 시행
            #    continue
            xNow, yNow = xTemp + xMove[i], yTemp + yMove[i]
            if 0 <= xNow <5 and 0 <= yNow < 5 and not visited[xNow][yNow]: 
                temp = graph[xNow]
                if temp[yNow] == "P": # 위치에 사람이 있는 경우 stop
                    if abs(x-xNow) + abs(y-yNow) <= 2:
                        result = True
                        return result
                elif temp[yNow] == "O": # 빈자리일 경우는 위치로 이동
                    save.append((xNow,yNow))
                else:
                    xDouble, yDouble = xNow + xMove[i], yNow + yMove[i]
                    if 0 <= xDouble < 5 and 0 <= yDouble < 5 and not visited[xDouble][yDouble]:
                        visited[xDouble][yDouble] = True
                visited[xNow][yNow] = True
    return result


a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(a)) 
