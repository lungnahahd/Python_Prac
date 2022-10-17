# 피보나치 수열

def solution(n):
    answer = 0
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    



    answer = fib[n] % 1234567
    return answer

print(solution(3)) # 2
print(solution(5)) # 5