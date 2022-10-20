# 최대값과 최솟값 
## 숫자로 이루어진 문자열에서 최대와 최솟값을 찾아서 한 줄로 출력하는 문제


def solution(s):
    answer = ''
    num_list = list(map(int,s.split(' ')))
    min_num = min(num_list)
    max_num = max(num_list)

    answer += str(min_num)
    answer += " "
    answer += str(max_num)
    return answer

s = "1 2 3 4"
s2 = "-1 -2 -3 -4"

print(solution(s))
print(solution(s2))