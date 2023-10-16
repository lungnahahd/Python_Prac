# 갈 수 있는 곳
## 그리드가 주어지고 해당 그리드에서 1은 갈 수 없는 길, 0은 갈수 있는 길로 분류
## 복수개의 시작점이 주어졌을 때, 각 시작점에서 시작해서 갈 수 있는 영역의 총 합을 구하시오(중복 영역은 중복 카운팅 X)
##### BFS 를 활용해서 문제를 풀이


grid_size, start_count = input().split()
grid_size, start_count = int(grid_size), int(start_count)

visited = [[False for _ in range(grid_size)] for _ in range(grid_size)]
grid = []
node_queue = []

result = 0


row_move = [+1,-1,0,0]
col_move = [0,0,+1,-1]

for _ in range(grid_size):
    row = list(map(int, input().split()))
    grid.append(row)

def bfs(node_queue):
    global visited
    global result

    while (node_queue):
        now_node = node_queue.pop()
        row, col = now_node[0], now_node[1]
        for idx in range(4):
            row_now, col_now = row + row_move[idx], col + col_move[idx]
            if (-1<row_now<grid_size and -1<col_now<grid_size 
                and grid[row_now][col_now] == 0 and not visited[row_now][col_now]):
                visited[row_now][col_now] = True
                result += 1                
                node_queue.append([row_now,col_now])

for _ in range(start_count):
    row, col = list(map(int, input().split()))
    node_queue.append([row-1, col-1])
    if (not visited[row-1][col-1]):
        result += 1
        visited[row-1][col-1] = True
    bfs(node_queue)

print(result)
