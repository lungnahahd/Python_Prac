# 무지의 먹방 라이브
### 그리디 알고리즘...

import heapq

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        answer = - 1
    else:
        food = []
        for idx,time in enumerate(food_times):
            heapq.heappush(food,(time,idx+1))

        spend = 0
        f_num = len(food_times)
        last_food = 0
        while (food[0][0] - spend) * f_num <= k:
            k = k - (food[0][0] - spend) * f_num
            f_num -= 1
            spend = food[0][0]
            last_food,_ = heapq.heappop(food)

            if k <= 0 :
                break
        remain = []
        while food:
            _,name = heapq.heappop(food)
            remain.append(name)

        remain.sort()
        now_food = (k % f_num)
        answer = remain[now_food]

    
    return answer