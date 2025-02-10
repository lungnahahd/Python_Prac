# 모든 수열 (10974)
## 난이도 : 실버 3

import sys
input = sys.stdin.readline

cnt = int(input())
temp = []
already_in = set()

def back_track():
    global temp, already_in

    if len(temp) == cnt:
        for num in temp:
            print(num, end = ' ')
        print()
        return
    
    for idx in range(1, cnt+1):
        if idx not in already_in:
            temp.append(idx)
            already_in.add(idx)
            back_track()
            already_in.remove(idx)
            temp.pop()

back_track()