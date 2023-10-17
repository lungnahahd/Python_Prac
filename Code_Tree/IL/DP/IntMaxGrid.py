# 정수 사각형 최소 합
## (0,n)에서 시작해서 (n,0)까지 이동하는데, 최종 도착시 최소 합 구하기
##### 처음에는 BFS로 접근해서 풀이하니 시간 초과 발생
##### 이후에는 그냥 단순 점화식으로 문제를 해결 --- > 해결 완료

import sys
INT_MAX = sys.maxsize

n = int(input())

grid = []
node_queue = []
result = [[INT_MAX for _ in range(n)] for _ in range(n)]

for _ in range(n):
    data = list(map(int, input().split()))
    grid.append(data)

####################### 점화식으로 처리 #################################
result[0][n-1] = grid[0][n-1]

for idx in range(n-2,-1,-1):

    result[0][idx] = result[0][idx+1] + grid[0][idx]

for idx in range(1,n):
    result[idx][n-1] = result[idx-1][n-1] + grid[idx][n-1]

for idx in range(n-2, -1, -1):
    for col in range(idx,-1, -1):
        result[n-idx-1][col] = grid[n-idx-1][col] + min(result[n-idx-2][col], result[n-idx-1][col+1])
    
    for row in range(n-1-idx,n):
        result[row][idx] = grid[row][idx] + min(result[row-1][idx], result[row][idx+1])





####################### BFS 로 처리 #################################
# row_move = [+1, 0]
# col_move = [0, -1]

# def bfs():
#     global node_queue
#     global grid

#     while (node_queue):
#         start = node_queue.pop()
#         row_start, col_start = start[0], start[1]
#         for idx in range(2):
#             row_next, col_next = row_start + row_move[idx], col_start + col_move[idx]
#             if (-1<row_next<n and -1<col_next<n):
#                 node_queue.append([row_next, col_next])
#                 result[row_next][col_next] = min(result[row_next][col_next], result[row_start][col_start] + grid[row_next][col_next]) 

# result[0][n-1] = grid[0][n-1]
# node_queue.append([0,n-1])
# bfs()

print(result[n-1][0])
