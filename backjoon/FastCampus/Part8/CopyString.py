# 문자열 복사 (2195)
## 난이도 : 골드 5

import sys
from collections import deque
input = sys.stdin.readline 

orgin_string = list(input())[:-1]
want_string = list(input())[:-1]

end_copy_idx = 0
result = 0
while end_copy_idx < len(want_string):
    move_idx = 0
    mid_end = end_copy_idx
    for word in orgin_string:
        if end_copy_idx + move_idx < len(want_string) and word == want_string[end_copy_idx + move_idx]:
            move_idx += 1
        else:
            mid_end = max(end_copy_idx + move_idx - 1, mid_end)
            move_idx = 0
    result += 1
    end_copy_idx = mid_end + 1
print(result)
