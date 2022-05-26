# 괄호 변환


def solution(p):
    answer = ''
    p_list = list(p)
    if len(p_list) == 0:
        return answer
    else:
        count_arr = 0
        check = True
        for i in range(len(p_list)):
            if p_list[i] == "(": 
                count_arr +=1
            else:
                count_arr -= 1
            if count_arr < 0: # 문자열이 올바른 문자열인지 여부를 파악하는 부분
                check = False 
            if count_arr == 0: # 문자열이 균형잡힌 문자열인지 여부를 파악하는 부분
                u = p_list[:i+1]
                v = p_list[i+1:]
                if check:
                    answer = ''.join(map(str,u)) + solution(v)
                    return answer
                else:
                    answer = "(" + solution(v) + ")" + change(u)
                    return answer
        

def change(p): 
    p = p[1:-1]
    chanage_p = ""
    for i in p:
        if i == "(":
            chanage_p += ")"
        else:
            chanage_p += "("
    return chanage_p


p = "(()())()"
#p = ")("
#p = "()))((()"
#p = "))((()"
print(solution(p))