# 적절한 옷 고르기

cloth, day = map(int,input().split())

info = []
can_pick = [[] for _ in range(day+1)]

for _ in range(cloth):
    start, end, point = map(int,input().split())
    for i in range(start,end+1):
        can_pick[i].append(point)
score = 0
def bk(before,today,temp):
    global score
    if today == day:
        for i in can_pick[today]:
            temp += abs(before-i)
            score = max(score, temp)
            return
    for i in can_pick[today]:
        temp += abs(before-i)
        bk(i,today + 1,temp)
        temp -= abs(before-i)
for i in can_pick[1]:
    bk(i,2,0)
print(score)