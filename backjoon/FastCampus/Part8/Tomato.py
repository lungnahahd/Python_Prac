# 토마토 (7576)
## 난이도 : 골드 5

import sys
import heapq
from collections import deque 
input = sys.stdin.readline 

box = []
col, row = list(map(int, input().split()))
tomato_cnt = col * row
move_r = [-1,0,+1,0]
move_c = [0,+1,0,-1]
visited = [[False for _ in range(col)] for _ in range(row)] # 방문 여부를 나타낼 배열
tomato_loaction = []
#tomato_location = deque([])

# 토마토를 박스에 담아서 세팅
for r_idx in range(row):
    temp = list(map(int, input().split()))
    box.append(temp)
    for c_idx in range(col):
        if temp[c_idx] == 1:
            heapq.heappush(tomato_loaction, (0, r_idx, c_idx))
            visited[r_idx][c_idx] = True
            tomato_cnt -= 1
        elif temp[c_idx] == -1:
            tomato_cnt -= 1

end_time = 0
def ripe_fruit(information):
    global end_time, box, visited, tomato_cnt
    #r_now, c_now, time_now = information.popleft()
    while information:
        time_now, r_now, c_now = heapq.heappop(information)
        for move in range(4):
            r_next, c_next = r_now + move_r[move], c_now + move_c[move]
            if 0 <= r_next < row and 0 <= c_next < col and not visited[r_next][c_next]:
                visited[r_next][c_next] = True
                if box[r_next][c_next] == 0:
                    tomato_cnt -= 1
                    box[r_next][c_next] = 1
                    end_time = max(end_time, time_now+1)
                    heapq.heappush(information, (time_now+1, r_next, c_next))

ripe_fruit(tomato_loaction)
if tomato_cnt != 0:
    print(-1)
else:
    print(end_time)