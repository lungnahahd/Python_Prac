# 트럭(13335)
## 난이도 : 중

from collections import deque

cnt_car, bridge, can_weight = list(map(int, input().split()))
trucks = list(map(int, input().split()))
answer = 0
end_truck = 0
now_weight = 0

dq_truck = deque(trucks)
dq_bridge = deque([0 for _ in range(bridge)])

while end_truck != cnt_car:
    temp = dq_bridge.popleft()
    if temp == 0:
        if len(dq_truck) != 0 and now_weight + dq_truck[0] <= can_weight:
            now_truck = dq_truck.popleft()
            dq_bridge.append(now_truck)
            now_weight += now_truck
        else:
            dq_bridge.append(0)
    else:
        end_truck += 1
        now_weight -= temp
        if len(dq_truck) != 0 and now_weight + dq_truck[0] <= can_weight:
            now_truck = dq_truck.popleft()
            dq_bridge.append(now_truck)
            now_weight += now_truck
        else:
            dq_bridge.append(0)
    answer += 1

print(answer)
