# 문제집 (1766)
## 난이도 : 중

import sys
import heapq

input = sys.stdin.readline

cnt_book, cnt_priority = list(map(int, input().split()))

books = [0 for _ in range(cnt_book+1)]
mapping = [[] for _ in range(cnt_book+1)]

sort_queue = []
for _ in range(cnt_priority):
    root, child = list(map(int, input().split()))
    books[child] += 1
    mapping[root].append(child)

visitied = set()

for idx in range(1, cnt_book+1):
    if books[idx] == 0:
        heapq.heappush(sort_queue, idx)
        visitied.add(idx)

result = []

if cnt_book == 1:
    print('1')
else:
    while sort_queue:
        now = heapq.heappop(sort_queue)
        visitied.add(now)
        result.append(str(now))
        if len(mapping[now]) == 0:
            continue
        for idx in mapping[now]:
            books[idx] -= 1
            if not idx in visitied and books[idx] == 0:
                heapq.heappush(sort_queue, idx)

    print(' '.join(result))
