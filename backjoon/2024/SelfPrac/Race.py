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

# 초기에 최대로 가능한 가장 넓은 간격을 활용해서 비교
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

end_count = 0 # 혹시나 간격이 더 넓은 경우 처리를 위한 변수 ... --> 여기서 확인 안 하면 반례 생김..
for asr in answer:
    end_count += 1
    answer_show[asr] = '1'
    if end_count == people_num:
        break

print(''.join(answer_show))