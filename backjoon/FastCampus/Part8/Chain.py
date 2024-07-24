# 체인 (2785)
## 난이도 : 실버 1

import sys
import heapq
input = sys.stdin.readline 

count_chain = int(input())
chain_list = list(map(int, input().split()))
chain_list.sort(reverse = True)


answer = 0
while chain_list:
    now_chain = chain_list.pop()
    step = len(chain_list) - 1
    if step == now_chain:
        answer += step
        break
    elif step > now_chain:
        answer += step
    else:
        answer += step
        answer += 1
        break
print(answer)