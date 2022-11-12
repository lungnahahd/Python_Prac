robots, round = list(map(int,input().split()))

upperR = [[] for _ in range(robots+1)]
lowerR = [[] for _ in range(robots+1)]

for _ in range(round):
    win, lose = list(map(int,input().split()))
    lowerR[win].append(lose)
    upperR[lose].append(win)

check = [False for _ in range(robots+1)]
answer = 0
for robot in range(1,robots+1):
    rank = len(lowerR[robot]) + len(upperR[robot])
    if rank == robots-1 and not check[robot]:
        answer+= 1
        check[robot] = True
        if len(lowerR[robot]) == 1:
            if not check[lowerR[robot][0]]:
                answer += 1
                check[lowerR[robot][0]] = True
        if len(upperR[robot]) == 1:
            if not check[upperR[robot][0]]:
                answer += 1
                check[upperR[robot][0]] = True
    if answer == robots:
        break
print(answer)