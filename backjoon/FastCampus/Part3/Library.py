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
while minus or plus:
    m_len, p_len = len(minus), len(plus)
    if m_len <= p_len:
        if p_len > can_bring:
            rst += (plus[-1] * 2)
            for _ in range(can_bring):
                plus.pop()
        else:
            if m_len == 0:
                rst += (plus[-1])
                break
            rst += (plus[-1] * 2)
            plus = []
            need_go = min(can_bring - p_len, m_len)
            if need_go == p_len:
                rst += ([need_go-1])
                break
            for _ in range(need_go):
                minus.popleft()
            rst += (minus[need_go-1] * 2)
    else:
        if m_len > can_bring:
            rst += (minus[-1] * 2)
        else:
            if p_len == 0:
                rst += (minus[-1])
                break
            rst += (minus[-1] * 2)
            minus = []
            need_go = min(can_bring - m_len, p_len)
            if need_go == p_len:
                rst += (plus[need_go-1])
                break
            for _ in range(need_go):
                plus.popleft()
            rst += (plus[need_go-1] * 2)

print(rst)