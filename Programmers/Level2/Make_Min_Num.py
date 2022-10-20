# 최소값 만들기
# 리스트가 주어졌을 때, 각각 하나씩 중복을 허용하지 않고 값을 꺼내서 곱의 크기를 확인

def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for idx in range(len(A)):
        answer += (A[idx] * B[len(B)-1-idx])

    return answer

a1 = [1,4,2]
b1 = [5,4,4]
a2 = [1,2]
b2 = [3,4]

print(solution(a1,b1))
print(solution(a2,b2))