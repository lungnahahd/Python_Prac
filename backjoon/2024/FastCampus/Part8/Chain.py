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
    if len(chain_list) - 2 - answer in chain_list:
        
        answer += (len(chain_list) - 2 - answer)
        break
    now_chain = chain_list.pop()
    now_chain += answer
    step = len(chain_list) - 1
    if step == now_chain:
        answer += step
        break
    elif step > now_chain:
        answer += now_chain
    else:
        
        answer += step
        answer += 1
        break
    print(now_chain, step,answer)
print(answer)