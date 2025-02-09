# 철로 (13334)
## 난이도 : 골드 2

import sys
input = sys.stdin.readline

cnt_people = int(input())

end_point = []
rail_info = dict()

for _ in range(cnt_people):
    start, end = list(map(int, input().split()))
    end_point.append(end)
    if end in rail_info:
        rail_info[end].append(start)
    else:
        rail_info[end] = [start]
end_point.sort(reverse=True)

train_size = int(input())

for start in end_point:
    