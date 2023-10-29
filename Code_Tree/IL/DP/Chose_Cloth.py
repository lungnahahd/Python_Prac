# 적절한 옷 고르기

num_cloth, days = list(map(int, input().split()))
cost = [[0 for _ in range(days)] for _ in range(num_cloth)]
result = [[0 for _ in range(days)] for _ in range(num_cloth)]

for idx in range(num_cloth):
    start, end, val = list(map(int, input().split()))
    for d in range(start-1, end):
        cost[idx][d] = val

for day in range(1, days):
    for cloth in range(num_cloth):
        if (cost[cloth][day] != 0):
            for obj in range(num_cloth):
                if (cost[obj][day-1] != 0):
                    now_cost = abs(cost[obj][day-1] - cost[cloth][day])
                    result[cloth][day] = max(result[cloth][day], result[obj][day-1] + now_cost)

answer = 0

for cloth in range(num_cloth):
    answer = max(answer, result[cloth][days-1])

print(answer)
