# 통나무 건너뛰기 (11497)
## 난이도 : 실버 1

import sys
from collections import deque

INT_MAX = sys.maxsize
input = sys.stdin.readline
cnt_case = int(input())
answer = []

for _ in range(cnt_case):
    sort_tree = deque([])
    tree_cnt = int(input())
    tree_list = list(map(int, input().split()))
    tree_list.sort()
    start = tree_cnt - 2
    sort_tree.append(tree_list[-1])
    result = 0
    while start != -1:
        if start ==  0:
            sort_tree.append(tree_list[0])
            break
        else:
            sort_tree.append(tree_list[start-1])
            sort_tree.appendleft(tree_list[start])
            start -= 2
    for idx in range(0, tree_cnt-1):
        result = max(result, abs(sort_tree[idx] - sort_tree[idx+1]))
    result = max(result, abs(sort_tree[0] - sort_tree[-1]))
    answer.append(result)

for asr in answer:
    print(asr)