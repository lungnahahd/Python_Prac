import sys
INT_MAX = sys.maxsize

n = int(input())

grid = []
node_queue = []
result = [[INT_MAX for _ in range(n)] for _ in range(n)]

for _ in range(n):
    data = list(map(int, input().split()))
    grid.append(data)

row_move = [+1, 0]
col_move = [0, -1]

def bfs():
    global node_queue
    global grid

    while (node_queue):
        start = node_queue.pop()
        row_start, col_start = start[0], start[1]
        for idx in range(2):
            row_next, col_next = row_start + row_move[idx], col_start + col_move[idx]
            if (-1<row_next<n and -1<col_next<n):
                node_queue.append([row_next, col_next])
                result[row_next][col_next] = min(result[row_next][col_next], result[row_start][col_start] + grid[row_next][col_next]) 

result[0][n-1] = grid[0][n-1]
node_queue.append([0,n-1])
bfs()

print(result[n-1][0])
