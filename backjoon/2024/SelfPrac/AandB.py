# A와 B (12904)
## 난이도 : 골드 5

from collections import deque


origin = list(input())
purpose = list(input())
end_time = len(purpose) - len(origin)

# purpose_str = ''.join(purpose)

answer = 0

def find(now):
    global answer
    if len(now) == len(purpose):
        #print(''.join(now), purpose_str)
        # if ''.join(now) == purpose_str:
        #     answer = 1
        if now == purpose:
            answer = 1
            return
    else:
        now.append("A")
        #print(now)
        find(now)
        now.pop()
        now.reverse()
        now.append("B")
        #print(now)
        find(now)
        now.pop()
        now.reverse()

find(origin)
print(answer)