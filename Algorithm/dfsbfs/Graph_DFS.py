# 그래프 탐색

# 그래프에 대한 정보를 받는 부분
node, line = list(map(int,input().split()))
nodeList= [[] for _ in range(node+1)]
nodeCheck = [ False for _ in range(node+1)]
nodeCheck[1] = True # 1에서 항상 시작하므로 1은 지났다고 처리


# 재귀함수를 통해 DFS를 구현한 코드
def dfs(start, nList, nCheck):
    global count # 전역변수로 count 처리
    for i in nList[start]:
        if not nCheck[i]:
            count += 1
            nCheck[i] = True 
            dfs(i, nList, nCheck)
    return count



for i in range(line):
    start, end = list(map(int,input().split()))
    nodeList[start].append(end)
    nodeList[end].append(start) # 양방향이므로 뒤집어서 처리 필요

count = 0
print(dfs(1,nodeList,nodeCheck))