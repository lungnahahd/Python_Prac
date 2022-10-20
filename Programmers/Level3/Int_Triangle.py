# 정수 삼각형
## DP 유형


def solution(triangle):
    answer = 0
    before_layer = [0]
    for layer in triangle:
        b_size = len(before_layer)
        for idx,num in enumerate(layer):
            temp = 0
            if 0 <= idx -1 < b_size:
                temp = num + before_layer[idx-1]
            if idx + 1 =< b_size:
                temp = max(temp,num + before_layer[idx+1])
            layer[idx] = temp
        before_layer = layer
    print(triangle)
    
    
    
    return answer