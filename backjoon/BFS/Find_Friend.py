# 케빈 베이컨의 6단계 법칙
from collections import deque
import heapq

user_num, relation_num = map(int,input().split())
user = [[] for _ in range(user_num+1)]
result = []

for r in range(relation_num):
    a,b = map(int,input().split())
    user[a].append(b)
    user[b].append(a)

for people in range(1,user_num+1):
    save = deque()
    check = [False for _ in range(user_num+1)]
    check[0] = True
    check[people] = True
    save.append((0,people))
    kb_score = 0
    visit = 1
    while save and visit != user_num:
        dist, node= save.popleft()
        for i in user[node]:
            if check[i]:
                continue
            check[i] = True
            visit += 1
            kb_score += dist + 1
            save.append((dist+1,i))
        
    heapq.heappush(result,(kb_score,people))
s,p = result[0]
print(p)