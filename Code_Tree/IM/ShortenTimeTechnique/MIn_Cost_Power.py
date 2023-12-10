# 최소 에너지 비용

place_cnt = int(input())
move_power = list(map(int, input().split()))
charge_power = list(map(int, input().split()))

min_charge_power = [charge_power[0] for _ in range(len(charge_power))]

# 각 노드를 이동할 때마다 최소 비용 에너지를 갱신
for idx in range(1, len(charge_power)):
    now_min = min(min_charge_power[idx-1], charge_power[idx])
    min_charge_power[idx] = now_min

answer = 0

# 최소 비용 에너지를 활용해서 각 경우의 비용을 구하기
for idx in range(len(move_power)):
    cost = move_power[idx] * min_charge_power[idx]
    answer += cost

print(answer)
