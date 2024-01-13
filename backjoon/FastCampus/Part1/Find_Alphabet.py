# 알파벳 찾기 (10809)
## 난이도 : 하

import sys

#input = sys.stdin.readline
result = [-1 for _ in range(26)]

word = input()

for idx in range(len(word)):
    num = ord(word[idx]) - 97
    if (result[num] == -1):
        result[num] = idx

for rst in result:
    print(rst, end=' ')