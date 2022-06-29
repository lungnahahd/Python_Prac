# 네 방향 탈출 가능 여부 판별

from collections import deque # bfs는 Queue를 사용해야 시간 초과 발생을 막을 수 있음

n,m = list(map(int,input().split()))
showMap = []

# Map을 입력 받는 코드
for i in range(n):
    get = input()
    getList = getList = get.split(' ')
    showMap.append(getList)

# 방문 여부를 기록할 배열
checkVisit = [[False for _ in range(m)] for _ in range(n)]

# 방문 위치를 간편하게 처리하기 위해 변수 세팅
rWay = [1,-1,0,0]
cWay = [0,0,1,-1]

def bfs(x,y,checkVisit):
    findWay = 0 # 결과를 기록할 변수
    save = deque([(x,y)])
    checkVisit[x][y] = True
    while save: # queue에 남아있는게 없는 경우는 더 이상 갈 수 없는 것이므로 동작 종료
        xTemp, yTemp = save.popleft()
        for i in range(4):
            xNow, yNow = xTemp + rWay[i], yTemp + cWay[i]
            # 조건을 통해 먼저 map에서 벗어나는지 확인하고, 방문 여부와 길이 존재하는지 여부를 확인 
            if 0 <= xNow < n and 0 <= yNow < m and not checkVisit[xNow][yNow] and showMap[xNow][yNow] == "1":
                save.append((xNow,yNow))
                checkVisit[xNow][yNow] = True
                if xNow == n-1 and yNow == m-1:
                    findWay = 1
                    break

    return findWay

print(bfs(0,0,checkVisit))