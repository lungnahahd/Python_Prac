# 멀리 뛰기

def solution(n):
    dist = [0,1,2]
    if n > 2:
        for i in range(3,n+1):
            temp = dist[i-2]+dist[i-1]
            dist.append(temp % 1234567)
    answer = dist[n]
    return answer

print(solution(4)) # 5
print(solution(3)) # 3