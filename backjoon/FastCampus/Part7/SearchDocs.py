# 문서 검색 (1543)
## 난이도 : 실버 5

import sys

docs = list(input())
find = list(input())

idx = 0
result = 0
for word in docs:
    if word == find[idx]:
        idx += 1
        if idx == len(find):
            idx = 0
            result += 1
    else:
        if word == find[0]:
            idx = 1
        else:
            idx = 0
print(result)