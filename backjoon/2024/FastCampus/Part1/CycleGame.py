# 사이클게임 (20040)
## 난이도 : 골드 4

import sys
input = sys.stdin.readline
node_cnt, line_cnt = list(map(int, input().split()))
mother = [idx for idx  in range(node_cnt)]\



def change_mother(a, b):
    global mother

    if mother[a] > mother[b]:
        mother[mother[a]] = mother[b]
    else:
        mother[mother[b]] = mother[a]


def find_mother(node):
    if node == mother[node]:
        return node
    mother[node] = find_mother(mother[node])
    return mother[node]




isCycle = False
for step in range(line_cnt):
    a, b = list(map(int, input().split()))
    if find_mother(a) == find_mother(b):
        print(step+1)
        isCycle = True
        break
    change_mother(a, b)

if not isCycle:
    print(0)

