# 거의 최단 경로(5719)
## 난이도 : 중상

import sys
import copy
from collections import deque


input = sys.stdin.readline
INT_MAX = sys.maxsize

def find_short(start, cnt):
    val_table = [[INT_MAX,[]] for idx in range(cnt)]

    save = deque([(start, 0)])
    val_table[start][0] = 0
    val_table[start][1] = [start]
    #val_table[start] = (0, [start])

    while save:
        now_node, now_cost = save.popleft()

        for next_node, next_cost in cost_map[now_node]:
            if val_table[next_node][0] > now_cost + next_cost:
                temp = copy.deepcopy(val_table[next_node][1])
                temp.append(next_node)
                val_table[next_node][0], val_table[next_node][1] = now_cost+next_cost, temp
                
                save.append((next_node, now_cost + next_cost))
    
    return val_table




while True:
    place_cnt, road_cnt = list(map(int, input().split())) # 각 케이스의 시작
    if (place_cnt == 0 and road_cnt == 0): # 프로그램 종료
        break
    start_node, end_node = list(map(int, input().split())) # 시작, 종료 노드
    cost_map = [[] for _ in range(place_cnt)]
    for _ in range(road_cnt):
        a_node, b_node, value = list(map(int, input().split()))
        cost_map[a_node].append((b_node, value))
    
    test = find_short(start_node, place_cnt)
    print(test)

