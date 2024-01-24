# 문서 검색 (1543)
## 난이도 : 하

#import sys

#input = sys.stdin.readline

doct = list(input())
find = list(input())

now_idx = 0
result = 0

for word in doct:
    if word == doct[now_idx]:
        if now_idx == len(find):
            result += 1
        else:
            now_idx += 1
    else:
        now_idx = 0

print(result)

