# 타켓 넘버 (Level 2)

def solution(numbers, target):
    maxNum = 0
    answer = 0
    for i in numbers:
        maxNum += i
    diff = maxNum - target
    if diff % 2 == 0:
        diff = diff / 2
        
    return answer