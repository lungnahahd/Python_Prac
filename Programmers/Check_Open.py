# 올바른 괄호

def solution(s):
    answer = True
    check_count = 0
    for word in s:
        if word == "(":
            check_count += 1
        else:
            check_count -= 1
        if check_count < 0: # 닫기는 괄호가 먼저 나오는 경우는 올바르지 못한 것
            answer = False
            break
    if answer and check_count != 0: # 처리되지 않은 열린 괄호가 있을 경우 올바르지 못한 것
        answer = False

    return answer