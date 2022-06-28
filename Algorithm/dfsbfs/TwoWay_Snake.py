# 두 방향 탈출 가능 여부 판별하기


n,m = list(map(int,input().split()))
showMap = []

# 문자로 맵을 입력 받기
for i in range(n):
    get = input()
    getList = get.split(' ')
    showMap.append(getList)

checkMap = [[False for _ in range(m)] for _ in range(n)]

# 결과를 담는 변수
findWay = 0

def dfs(a, b ,showMap, checkMap):
    global findWay
    # map  내부에 위치한 경우만 동작 시행
    if -1<a<n and -1<b<m:
        if not checkMap[a][b] and showMap[a][b] == "1":    
            # 끝에 도달한 경우 결과 변경
            if a == n-1 and b == m -1:
                findWay = 1
            else:
                # 지나간 여부를 체크 -> 해당 문제에서는 돌아가는 경우는 없으므로 필요 없는 코드
                checkMap[a][b] = True
                # 아래와 오른쪽으로만 이동하므로 해당 경우만 처리
                dfs(a+1,b,showMap,checkMap)
                dfs(a,b+1,showMap,checkMap)

    return findWay

print(dfs(0,0,showMap,checkMap))