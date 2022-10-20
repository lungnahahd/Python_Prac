# 멀쩡한 사각형
import math 

def solution(w,h):
    answer = 1
    if w == 1 or h == 1: # 가로 혹은 세로가 1로 주어진 경우, 대각선을 그으면 멀쩡한 정사각형이 없으므로 해당 경우는 0을 반환
        answer = 0
    elif w == h: # 가로와 세로가 같은 경우는 대각선이 정확하게 그어지므로 해당 결과를 반환
        answer = w*h - w
    else:
        temp = min(w,h)
        gcd = 1 
        for i in range(1,temp+1):
            if w %i == 0 and h % i == 0: # 각 경우의 최대 공약수를 구하는 부분
                gcd = i

        # 대각선의 성질에 의해 세로는 반드시 한 칸만 차지한다고 생각 가능
        # 가로는 -1을 해주어야 함
        answer = int(w * h -((w/gcd) + (h/gcd) - 1)*gcd) 

    return answer














w = 8
h = 12
#print(solution(5,3))
print(solution(w,h))
print(solution(1,1))
print(solution(2,1))