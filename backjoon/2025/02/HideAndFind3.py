# 숨바꼭질 3
## 난이도 : 골드 5

import sys
input = sys.stdin.readline


start, end = list(map(int, input().split()))
result = sys.maxsize

def back_track(start, end, cnt):
    global result
    
    if start == end:
        result = min(cnt, result)
        return
    if start > end or end > 100000:
        return

    if end % 2 == 0:
        back_track(start, end / 2, cnt)
    else:
        back_track(start, end+1, cnt + 1)
        back_track(start, end-1, cnt + 1)

back_track(start, end, 0)
print(result)