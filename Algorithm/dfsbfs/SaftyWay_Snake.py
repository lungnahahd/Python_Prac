# 두 방향 탈출 가능 여부 판별하기


n,m = list(map(int,input().split()))
showMap = []

# 문자로 맵을 입력 받기
for i in range(n):
    get = input()
    getList = get.split(' ')
    showMap.append(getList)

checkMap = [[False for _ in range(m)] for _ in range(n)]
#checkMap[0][0] = True  

findWay = 0

def dfs(a, b ,showMap, checkMap):
    global findWay
    if -1<a<n and -1<b<n:
        if not checkMap[a][b] and showMap[a][b] == "1":
            if a == n-1 and b == m -1:
                findWay = 1
            else:
                checkMap[a][b] = True
                dfs(a-1,b, showMap,checkMap)
                dfs(a+1,b,showMap,checkMap)
                dfs(a,b+1,showMap,checkMap)
                dfs(a,b-1,showMap,checkMap)

    return findWay

print(dfs(0,0,showMap,checkMap))