# 마을 구분하기

n = int(input())

visited = [[False for _ in range(n)] for _ in range(n)]
town = []

village_size = 0
village_people = []

for i in range(n):
    temp = list(map(int,input().split()))
    town.append(temp)
x_move = [0,+1,0,-1]
y_move = [+1,0,-1,0]
x_check, y_check = 0,0
while x_check < n and y_check < n:
    village = []
    if town[y_check][x_check] == 1 and not visited[y_check][x_check]:
        village.append((y_check,x_check))
        visited[y_check][x_check] = True
    num_people = 1
    while village:
        y_now, x_now = village.pop()
        for idx in range(4):
            y_temp, x_temp = y_now + y_move[idx], x_now + x_move[idx]
            if 0 <= y_temp < n and 0 <= x_temp < n and town[y_temp][x_temp] == 1 and not visited[y_temp][x_temp]:
                village.append((y_temp,x_temp))
                visited[y_temp][x_temp] = True
                num_people += 1
        if len(village) == 0:
            village_people.append(num_people)
            village_size += 1
    if x_check == n - 1:
        y_check += 1
        x_check = 0
    else:
        x_check += 1
village_people.sort()
print(village_size)
for i in village_people:
    print(i)