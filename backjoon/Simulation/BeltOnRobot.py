# 컨베이어 벨트 위의 로봇
#####################
# 1이 위에 올리기, n이 내리기
# 벨트는 로봇과 함께 한 칸씩 이동 -> 단 내구도가 1 이상 남았이어야 함
# 로봇 이동은 이동하려는 칸이 비어 있고, 그 칸의 내구도가 1 이상인 경우만 가능
# 내구도가 0인 칸의 개수가 k 이면 과정 종료, 그렇지 않으면 벨트가 한 칸 회전
# 몇 번째 단계가 진행 중일 때 종료되었는지 출력
from collections import deque

n, k = map(int, input().split())
temp = list(map(int, input().split()))
belt_strong = deque(temp)

not_work_container_num = 0
robots_location = deque()
answer = 1
while not_work_container_num < k:
    for idx in range(len(robots_location)):
        robots_location[idx] += 1
    before = belt_strong[-1]
    for idx in range(len(belt_strong)):
        belt_strong[idx], before = before, belt_strong[idx]
    if n-1 in robots_location:
        robots_location.remove(n-1)
    for idx in range(len(robots_location)):
        temp_robot_location = robots_location[idx] + 1
        if temp_robot_location not in robots_location:
            if belt_strong[temp_robot_location] != 0:
                robots_location[idx] = temp_robot_location
                belt_strong[temp_robot_location] -= 1
    if n-1 in robots_location:
        robots_location.remove(n-1)
    if belt_strong[0] != 0 and 0 not in robots_location:
        robots_location.append(0)
        belt_strong[0] -= 1
    not_work_container_num = belt_strong.count(0)
    if not_work_container_num < k:
        answer += 1
print(answer)
