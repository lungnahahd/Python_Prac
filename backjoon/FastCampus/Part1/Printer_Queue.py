# 프린터 큐 (1966)

import heapq

case_size = int(input())
answer = []

for _ in range(case_size):
    print_num, want = tuple(map(int, input().split()))
    list_print = list(map(int, input().split()))
    cnt = 1
    print_queue = []
    again_push = 0
    for idx in range(1, len(list_print)+1):
        heapq.heappush(print_queue, (idx, list_print[idx-1], idx-1))
        again_push = idx
    strong = 0
    list_print.sort(reverse=True)

    while(print_queue):
        turn, power, where = heapq.heappop(print_queue)
        if (power == list_print[strong]):
            if (where == want):
                answer.append(cnt)
                break
            else:
                cnt += 1
                strong += 1
        else:
            again_push += 1
            heapq.heappush(print_queue, (again_push, power, where))

for num in answer:
    print(num)