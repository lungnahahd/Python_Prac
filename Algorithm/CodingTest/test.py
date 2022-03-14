
import heapq
fixCost = []

def solution(money,costs):
    global fixCost
    answer = 0
    heapq.heappush(fixCost,(costs[0],1))
    heapq.heappush(fixCost,(costs[1] / 5, 5))
    heapq.heappush(fixCost,(costs[2] / 10, 10))
    heapq.heappush(fixCost,(costs[3] / 50, 50))
    heapq.heappush(fixCost,(costs[4] / 100, 100))
    heapq.heappush(fixCost,(costs[5] / 500, 500))

    while money != 0:
        cheap, unit = heapq.heappop(fixCost)
        howMuch = money // unit
        answer += howMuch * unit * cheap
        money -= howMuch * unit
    return int(answer)

costs = [1, 4, 99, 35, 50 ,1000]
costs2 = [2,11,20,100,200,600]
print(solution(1999,costs2))