# 우리집엔 도서관이 있어 
## 난이도 : 실버1

import sys
input = sys.stdin.readline

book_cnt = int(input())
rank_dict, book_dict = dict(), dict()

for idx in range(book_cnt):
    num = int(input())
    rank_dict[idx+1] = num

isEnd = False
result_count = 0
now_top = 0
top_idx = 0

while True:
    if isEnd:
        break
    if rank_dict[1] != 1:
        now_top = rank_dict[1]
        top_idx = 1
    else:
        now_top = rank_dict[2]
        top_idx = 2
    
    for where in range(top_idx+1, book_cnt+1):
        if now_top -1 == rank_dict[where]:
            rank_dict[1] = rank_dict[where]
            for before_where in range(2,where+1):
                rank_dict[before_where] = rank_dict[before_where+1]
            

    result_count += 1

print(result_count)