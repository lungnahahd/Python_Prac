from itertools import permutations
import heapq

# a = [1, 2, 3, 4, 4]
# b = list(permutations(a, 5))
a = [5, 5, 1, 4]
b = list(permutations(a, 3))

save = []
for c in b:
    left = c[:len(c)//2]
    right = c[len(c)//2+1:]
    if sum(left) == sum(right):
        heapq.heappush(save, (-sum(c), c))
print(save)
_, result = heapq.heappop(save)
print(list(result))
