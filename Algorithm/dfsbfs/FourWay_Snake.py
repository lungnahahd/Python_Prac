# 네 방향 탈출 가능 여부 판별

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
    global findWay
    if 0 <= row < n and 0 <= col < m:
        if row == n-1 and col == m-1:
            findWay = 1
        else:
            if not check[row][col] and showMap[row][col] == "1":
                check[row][col] = True
                bfs(row+1,col,check)
                bfs(row-1,col,check)
                bfs(row,col+1,check)
                bfs(row,col-1,check)
    
    return findWay
print(bfs(0,0,check))