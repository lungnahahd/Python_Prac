# 시리얼 번호 (1431)
## 난이도 : 실버 3

import heapq

cnt = int(input())

save = []

for _ in range(cnt):
    now = input()
    now_serial = list(now)
    sum_num = 0
    for word in now_serial:
        if word.isdigit():
            sum_num += int(word)
    heapq.heappush(save, (len(now_serial),sum_num ,now))

for _ in range(len(save)):
    _, _, serial = heapq.heappop(save)
    print(serial)

