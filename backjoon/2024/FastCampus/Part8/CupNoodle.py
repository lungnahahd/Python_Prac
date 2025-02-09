# 컵라면 (1781)
## 난이도 : 골드 2

import sys
import heapq
input = sys.stdin.readline

count = int(input())
noodles, best_choice = [], []

for _ in range(count):
    deadline, cup_num = list(map(int, input().split()))
    noodles.append((deadline, cup_num))

noodles.sort() # 컵라면을 데드라인 기준으로 정렬

for now in noodles:
    heapq.heappush(best_choice, now[1]) # 일단 데드라인 기준으로 값들을 저장 
    if len(best_choice) > now[0]:   # 큐의 크기가 데드라인 기준으로 생각 --> 즉, 2개의 값이 있으면 데드라인 2가 되었다고 생각
        heapq.heappop(best_choice)  # 데드라인 기준으로 가장 작은 값은 내보내기 --> 내보내고 다른 값을 취하는 것이 이득이므로..

print(sum(best_choice))