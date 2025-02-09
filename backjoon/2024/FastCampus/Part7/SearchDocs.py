# 문서 검색 (1543)
## 난이도 : 실버 5

import sys
INT_MAX = sys.maxsize
docs = list(input())
find = list(input())
can_case = []

idx = 0
result = 0

start = find[0]
find_size = len(find)

for idx in range(len(docs)):
    if docs[idx] == start and (idx + find_size -1) < len(docs):
        can_case.append((docs[idx:idx + find_size], idx, idx+find_size-1))

result = 0
last_idx = -1
for case in can_case:

    if case[0] == find and last_idx < case[1]:
        last_idx = case[2]
        result += 1
print(result)