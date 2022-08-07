# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    if bridge_length == 1: # 다리 길이가 1인 경우 처리하는 부분
        answer += (1+len(truck_weights))
    else:
        bfTime = 1 # 현재 얼만큼 지났는가를 나타내는 변수
        onBridge = deque([(truck_weights[0],bfTime+bridge_length)]) # queue에 트럭의 무게와 현재 트럭이 다리를 다 건널 경우의 시간을 기록
        nowTruck = truck_weights[0] # 현재 다리 위에 트럭의 무게를 나타냄
        for truck in truck_weights[1:]: # 트럭을 하나씩 지나가게 하기
            if nowTruck + truck <= weight: # 현재 다리 위에 트럭이 더 위치할 수 있는 경우
                bfTime += 1
                if onBridge[0][1] <=bfTime: # 시간이 증가했을 때, 다리 위에 트럭이 다 지나가게 되었을 수도 있기에 필요
                    outTruck = onBridge.popleft() # 다리 위를 건넌 트럭을 큐에서 빼주기
                    nowTruck -= outTruck[0]
                nowTruck += truck
                onBridge.append((truck,bfTime+bridge_length))
            else: # 현재 다리 위에 트럭이 더 이상 올라가지 못하는 경우
                while nowTruck + truck > weight: # 현재 트럭이 올라갈 수 있을 때까지 큐에서 빼주기
                    outTruck = onBridge.popleft()
                    bfTime = outTruck[1]
                    nowTruck -= outTruck[0]
                onBridge.append((truck,bfTime+bridge_length)) # 현재 트럭을 넣어주기
                nowTruck += truck
        outTruck = onBridge.pop() # 마지막에는 무조건 남은 트럭이 지나갔을 때가 정답!
        answer = outTruck[1]
    return answer


#l = 5
l = 100
#w = 5
w = 100
#t = [2,2,2,2,1,1,1,1,1]
t = [10,10,10,10,10,10,10,10,10,10]
print(solution(l,w,t))