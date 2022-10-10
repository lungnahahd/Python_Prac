# 카펫

import math


def solution(brown, yellow):
    answer = []
    tile_size = brown + yellow
    posible = []
    
    # 카펫 타일의 전체 갯수의 약수 구하기
    for num in range(1,int(math.sqrt(tile_size)) + 1):
        if tile_size % num == 0:
            posible.append(num)

    # 약수를 기준으로 부합하는 카펫 찾기
    for num in posible:
        row = tile_size / num
        col = num
        if (row-2) * (col-2) == yellow: # 카펫을 찾은 경우 break
            answer.append(row)
            answer.append(col)
            break
    
    
    return answer

print(int(math.sqrt(24)))