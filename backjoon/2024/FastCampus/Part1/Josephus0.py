# 요세푸스 문제0 (11866)

from collections import deque

queue = deque([])
result = []
list_size, gap = list(map(int, input().split()))

for idx in range(1, list_size + 1):
    queue.append(idx)

while queue:
    for _ in range(gap-1):
        now_num = queue.popleft()
        queue.append(now_num)
    out_num = queue.popleft()
    result.append(out_num)

answer = '<'
for idx in range(len(result)-1):
    answer += str(result[idx])
    answer += ', '
answer += str(result[-1])
answer += '>'
print(answer)

