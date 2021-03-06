# 음료수 얼려 먹기 알고리즘
# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 제공
# 두 번째 줄에 N+1 번 째 줄까지 얼음 틀의 형태가 제공
# 구멍이 뚫려 있는 부분은 0, 그렇지 않은 부분은 1
# 출력 조건 : 한번에 만들어 지는 아이스크림의 갯수를 출력

import sys
input = sys.stdin.readline

size = input().split()
row = int(size[0])
col = int(size[1])
ice = []
# 행렬 구현
for i in range(row):
    list = input().strip()
    icelist = []
    for j in range(col):
        icelist.append(int(list[j]))
    ice.append(icelist)

# 행렬 간단 구현
# graph = []
# for i in range(row):
#   graph.append(list(map(int,input()))

# 아이스크림 갯수 확인 
def coldice(x,y):
    if x < 0 or x >= row or y < 0 or y >= col:
        return False
    else:
        if ice[x][y] == 1:
            return False
        else:
            ice[x][y] = 1
            coldice(x-1,y)
            coldice(x+1,y)
            coldice(x,y-1)
            coldice(x,y+1)
            return True

count = 0
for i in range(row):
    for j in range(col):
        if ice[i][j] == 0:
            check = coldice(i,j)
            if check == True:
                count = count + 1
print(count)