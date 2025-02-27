# 이전 순열
## 난이도 : 실버 3

import sys
input = sys.stdin.readline

num_cnt = int(input())
after_target = list(map(int, input().split()))
after_key = ''
for now in after_target:
    after_key += str(now)
already_get = set()
value_answer = dict()
key_answer = dict()
index = 1

def find_key(now_arr):
    global already_get, value_answer, key_answer, index

    if len(now_arr) == num_cnt:
        temp = ''.join(now_arr)
        key_answer[temp] = index
        value_answer[index] = temp
        index += 1
        return

    for num in range(1,num_cnt + 1):
        if num not in already_get:
            already_get.add(num)
            now_arr.append(str(num))
            find_key(now_arr)
            now_arr.pop()
            already_get.remove(num)


find_key([])

if key_answer[after_key] == 1:
    print(-1)
else:
    val = key_answer[after_key]
    answer = value_answer[val-1]
    print(' '.join(answer))