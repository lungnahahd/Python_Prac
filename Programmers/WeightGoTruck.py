# 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    if bridge_length == 1:
        answer += (1+len(truck_weights))
    else:
        bfTime = 1
        nowTruck = truck_weights[0]
        for truck in truck_weights[1:]:
            if nowTruck + truck <= weight:
                bfTime += 1
            else:
                bfTime += bridge_length
            nowTruck = truck
        bfTime += bridge_length
        answer = bfTime



    return answer


#l = 2
l = 100
#w = 10
w = 100
#t = [7,4,5,6]
t = [10,10,10,10,10,10,10,10,10,10]
print(solution(l,w,t))