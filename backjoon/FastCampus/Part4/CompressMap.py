# 좌표 압축 (18870)
## 난이도 : 실버 2

import sys

input = sys.stdin.readline

cnt = int(input())
num_list = list(input().split())

temp = set()

for num in num_list:
    temp.add(num)

sort_list = []
for num in temp:
    sort_list.append(int(num))

sort_list.sort()

result = []
for num in num_list:
    result.append(str(sort_list.index(int(num))))

print(' '.join(result))

