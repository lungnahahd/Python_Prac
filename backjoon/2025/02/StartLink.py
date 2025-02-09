# 스타트와 링크 (14889)
## 난이도 : 실버 1

import sys
input = sys.stdin.readline


people_num = int(input())
score = []
our_team = []
total_people = [i for i in range(people_num)]
total_score = 0
result = sys.maxsize

for _ in range(people_num):
    temp_score = list(map(int, input().split()))
    score.append(temp_score)
    total_score += sum(temp_score)

def cal_different(team):
    our_score, opposite_score = 0, 0
    for now_idx in range(len(team)-1):
        for next_idx in range(now_idx, len(team)):
            now_p, next_p = team[now_idx], team[next_idx]
            our_score += score[now_p][next_p]
            our_score += score[next_p][now_p]
    
    opposite = list(set(total_people) - set(team))
    for now_idx in range(len(opposite)-1):
        for next_idx in range(now_idx, len(opposite)):
            now_p, next_p = opposite[now_idx], opposite[next_idx]
            opposite_score += score[now_p][next_p]
            opposite_score += score[next_p][now_p]


    return abs(our_score - opposite_score)

def back_tracking(now_people):
    global our_team, result

    if len(our_team) == int(people_num // 2):
        result = min(result, cal_different(our_team))
        return

    for people in range(now_people, people_num):
        our_team.append(people)
        back_tracking(people+1)
        our_team.pop()

back_tracking(0)
print(result)