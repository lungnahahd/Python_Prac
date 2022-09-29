# 주식 가격
import heapq

def solution(prices):
    answer = [0] * len(prices)
    lower_price = []
    for idx, price in enumerate(prices):
        heapq.heappush(lower_price,(price,idx))
    mid_idx = -1
    while lower_price:
        _,temp_idx = heapq.heappop(lower_price)
        if mid_idx < temp_idx:
            answer[temp_idx] = (len(prices)-1) - temp_idx
            mid_idx = temp_idx
        else:
            answer[temp_idx] = mid_idx - temp_idx
        

    return answer


print(solution([1,2,3,2,3]))