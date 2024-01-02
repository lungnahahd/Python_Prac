# 풍선 터뜨리기 (2346)
## 난이도 : 하

from collections import deque


cnt_ballon = int(input())
paper_num = list(map(int, input().split()))
paper_dq = deque(paper_num)
result = []

ballon_dq = deque([ballon for ballon in range(1, cnt_ballon + 1)])

while ballon_dq:
    ballon = ballon_dq.popleft()
    result.append(str(ballon))
    now_move = paper_num[ballon-1]
    if not ballon_dq:
        break
    if now_move < 0:
        for _ in range(abs(now_move)):
            temp = ballon_dq.pop()
            ballon_dq.appendleft(temp)
    else:
        for _ in range(now_move-1):
            temp = ballon_dq.popleft()
            ballon_dq.append(temp)
            
answer = ' '.join(result)
print(answer)