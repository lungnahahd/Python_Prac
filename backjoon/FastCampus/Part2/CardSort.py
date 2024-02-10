# 카드 정렬하기 (1715)
## 난이도 : 하

import heapq
import sys

input = sys.stdin.readline

cnt = int(input())
cards = []

for _ in range(cnt):
    card = int(input())
    heapq.heappush(cards, card)

mid_sum = heapq.heappop(cards)
result = 0

while cards:
    now = heapq.heappop(cards)
    mid_sum += now

    result += mid_sum

print(result)