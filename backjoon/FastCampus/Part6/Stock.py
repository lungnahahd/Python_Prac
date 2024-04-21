# 주식 (11501)
## 난이도 : 실버 2

import heapq
import sys
input = sys.stdin.readline

case_cnt = int(input())
answer = []

for _ in range(case_cnt):
    already = set()
    result = 0
    chart_cnt = int(input())
    chart = list(map(int, input().split()))
    big_chart = [0 for _ in range(len(chart))]
    temp_big = 0
    for idx in range(chart_cnt-1, -1, -1):
        temp_num = chart[idx]
        temp_big = max(temp_big, temp_num)
        big_chart[idx] = temp_big
    
    for idx in range(chart_cnt):
        result += (big_chart[idx] - chart[idx])

    answer.append(result)


for aws in answer:
    print(aws)