# 연결 요소의 개수 (11724)
## 난이도 : 중

import sys
input = sys.stdin.readline

node_cnt, line_cnt = list(map(int, input().split()))
mothers = [idx for idx in range(node_cnt+1)]

def find_mother(node):
    global mothers
    if node != mothers[node]:
        mothers[node] = find_mother(mothers[node])
    return mothers[node]

def union(x, y):
    global mothers
    x_mother = find_mother(x)
    y_mother = find_mother(y)
    chk_mother = 0
    before_mohter = 0
    if (x_mother <= y_mother):
        mothers[y] = x_mother
        chk_mother = x_mother
        before_mohter = y_mother
    else:
        mothers[x] = y_mother
        chk_mother = y_mother
        before_mohter = x_mother
    for idx in range(1, node_cnt + 1):
        temp_mother = mothers[idx]:
        if t

for _ in range(line_cnt):
    x,y = list(map(int, input().split()))
    union(x,y)

set_mother = set()

for idx in range(1,node_cnt+1):
    now_num = mothers[idx]
    if now_num in set_mother:
        continue
    set_mother.add(now_num)

print(len(set_mother))