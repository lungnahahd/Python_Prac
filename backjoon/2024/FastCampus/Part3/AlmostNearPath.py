# 거의 최단 경로(5719)
## 난이도 : 중상

import sys
import copy
from collections import deque


input = sys.stdin.readline
INT_MAX = sys.maxsize
SHORT_DIS = sys.maxsize
finish = False

def find_short(start, end, cnt, flag):
    global short_dis
    global finish

    val_table = [[INT_MAX,[]] for idx in range(cnt)]

    save = deque([(start, 0, [start])])
    val_table[start][0] = 0
    val_table[start][1] = [start]

    while save:
        now_node, now_cost, path = save.popleft()

        for next_node, next_cost in cost_map[now_node]:
            if val_table[next_node][0] > now_cost + next_cost:
                temp = copy.deepcopy(path)
                temp.append(next_node)
                val_table[next_node][0], val_table[next_node][1] = now_cost+next_cost, temp
                
                save.append((next_node, now_cost + next_cost, temp))

    if flag:
        if short_dis == val_table[end][0]:
            finish = True    
        short_dis = val_table[end][0]
        return get_rid_of(val_table[end][1])
    else:
        return val_table


def get_rid_of(target):
    for idx in range(1, len(target)):
        for tg, tg_val in cost_map[target[idx-1]]:
            if tg == target[idx]:
                cost_map[target[idx-1]].remove((tg, tg_val))
                break
    
    return cost_map

while True:
    place_cnt, road_cnt = list(map(int, input().split())) # 각 케이스의 시작
    if (place_cnt == 0 and road_cnt == 0): # 프로그램 종료
        break
    start_node, end_node = list(map(int, input().split())) # 시작, 종료 노드
    cost_map = [[] for _ in range(place_cnt)]
    for _ in range(road_cnt):
        a_node, b_node, value = list(map(int, input().split()))
        cost_map[a_node].append((b_node, value))
    
    short_dis = sys.maxsize
    
    cost_map = find_short(start_node, end_node, place_cnt, True)

    while not finish:
        cost_map = find_short(start_node, end_node, place_cnt, True)
        if short_dis == sys.maxsize:
            break

    answer = find_short(start_node, end_node, place_cnt, False)
    if answer[end_node][0] == sys.maxsize:
        print(-1)
    else:
        print(answer[end_node][0])
