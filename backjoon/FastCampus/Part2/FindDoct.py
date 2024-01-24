# 문서 검색 (1543)
## 난이도 : 하

#import sys

#input = sys.stdin.readline

doct = list(input())
find = list(input())

now_idx = 0
result = 0
back_idx, go_idx = 1, 0

while go_idx < len(doct):
    if doct[go_idx] == find[now_idx]:
        if now_idx == len(find):
            result += 1
            back_idx = go_idx + 2
            now_idx = 0
        else:
            now_idx += 1
    else:
        now_idx = 0
        go_idx = back_idx

print(result)

