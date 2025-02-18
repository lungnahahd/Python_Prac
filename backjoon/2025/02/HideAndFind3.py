# 숨바꼭질 3
## 난이도 : 골드 5

import sys
input = sys.stdin.readline


a, b = list(map(int, input().split()))
start = min(a,b)
end = max(a,b)
result = sys.maxsize


def back_track(start, end, cnt):
    global result
    
    if start == end:
        result = min(cnt, result)
        return
    if end > 100000 or end < start:
        return

    if end % 2 == 0:
        back_track(start, end / 2, cnt)
    
    back_track(start, end+1, cnt + 1)
    back_track(start, end-1, cnt + 1)

back_track(start, end, 0)
print(result)