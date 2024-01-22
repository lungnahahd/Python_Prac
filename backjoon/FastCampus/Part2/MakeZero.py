# 0 만들기 (7490)
## 난이도 : 중


# 1+2-3    /    3

# 1+2-3+4-5-6+7     /       7
# 1+2-3-4+5+6-7
# 1-2 3+4+5+6+7
# 1-2 3-4 5+6 7
# 1-2+3+4-5+6-7
# 1-2-3-4-5+6+7

import sys
import heapq
input = sys.stdin.readline



def make_zero(temp_rst, real_rst, now, end):
    global save
    if (end == now):
        if(eval(temp_rst) == 0):
            #print(real_rst)
            heapq.heappush(save, real_rst)
        return
    else:
        now += 1
        make_zero(temp_rst + '+' + str(now) ,real_rst + '+' + str(now), now, end)
        make_zero(temp_rst + '-' + str(now) ,real_rst + '-' + str(now), now, end)
        make_zero(temp_rst + str(now) ,real_rst + ' ' + str(now), now, end)

case = int(input())
for _ in range(case):
    save = []
    max_num = int(input())
    make_zero('1','1',1,max_num)
    while save:
        now_save = heapq.heappop(save)
        print(now_save)
    print()