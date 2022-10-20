# 정수 삼각형
## DP 유형


import copy

def solution(triangle):
    answer = 0
    before_layer = [0]
    sum_tri = copy.deepcopy(triangle)
    for idx in range(len(triangle)-1):
        layer = sum_tri[idx]
        for i, num in enumerate(layer):
            sum_tri[idx+1][i] = max(sum_tri[idx+1][i],num + triangle[idx+1][i])
            sum_tri[idx+1][i+1] = max(sum_tri[idx+1][i+1], num + triangle[idx+1][i+1])  
            
    answer = max(sum_tri[-1])
    
    return answer