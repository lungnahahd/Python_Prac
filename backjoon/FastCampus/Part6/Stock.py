# 주식 (11501)
## 난이도 : 실버 2

import heapq

case_cnt = int(input())
answer = []

for _ in range(case_cnt):
    already = set()
    chart_cnt = int(input())
    chart = list(map(int, input().split()))
    chart_hq = []
    result = 0
    for idx in range(len(chart)):
        heapq.heappush(chart_hq,(-chart[idx], idx))
    while chart_hq:
        now_data, day = heapq.heappop(chart_hq)
        now_data = -(now_data)
        already.add(day)
        for before in range(day-1,-1,-1):
            if before not in already:
                result += (now_data- chart[before])
                already.add(before)
    answer.append(result)

for aws in answer:
    print(aws)