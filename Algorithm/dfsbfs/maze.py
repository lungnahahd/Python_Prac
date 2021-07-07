# 미로 탈출 알고리즘
# 첫째 줄에 두 정수(행,렬)이 주어지고 각각의 수들은 공백 없이 붙어서 입력으로 제시되며 시작 칸과 마지막 칸은 항상 1
# 최소 이동 칸의 갯수를 출력(미로는 반드시 탈출 가능한 형태)
# 최단 거리를 구하는 것이므로 BFS를 이용함을 인지하고 구현 시작

from collections import deque
import sys
input = sys.stdin.readline


size = input().split()
row = int(size[0])
col = int(size[1])

rowy = [-1,1,0,0]
colx = [0,0,-1,1]
# 행렬 간단 구현
maze = []
for i in range(row):
    list = input().strip()
    icelist = []
    for j in range(col):
        icelist.append(int(list[j]))
    maze.append(icelist)



def bfs(x,y):
    queue = deque()
    queue.append((y,x))
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            if y + rowy[i] < 0 or y + rowy[i] >= row or x + colx[i] < 0 or x + colx[i] >= col:
                continue
            if maze[y+rowy[i]][x+colx[i]] == 1:
               queue.append((y+rowy[i],x+colx[i]))
               maze[y+rowy[i]][x+colx[i]] = maze[y][x] + 1
    
    print(maze[row-1][col-1])

bfs(0,0)