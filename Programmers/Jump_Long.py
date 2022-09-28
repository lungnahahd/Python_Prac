# 멀리 뛰기

dist = []
answer = 0

def solution(n):
    global answer

    for i in range(1,3):
        n = n - i
        if n == 0:
            answer += 1
            break
        else:
            solution(n)
        n = n + i
    return answer


print(solution(4)) # 5
print(solution(3)) # 3