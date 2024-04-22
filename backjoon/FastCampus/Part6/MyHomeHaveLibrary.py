# 우리 집에는 도서관이 있어 (2872)
## 난이도 : 실버2

import sys
input = sys.stdin.readline
from collections import deque

cnt_book = int(input())
books = deque([])

for _ in range(cnt_book):
    book = int(input())
    books.append(book)
if cnt_book == 1:
    print(0)
else:
    result = 0
    keep_going = True
    while keep_going:
        keep_going = False
        temp_save = deque([books[0]])
        for idx in range(1, cnt_book):
            if keep_going or books[idx-1] < books[idx]:
                temp_save.append(books[idx])
            if books[idx-1] > books[idx]:
                temp_save.appendleft(books[idx])
                keep_going = True
                result += 1
        for idx in range(cnt_book):
            books[idx] = temp_save[idx]
        temp_save.clear()
            
            




    print(result)