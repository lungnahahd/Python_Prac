# 멀쩡한 사각형

def solution(w,h):
    answer = 1
    if w == 1 or h == 1: # 가로 혹은 세로가 1로 주어진 경우, 대각선을 그으면 멀쩡한 정사각형이 없으므로 해당 경우는 0을 반환
        answer = 0
    elif w == h: # 가로와 세로가 같은 경우는 대각선이 정확하게 그어지므로 해당 결과를 반환
        answer = w*h - w
    else:
        temp = min(w,h)
        answer = w*h - 2*temp


    return answer














w = 8
h = 12
print(solution(w,h))