n = int(input())
num_arr = list(map(int, input().split()))
result = [0 for _ in range(n)]


can_move = []
can_move.append(0)

while can_move:
    node = can_move.pop()
    max_jump = num_arr[node]
    for jump in range(1,max_jump+1):
        if(node + jump < n):
            result[node+jump] = max(result[node+jump], result[node] + 1)
            can_move.append(node+jump)

print(max(result))
