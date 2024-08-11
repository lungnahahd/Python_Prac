# 레이스 (1508)
## 난이도 : 골드 2

import sys
import heapq
input = sys.stdin.readline

distance, people_num, point_num = list(map(int, input().split()))
points = list(map(int, input().split()))

between_dist = []
for idx in range(1, point_num):
    between_dist.append(points[idx] - points[idx-1])


first_dist = distance // (people_num - 1)

answer = [0]
answer_show = ['0' for _ in range(point_num)]
while len(answer) < people_num:
    answer = [0]
    before_idx = 0
    for idx in range(1,point_num):
        if points[idx] - points[before_idx] >= first_dist:
            answer.append(idx)
            before_idx = idx
    first_dist -= 1

for asr in answer:
    answer_show[asr] = '1'

print(''.join(answer_show))