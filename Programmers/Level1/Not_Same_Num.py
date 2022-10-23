# 같은 숫자는 싫어~
from collections import deque


def solution(arr):
    answer = []
    answer.append(arr[0])
    for num in arr[1:]:
        if answer[-1] == num:
            continue
        answer.append(num)
    
    return answer