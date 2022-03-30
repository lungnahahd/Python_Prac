# 124 나라의 숫자(Level 2)

s = int(input())

def solution(n):
    answer = ''
    numArr = [4,1,2,4]
    change = False
    if n % 3 == 0:
        n = n-1
        change = True
    
    temp = n//3
    
    if temp >= 3: # 몫이 3보다 크면 추가적인 작업이 필요하므로 재귀함수로 들어가기
        answer = solution(temp) # 재귀 함수로 각 경우를 나누어서 처리하기
    elif temp != 0: # 더 이상 재귀함수로 진행되지 않고, 몫이 0이 아닌 경우, 자리수를 처리하는 부분
        answer = str(numArr[temp]) 
    
    n = n % 3 # 나머지로 마지막 자리수를 처리
    answer = answer + str(numArr[n])

    if change: # 3으로 딱 나누어 떨어지는 경우 하나 작게 처리해서 나머지를 이용하는 것을 편하게 하기
        answer = list(answer)
        answer[-1] = '4'
        answer = ''.join(answer)

    return answer


print(solution(s))