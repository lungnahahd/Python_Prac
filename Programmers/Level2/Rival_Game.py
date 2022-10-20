# 예상 대진표
## 대진표에 대한 정보와 라이벌의 정보가 주어지면 몇 번만에 라이벌을 만나는 가에 대해 출력하는 프로그램

def solution(n,a,b):
    answer = 0
    meet_friend = False
    while not meet_friend:
        if abs(b-a) == 1:
            if (max(a,b) % 2) == 0:
                meet_friend = True
        if a % 2 == 0:
            a = a / 2
        else:
            a = int(a/2) + 1
        if b % 2 == 0:
            b = b / 2
        else:
            b = int(b/2) + 1
        answer += 1
    return answer


n = 8
a = 4
b = 7
print(solution(n,a,b))