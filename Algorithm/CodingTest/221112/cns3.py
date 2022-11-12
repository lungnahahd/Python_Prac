from itertools import combinations
import sys


def find_sub(s):
    size = len(s)
    return [s[start:end+1] for start in range(size) for end in range(start, size)]


#s = "abc"
s = "vxrvip"
#track = "bcab"
track = "xrviprvipvxrv"
l_s = list(s)
a = list(combinations(l_s, 2))
answer = 0
sub_str = find_sub(s)
for jump in range(len(s), 0, -1):
    print(jump)
    if answer >= jump:
        break
    border = jump
    start = 0
    temp = sys.maxsize
    can_result = True
    out = False
    while True:
        if border == len(track):
            out = True
        now_lst = track[start:border]
        now_str = ''.join(now_lst)
        print(now_str)
        if now_str in sub_str:
            temp = min(temp, len(now_str))
            start = border
            border = min(border+jump, len(track))
        else:
            can_result = False
            break
        if out:
            break
    if can_result:
        answer = max(answer, temp)
print(answer)
