# 좌표 압축 (18870)
## 난이도 : 실버 2

import sys
import copy

input = sys.stdin.readline
result = []
cnt = int(input())
num_list = list(map(int, input().split()))

unique_list = list(set(num_list))
unique_list.sort()

dict = {}
for idx in range(len(unique_list)):
    dict[unique_list[idx]] = idx

for num in num_list:
    print(dict[num], end= ' ')