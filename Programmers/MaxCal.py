# 수식 최대화

## eval()
### 파이썬 내장함수로 문자열로 주어진 것을 파이썬 코드로 실행할 수 있도록 도와줌

## a.insert(인덱스, 값)
### a 리스트의 인덱스에 값을 추가

## abs()
### 안에 숫자를 넣고, 이를 절대값으로 만들어주는 함수


import tempfile


def solution(expression):
    answer = 0
    priority_arr = [['*','+','-'],['*','-','+'],['+','-','*'],['+','-','*'],['-','+','*'],['-','*','+']] # 각 연산자의 우선순위를 지정해주는 변수
    temp_list = list(expression)
    exp_list = []
    temp_num = ''
    for i in temp_list:
        if i == "+" or i == "-" or i == "*":
            exp_list.append(temp_num)
            exp_list.append(i)
            temp_num = ''
        else:
            temp_num += i
    exp_list.append(temp_num)
    print(exp_list)
    for strong in priority_arr:
        temp = exp_list[:] # 기존 수식에 괄호를 추가할 배열
        count = 0 # 현재 우선순위 연산자를 위한 변수
        where = 0 # 수식을 돌면서 현재 위치를 저장할 변수
        realcount = 0
        while True:
            #print(temp,strong[count])
            if realcount == len(exp_list):
                if count != 2:
                    count += 1
                    realcount = 0
                    where = 0
                else:  
                    break
            if temp[where] == strong[count]:
                if where+2 >= len(temp) or temp[where+1] != "(":
                    temp.insert(where+2,")")
                else:
                    idx = where+1
                    while True:
                        if temp[idx] == ")":
                            temp.insert(idx+1,")")
                            break
                        idx += 1
                if where-2 < 0 or temp[where-1] != ")":
                    idx = where-1
                    if idx < 0:
                        idx = 0
                    temp.insert(idx,"(")
                else:
                    idx = where-1
                    while True:
                        if temp[idx] =="(":
                            if idx < 0:
                                idx = 0
                            temp.insert(idx-1,"(")
                            break
                        idx -= 1
                where += 1
                realcount += 1
            else:
                if temp[where] != "(" and temp[where] != ")":
                    realcount += 1
                where += 1
            
        result = ''.join(map(str,temp))
        answer = max(answer,abs(eval(result))) # 수식의 최대화를 구하고 저장
        if answer == 594:
            print(result,strong[count])


    return answer







#a = "100-200*300-500+20"
#a = "10+2-3"
a = "50*6-3*2"
print(solution(a))