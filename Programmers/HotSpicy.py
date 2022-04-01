## 더 맵게
import heapq

def solution(scoville, K):
    answer = 0

    foods = [] # 맵기 정도를 저장할 힙

    for i in scoville:
        heapq.heappush(foods, i)
    
    noFind = True # 맵기가 원하는 만큼에 도달하지 않았음을 나타내는 변수

    if foods[0] >= K: # 처음부터 맵기가 정해진만큼에 만족되는 경우를 판별하기 위해 작성
        noFind = False

    while len(foods) >= 2 and noFind:
        firstFood = heapq.heappop(foods)
        secondFood = heapq.heappop(foods)
        
        sumFood = firstFood + secondFood*2 # 섞는 음식 맵기 계산
        answer += 1
        heapq.heappush(foods,sumFood)

        if foods[0] >= K: # 맵기가 원하는만큼에 도달하면 바로 동작 정지
            noFind = False
    
    if noFind: # 혹시 배열의 사이즈가 더 이상 계산을 못할 정도가 되었을 경우 혹시나 마지막으로 점검해보는 코드
        temp = heapq.heappop(foods)
        if temp < K:
            answer = - 1

    return answer


s= [1, 2, 3, 9, 10, 12]	
k = 7

print(solution(s,k))