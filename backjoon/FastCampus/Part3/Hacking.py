# 해킹 (10282)
## 난이도 : 중

import sys
from collections import deque

input = sys.stdin.readline
INT_MAX = sys.maxsize

case = int(input())

def bfs(start, computer):
    #visited = [False for _ in range(len(computer))]
    time_table = [INT_MAX for _ in range(len(computer))]
    go = deque([(start, 0)])
    time_table[start] = 0
    #visited[start] = True
    
    while go:
        now_com, now_time = go.popleft()
        for next_com, next_time in computer[now_com]:
            #if not visited[next_com]:
                #visited[next_com] = True
            ## 해당 문제에서는 시간을 재갱신이 필요한 경우가 있기에 visited를 사용 안함
            time = time_table[next_com]
            if (time > now_time + next_time): # 대신, 시간을 활용해서 시간이 작은 경우만 실행 
                time = now_time + next_time
                time_table[next_com] = time
                go.append((next_com, time))
    return time_table

answer = []

for _ in range(case):
    cnt_com, cnt_connect, start_com = list(map(int, input().split()))
    computer = [[] for _ in range(cnt_com+1)]
    for _ in range(cnt_connect):
        a_com, b_com, disease_time = list(map(int, input().split()))
        computer[b_com].append((a_com, disease_time))
    result = bfs(start_com, computer)
    
    disease_com = 0
    rst_time = 0
    for time_val in result:
        if time_val != INT_MAX:
            disease_com += 1
            rst_time = max(rst_time, time_val)
    answer.append((disease_com, rst_time))

# 결과 출력
for answer_cnt, answer_time in answer:
    print(str(answer_cnt) + ' ' + str(answer_time))
