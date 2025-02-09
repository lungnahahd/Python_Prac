# 이중 우선 순위 큐 (7622)
## 난이도 : 골드 4

import sys
import heapq

input = sys.stdin.readline

case_cnt = int(input())
for _ in range(case_cnt):
    method_cnt = int(input())
    min_hq, max_hq = [], []
    total_num_dict = dict()
    total_cnt = 0
    for _ in range(method_cnt):
        temp = input()
        now_method = temp.split()
        #now_method = list(input())
        if now_method[0] == "I":
            heapq.heappush(min_hq, int(now_method[1]))
            heapq.heappush(max_hq, -int(now_method[1]))
            if now_method[1] in total_num_dict:
                total_num_dict[now_method[1]] += 1
            else:
                total_num_dict[now_method[1]] = 1
            total_cnt += 1
        else:
            if total_cnt <= 0:
                continue
            total_cnt -= 1
            if now_method[1] == "-1":
                while True:
                    if len(min_hq) == 0:
                        break
                    out_num = heapq.heappop(min_hq)
                    if total_num_dict[str(out_num)]  > 0:
                        total_num_dict[str(out_num)] -= 1
                        break
            else:
                while True:
                    if len(max_hq) == 0:
                        break
                    out_num = heapq.heappop(max_hq)
                    if total_num_dict[str(-out_num)] > 0:
                        total_num_dict[str(-out_num)] -= 1
                        break
    if total_cnt == 0:
        print("EMPTY")
    else:
        answer_max, answer_min = 0,0

        while True:
            out_num = heapq.heappop(max_hq)
            if total_num_dict[str(-out_num)] > 0:
                answer_max = -out_num
                break
        while True:
            out_num = heapq.heappop(min_hq)
            if total_num_dict[str(out_num)] > 0:
                answer_min = out_num
                break
        answer = str(answer_max) + ' ' + str(answer_min)
        print(answer)