# 계단 오르기
## n 층의 계단을 2계단 또는 3계단 씩 오를때, 딱 원하는 n층에 도달할 때의 경우의 수 구하기
##### DP 중 SubProblem 으로 해결

top = int(input())

go_top_count = [0 for _ in range(top+1)]
go_top_count[2] = 1
if(top > 2):
    go_top_count[3] =  1

for idx in range(2,top+1):
    if(idx+2 <= top):
        go_top_count[idx+2] += go_top_count[idx]
    if(idx+3 <= top ):
        go_top_count[idx+3] += go_top_count[idx]

print(go_top_count[top] % 10007)
