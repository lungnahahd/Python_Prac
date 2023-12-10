# 0에 가장 가까운 합

num_cnt = int(input())
num_list = list(map(int, input().split()))

answer = 1000000000

for start in range(num_cnt - 1):
    t_start = start + 1
    for end in range(t_start, num_cnt):
        now_sum = abs(num_list[start] + num_list[end])
        answer = min(now_sum, answer)

print(answer)
