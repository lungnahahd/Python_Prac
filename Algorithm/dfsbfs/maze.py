# 미로 탈출 알고리즘
# 첫째 줄에 두 정수(행,렬)이 주어지고 각각의 수들은 공백 없이 붙어서 입력으로 제시되며 시작 칸과 마지막 칸은 항상 1
# 최소 이동 칸의 갯수를 출력(미로는 반드시 탈출 가능한 형태)
# 최단 거리를 구하는 것이므로 BFS를 이용함을 인지하고 구현 시작

from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph,start, visited):
    queue = deque([start])

size = input().split()
row = int(size[0])
col = int(size[1])
count = 1
x = 0
y = 0
saverow = []
savecol = []

# 행렬 간단 구현
maze = []
for i in range(row):
    maze.append(list(map(int,input())))

while x != col-1 and y != row -1:
    count = count + 1
    if x-1 >= 0 :
        if maze[x-1][y] == 1:
            maze[x-1][y] = count
    if x + 1 < col:
        if maze[x+1][y] == 1:
            maze[x+1][y] = count




while x != col-1 and y != row-1:
    if maze[x][y+1] == 1:
        y = y + 1
        count = count + 1
        saverow.append(x)
        savecol.append(y)
    elif maze[]