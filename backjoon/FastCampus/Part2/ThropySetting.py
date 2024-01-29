# 트로피 진열 (1668)
## 난이도 : 하

import sys
from collections import deque

input = sys.stdin.readline

cnt_award = int(input())
awards = []


for _ in range(cnt_award):
    size = int(input())
    awards.append(size)

left, right = deque(awards), deque(awards)

result = []


height_tall = -1
temp_result = 0

for _ in range(cnt_award):
    now_height = left.popleft()
    if now_height > height_tall:
        height_tall = now_height
        temp_result += 1
    
result.append(temp_result)

height_tall = -1
temp_result = 0

for _ in range(cnt_award):
    now_height = right.pop()
    if now_height > height_tall:
        height_tall = now_height
        temp_result += 1

result.append(temp_result)

for height in result:
    print(height)        