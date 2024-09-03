# Yonsei TOTO (1218)
## 난이도 : 실버 3

import sys
import heapq
input = sys.stdin.readline

subject_count, max_point = list(map(int, input().split()))

minimal_points = []
for _ in range(subject_count):
    already_people, now_class_max = list(map(int, input().split()))
    now_points = list(map(int, input().split()))
    now_points.sort(reverse=True)
    if len(now_points) < now_class_max:
        heapq.heappush(minimal_points, 1)
    else:
        heapq.heappush(minimal_points, now_points[now_class_max-1])

result = 0
while minimal_points:
    now_point = heapq.heappop(minimal_points)
    max_point -= now_point
    if max_point >= 0:
        result += 1
    else:
        break

print(result)