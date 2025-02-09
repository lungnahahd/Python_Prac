# 단지 번호 붙이기
import copy

numMap = int(input())
answer = []
town = []
visited = [[False for _ in range(numMap)]for _ in range(numMap)]
moves = [[+1, 0], [0, +1], [-1, 0], [0, -1]]
# 입력을 받는 부분
for _ in range(numMap):
    temp = list(input())
    town.append(temp)

# DFS를 적용해서 방문 여부를 확인하는 함수


def dfs(r, c):
    global visited
    save = []
    town_size = 0
    save.append((r, c))
    visited[r][c] = True
    while save:
        now_r, now_c = save.pop()
        town_size += 1
        for move in moves:
            next_r, next_c = now_r + move[0], now_c + move[1]
            if 0 <= next_r < numMap and 0 <= next_c < numMap and town[next_r][next_c] == '1' and not visited[next_r][next_c]:
                save.append((next_r, next_c))
                visited[next_r][next_c] = True
    return town_size


# 실제 노드를 하나 하나 따지면서 들어가기
for row in range(numMap):
    for col in range(numMap):
        if town[row][col] == '1' and not visited[row][col]:
            now_town_size = dfs(row, col)
            answer.append(now_town_size)
answer.sort()
print(len(answer))
for n in answer:
    print(n)
