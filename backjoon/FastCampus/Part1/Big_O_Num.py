# 오큰수 (17298)
## 난이도 : 중상
import sys

input = sys.stdin.readline

result = []
left_stack, right_stack = [], []
cnt_num = int(input())
num_list = input().split()

for idx in range(cnt_num-1, -1, -1):
    left_stack.append(num_list[idx])

for idx in range(cnt_num):
    left_stack.pop()
    big_o_num = '-1'
    while left_stack:
        now_num = left_stack.pop()
        right_stack.append(now_num)
        if (now_num > num_list[idx]):
            big_o_num = now_num
            break
    result.append(big_o_num)
    right_stack.reverse()
    left_stack = left_stack + right_stack
    right_stack.clear()

print(' '.join(result))