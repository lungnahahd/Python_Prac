from collections import deque

move_r = [1,0,-1,0]
move_c = [0,1,0,-1]
area = [[0 for _ in range(51)] for _ in range(51)]

def check_stance(find_r, find_c, find_r2,find_c2, rec):
    for now_rec in rec:
        here = 0
        small_c, small_r, big_c, big_r = now_rec
        for r in range(small_r, big_r+1):
            for c in range(small_c, big_c+1):
                if (r == find_r and c == find_c) or (r == find_r2 and c == find_c2):
                    here += 1
                    if here == 2:
                        return True
    return False

def make_maze(rec):
    global area
    maze = [[0 for _ in range(51)] for _ in range(51)]
    for now_rec in rec:
        small_c, small_r, big_c, big_r  = now_rec
        for r in range(small_r, big_r+1):
            maze[r][small_c] += 1
            maze[r][big_c] += 1
        for c in range(small_c+1, big_c):
            maze[small_r][c] +=1
            maze[big_r][c] += 1
    for now_rec in rec:
        small_c, small_r, big_c, big_r = now_rec
        for r in range(small_r+1, big_r):
            for c in range(small_c+1, big_c):
                if maze[r][c] != 0:
                    maze[r][c] = 0
    return maze

def bfs(start_r, start_c, end_r, end_c, maze, rec):
    visited = [[False for _ in range(51)] for _ in range(51)]
    visited[start_r][start_c] = True
    temp = deque([(start_r, start_c, 1)])
    cnt = 0
    while temp:
        now_r, now_c, now_cnt = temp.popleft()
        now_val = maze[now_r][now_c]
        for m_idx in range(4):
            next_r, next_c = now_r + move_r[m_idx], now_c + move_c[m_idx]
            if 0 <= next_r < 51 and 0 <= next_c < 51 and not visited[next_r][next_c]:
                
                if maze[next_r][next_c] != 0 and check_stance(now_r, now_c, next_r, next_c, rec):
                    if next_r == end_r and next_c == end_c :
                        return now_cnt
                    visited[next_r][next_c] = True
                    temp.append((next_r, next_c, now_cnt+1))
                
    return cnt

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maze = make_maze(rectangle)
    answer = bfs(characterY, characterX, itemY, itemX, maze, rectangle)
    
    
    return answer