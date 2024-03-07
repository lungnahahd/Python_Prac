# 친구 네트워크 (4195)

import sys

input = sys.stdin.readline

case = int(input())

def union(a, b):
    a_mom = find(a)
    b_mom = find(b)

    if(a < b):
        mother[b] = a_mom
    else:
        mother[a] = b_mom

def find(node):
    if mother[node] != node:
        return find(mother[node])
    else:
        return mother[node]


for _ in range(case):
    cnt_network  = int(input())
    mother = dict()
    cnt = 0
    for _ in range(cnt_network):
        a, b = input().split()
        if 1 not in mother:
            mother[a] = a
        if b not in mother:
            mother[b] = b
        union(a,b)
    print(mother)