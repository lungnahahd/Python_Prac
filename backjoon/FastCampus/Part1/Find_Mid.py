# 중앙값 구하기
## 난이도 : 중

import sys
import heapq
#input = sys.stdin.readline

case_cnt = int(input())
result = [[] for _ in range(case_cnt)]

for idx in range(case_cnt):
    size = int(input())
    small = []
    big = []
    now_case = list(map(int, input().split()))
    now_mid = 0
    now_rst = result[idx]
    for cs_idx in range(len(now_case)):
        if (cs_idx == 0):
            now_rst.append(str(now_case[cs_idx]))
            now_mid = now_case[cs_idx]
        else:
            if(now_case[cs_idx] < now_mid):
                heapq.heappush(small, -(now_case[cs_idx]))
            else:
                heapq.heappush(big, now_case[cs_idx])
            if(cs_idx % 2 == 0):
                if (len(small) > len(big)):
                    heapq.heappush(big, now_mid)
                    now_mid = -heapq.heappop(small)
                elif(len(small) < len(big)):
                    heapq.heappush(small, -now_mid)
                    now_mid = heapq.heappop(big)
                now_rst.append(str(now_mid))

for idx in range(case_cnt):
    print(len(result[idx]))
    print(' '.join(result[idx]))
