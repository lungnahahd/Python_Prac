import heapq

def solution(food_times, k):
    answer = 0
    food = []
    for idx,time in enumerate(food_times):
        heapq.heappush(food,(time,idx+1))
    
    spend = 0
    f_num = len(food_times)
    while (food[0][0] - spend) * f_num <= k:
        k = k - (food[0][0] - spend) * f_num
        f_num -= 1
        spend = food[0][0]
        heapq.heappop(food)
        if k <= 0 :
            break
    if f_num == 0:
        answer = -1
    else:
        remain = []
        while food:
            _,name = heapq.heappop(food)
            remain.append(name)
        remain.sort()
        now_food = (k % f_num)
        answer = remain[now_food]