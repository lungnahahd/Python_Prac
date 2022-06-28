# 네 방향 탈출 가능 여부 판별

from collections import deque


n,m = list(map(int,input().split()))
showMap = []

# Map을 입력 받는 코드
for i in range(n):
    get = input()
    getList = getList = get.split(' ')
    showMap.append(getList)

findWay = 0
check = [[False for _ in range(m)] for _ in range(n)]

def bfs(row, col, check):
    check[row][col] = True
    findWay = 0
    if showMap[row][col] == "1":
        queue = deque([(row,col)])
        while queue:
            rNow, cNow = queue.popleft()
            #check[rNow][cNow] = True
            if rNow == n-1 and cNow == n-1:
               findWay = 1
               break 
            else:
                if 0 <= rNow-1:
                    if not check[rNow-1][cNow] and showMap[rNow-1][cNow] == "1":
                        queue.append((rNow-1,cNow))
                        check[rNow-1][cNow] = True
                if rNow +1 < n:
                    if not check[rNow+1][cNow] and showMap[rNow+1][cNow] == "1":
                        queue.append((rNow+1,cNow))
                        check[rNow+1][cNow] = True
                if 0 <= cNow -1:
                    if not check[rNow][cNow-1] and showMap[rNow][cNow-1] == "1":
                        queue.append((rNow, cNow-1))
                        check[rNow][cNow-1] = True
                if cNow+1 < m:
                    if not check[rNow][cNow+1] and showMap[rNow][cNow+1] == "1":
                        queue.append((rNow,cNow+1))
                        check[rNow][cNow+1] = True
                        
            

    
    return findWay
    
print(bfs(0,0,check))