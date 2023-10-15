# 뿌요뿌요
## 상하좌우로 연결된 숫자가 동일하면 카운트
## 카운트가 4이상이면 해당 영역은 파괴
### 파괴된 영역의 개수와 가장 넓은 영역의 크기를 출력
##### dfs를 이용해서 해당 문제를 해결


areaSize = int(input())
area = []
visited = [[False for _ in range(areaSize)] for _ in range(areaSize)]
blockSize, resultCount, resultBlock = 1, 0, 0

for _ in range(areaSize):
    areaRow = list(map(int, input().split()))
    area.append(areaRow)

ax = [-1, 0, +1, 0]
ay = [0, +1, 0, -1]

def dfs(x,y,nowNum):
    global blockSize
    for idx in range(4):
        x_now, y_now = x + ax[idx], y + ay[idx]
        if(-1 < x_now < areaSize and -1 < y_now < areaSize and not visited[x_now][y_now]):
            if (area[x_now][y_now] == nowNum):
                visited[x_now][y_now] = True
                blockSize += 1
                dfs(x_now,y_now,nowNum)


for y in range(areaSize):
    for x in range(areaSize):
        if (not visited[x][y]):
            visited[x][y] = True
            dfs(x,y,area[x][y])
            if (blockSize >= 4):
                resultCount += 1 
            resultBlock = max(resultBlock, blockSize)
            blockSize = 1

print(resultCount, resultBlock)

  
