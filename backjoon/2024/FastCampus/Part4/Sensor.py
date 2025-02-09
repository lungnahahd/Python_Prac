# 센서 (2212)
## 난이도 : 골드(5)

import sys
input = sys.stdin.readline

cnt_sensor = int(input())
cnt_station = int(input())

sensors = list(map(int, input().split()))
sensors.sort()

distance = []

# 센서 사이의 거리를 구하기
for idx in range(1, cnt_sensor):
    distance.append(abs(sensors[idx] - sensors[idx-1]))

distance.sort(reverse=True)

rst = 0
 
for idx in range(cnt_station-1, len(distance)):
    rst += distance[idx]
print(rst)