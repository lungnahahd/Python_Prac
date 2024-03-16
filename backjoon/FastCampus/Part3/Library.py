# 도서관 (1461)
## 난이도 : 중

import sys
from collections import deque

input = sys.stdin.readline

cnt_book, can_bring = list(map(int, input().split()))
where_book = list(map(int, input().split()))
where_book.sort()
minus, plus = deque([]), deque([])

for book in where_book:
    if book < 0 :
        minus.append(book)
    else:
        plus.append(book)

rst = 0

minus_len, plus_len = len(minus), len(plus)
minus_idx, plus_idx = 0, plus_len - 1

max_vals = []

while minus_len != 0:
    max_vals.append(abs(minus[minus_idx]))
    if minus_len - minus_idx - 1 < can_bring:
        break
    minus_idx += can_bring


while plus_len != 0:
    max_vals.append(plus[plus_idx])
    if plus_idx < can_bring:
        break
    plus_idx -= can_bring

rst = 0
very_big_val = max(max_vals)

for val in max_vals:
    if val == very_big_val:
        rst += val
    else:
        rst += val * 2

print(rst)