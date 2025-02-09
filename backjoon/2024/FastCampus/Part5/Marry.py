# 결혼식 (5567)
## 난이도 : 실버 2

import sys
from collections import deque
input = sys.stdin.readline

mate_num = int(input())
relation_num = int(input())
relation = [[] for _ in range(mate_num + 1)]
already_invite = set()

for _ in range(relation_num):
    a, b = list(map(int, input().split()))
    relation[a].append(b)
    relation[b].append(a)

def invite(start):
    global already_invite

    already_invite.add(start)
    result = 0
    save = deque([(start,0)])
    cnt = 0
    while save :
        now_node, now_cnt =  save.popleft()
        if now_cnt > 1:
            break
        for next_node in relation[now_node]:
            if next_node not in already_invite: 
                already_invite.add(next_node)
                save.append((next_node, now_cnt+1))
                result += 1
    return result

invite_result = invite(1)
print(invite_result)