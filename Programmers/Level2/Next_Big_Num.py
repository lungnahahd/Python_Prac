# 다음 큰 숫자

def solution(n):
    answer = 0
    bin_n = bin(n)[2:] # 주어진 수를 이진수로 변환
    if bin_n.count('1') == len(bin_n): # 1의 개수가 꽉 찬 경우(1 이동 불가)
        bin_n = bin_n[0] + '0' + bin_n[1:]
    else: # 1이 이동 가능한 경우
        next_n = n
        while True:
            next_n += 1
            bin_next_n = bin(next_n)[2:]
            if bin_n.count('1') == bin_next_n.count('1'):
                bin_n = bin_next_n
                break
            
    answer = int(bin_n,2)
    return answer