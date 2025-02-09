# 정육점 (2258)
## 난이도 : 골드 4

import sys
import heapq
input = sys.stdin.readline 

house_cnt, want_weight = list(map(int, input().split()))

house = []
stack_house = []
before_cost = 0
before_weight = 0
stack_weight = 0
for _ in range(house_cnt):
    weight, cost = list(map(int, input().split()))
    heapq.heappush(house, (cost, weight))

temp = 0
while house:
    now_cost, now_weight = heapq.heappop(house)
    if now_cost == before_cost:
        if temp == 0:
            temp = stack_weight - before_weight
        else:
            temp -= before_weight
        temp += now_weight
        heapq.heappush(stack_house, (now_cost, temp))
        stack_weight += now_weight
    else:
        temp = 0
        stack_weight += now_weight
        heapq.heappush(stack_house, (now_cost, stack_weight))
    before_cost = now_cost
    before_weight = now_weight

#print(stack_house)
#answer = 2147483648
answer = sys.maxsize
before_weight, before_cost, stack_before_cost, stack_before_weight = 0, 0, 0, 0
while stack_house:
    now_cost, now_weight = heapq.heappop(stack_house)
    if now_weight >= 2147483648:
        continue
    if now_weight >= want_weight:
        answer = min(now_cost, answer)
    if now_cost == before_cost:
        if stack_before_cost == 0:
            stack_before_cost = before_cost + now_cost
            stack_before_weight = before_weight + now_weight
        else:
            stack_before_weight += now_weight
            stack_before_cost += now_cost
        if now_weight >= 2147483648:
            continue 
        if stack_before_weight >= want_weight:
            answer = min(answer, stack_before_cost)
    else:
        stack_before_cost, stack_weight = 0, 0
    before_weight, before_cost = now_weight, now_cost


if answer == sys.maxsize:
    print(-1)
else:
    print(answer)