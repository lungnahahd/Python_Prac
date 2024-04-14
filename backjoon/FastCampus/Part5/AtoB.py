# A -> B (16953)
## 난이도 : 실버 2

from collections import deque

start_num, end_num = list(map(int, input().split()))

size_end_num = len(str(end_num)) # end_num의 자리수를 저장
already_make = set()
result = -1

def find_num_bfs(start):
    global already_make,result

    save = deque([(start, 1)])
    already_make.add(start)
    while save:
        num, cost = save.popleft()
        temp_multi = num * 2
        temp_plus_one = int(str(num) + '1')
        if temp_multi == end_num or temp_plus_one == end_num:
            result = cost + 1
            return
        if temp_multi < end_num:
            save.append((temp_multi, cost+1))
        if temp_plus_one < end_num:
            save.append((temp_plus_one, cost+1))
    return

find_num_bfs(start_num)
print(result)