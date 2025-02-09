# 나는 요리사다 (2953)
## 난이도 : 하

score = 0
winner = 0

for idx in range(5):
    now_cooker = list(map(int, input().split()))
    temp_score = 0
    for now in now_cooker:
        temp_score += now
    if(score < temp_score):
        score = temp_score
        winner = idx + 1

print(winner, end=' ')
print(score)