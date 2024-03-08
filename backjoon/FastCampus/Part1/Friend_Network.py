# 친구 네트워크 (4195)

import sys

input = sys.stdin.readline

case = int(input())

def union(a, b):
    a_mom = find(a)
    b_mom = find(b)

    if a_mom != b_mom:
        mother[b] = a_mom
        connect_num[a] += connect_num[b]
    print(connect_num[a])

def find(node):
    if mother[node] != node:
       mother[node] = find(mother[node])
    return mother[node]


for _ in range(case):
    cnt_network  = int(input())
    mother = dict()
    connect_num = dict()

    cnt = 0
    for _ in range(cnt_network):
        a, b = input().split()
        if a not in mother:
            mother[a] = a
            connect_num[a] = 1
        if b not in mother:
            mother[b] = b
            connect_num[b] = 1
        union(a,b)