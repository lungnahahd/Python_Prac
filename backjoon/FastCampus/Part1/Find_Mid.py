# 중앙값 구하기
## 난이도 : 골드 2

import sys
import heapq
input = sys.stdin.readline

case_cnt = int(input())

for _ in range(case_cnt):
    num_cnt = int(input())
    num_list = []
    for _ in range(num_cnt//10 + 1):
        temp = list(map(int, input().split()))
        for num in temp:
            num_list.append(num)
    


    big_hq, small_hq = [], []
    now_mid = 0
    mid_nums = []
    for now_idx in range(len(num_list)):
        if now_idx == 0:
            now_mid = num_list[now_idx]
            mid_nums.append(now_mid)
            continue
        now_num = num_list[now_idx]
        if now_num >= now_mid:
            heapq.heappush(big_hq, now_num)
        else:
            heapq.heappush(small_hq, -now_num)
        
        if now_idx % 2 == 0:
            if len(big_hq) > len(small_hq):
                heapq.heappush(small_hq, -now_mid)
                temp = heapq.heappop(big_hq)
                now_mid = temp
            elif len(big_hq) < len(small_hq):
                heapq.heappush(big_hq, now_mid)
                temp = heapq.heappop(small_hq)
                now_mid = -temp
            mid_nums.append(now_mid)
    for idx in range(len(mid_nums)):
        print(mid_nums[idx], end = ' ')
        if (idx % 10 == 9 and idx != len(mid_nums)-1):
            print()