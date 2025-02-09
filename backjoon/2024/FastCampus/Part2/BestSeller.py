# 베스트셀러 (1302)
## 난이도 : 하

import heapq

temp = dict([])
prior = []

cnt_sell = int(input())

for _ in range(cnt_sell):
    book = input()
    if book in temp:
        temp[book] = temp[book] + 1
        continue
    temp[book] = 1

for key, val in temp.items():
    heapq.heappush(prior, (-val, key))

_, answer = heapq.heappop(prior)

print(answer)
