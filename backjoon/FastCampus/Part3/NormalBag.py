# 평범한 배낭 (12865)
## 난이도 : 하

# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

import sys
import heapq

case, max_weight = list(map(int, input().split()))

save_weight = [[0 for _ in range(max_weight + 1)] for _ in range(case+1)]

for idx in range(1, case+1):
    now_weight, now_cost = list(map(int, input().split()))
    for proceed in range(1, max_weight + 1):
        if proceed < now_weight:
            save_weight[idx][proceed] = save_weight[idx-1][proceed]
        else:
            dp_proceed = proceed - now_weight
            save_weight[idx][proceed] = max(save_weight[idx-1][proceed], save_weight[idx][dp_proceed] + now_cost)


print(save_weight[-1][-1])