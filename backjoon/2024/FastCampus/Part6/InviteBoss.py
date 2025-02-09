# 이장님 초대 (9237)
## 난이도 : 실버 5
import heapq

cnt = int(input())
trees = list(map(int, input().split()))

tree_queue = []

for tree in trees:
    heapq.heappush(tree_queue, -tree)

days = 1
result = 0
while tree_queue:
    now_tree = heapq.heappop(tree_queue)
    result = max(result, -(now_tree) + days)
    days += 1

print(result + 1)