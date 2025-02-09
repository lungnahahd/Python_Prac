# 주사위 (1233)
## 난이도 : 하

import sys

input = sys.stdin.readline
a_size, b_size, c_size = list(map(int, input().split()))
result = dict()

for s1 in range(1, a_size+1):
    for s2 in range(1, b_size+1):
        for s3 in range(1, c_size+1):
            temp = s1 + s2 + s3
            if temp in result:
                result[temp] += 1
            else:
                result[temp] = 1

max_size = 0
answer = 0

for key in result.keys():
    if result[key] > max_size:
        max_size = result[key]

        answer = key
print(answer)
