# 거리두기 확인하기
# 2021 카카오 채용연계형 인턴십
from collections import deque

def bfs(room):
    xMove = [1,-1,0,0]
    yMove = [0,0,1,-1]
    person = []
    for x in range(5):
        for y in range(5):
            if room[x][y] == "P":
                person.append((x,y))
    for s in person:
        visited = [[False for _ in range(5)] for _ in range(5)]
        save = deque([(s[0],s[1],0)])
        visited[s[0]][s[1]] = True
        while save:
            xTemp, yTemp, distTemp = save.popleft()
            for idx in range(4):
                xNow, yNow, disNow = xMove[idx] + xTemp , yMove[idx] + yTemp , distTemp + 1
                if disNow > 2:
                    continue
                else:
                    if 0<= xNow < 5 and 0 <= yNow < 5 and not visited[xNow][yNow]:
                        if room[xNow][yNow] == "P":
                            return 0
                        elif room[xNow][yNow] == "O":
                            visited[xNow][yNow] = True
                            save.append((xNow,yNow,disNow))

    return 1        


def solution(places):
    answer = []
    for room in places:
        answer.append(bfs(room))

    return answer





a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(a)) 
