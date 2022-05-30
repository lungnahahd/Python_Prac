# 수식 최대화

## eval()
### 파이썬 내장함수로 문자열로 주어진 것을 파이썬 코드로 실행할 수 있도록 도와줌

## a.insert(인덱스, 값)
### a 리스트의 인덱스에 값을 추가

## abs()
### 안에 숫자를 넣고, 이를 절대값으로 만들어주는 함수




def solution(expression):
    answer = 0
    priority_arr = [['*','+'],['*','-'],['+','-'],['+','*'],['-','+'],['-','*']] # 각 연산자의 우선순위를 지정해주는 변수
    temp_list = list(expression)
    exp_list = []
    temp_num = ''
    arr_count = 0
    arr_check = [False,False,False]
    # 수식에서 숫자와 연산자를 구분해서 저장하는 코드
    for i in temp_list:
        if i == "+" or i == "-" or i == "*":
            exp_list.append(temp_num)
            exp_list.append(i)
            temp_num = ''
            if i == "+":
                if  not arr_check[0]:
                    arr_check[0] = True
                    arr_count += 1
            elif i == "-":
                if not arr_check[1]:
                    arr_check[1] = True
                    arr_count += 1
            else:
                if not arr_check[2]:
                    arr_check[2] = True
                    arr_count += 1
        else:
            temp_num += i
    exp_list.append(temp_num)
    if arr_count == 1:
        last = ''.join(map(str,exp_list))
        answer = max(answer,abs(eval(last)))
    else:
        for now_cal in priority_arr:
            count = 0
            max_len = len(exp_list)
            temp_one = []
            temp_second = []
            idx = 0
            check_num = True
            while True:
                if idx == max_len-1:
                    if count != 1 :
                        count += 1
                        idx = 0
                        if check_num:
                            temp_one.append(exp_list[-1])
                        check_num = True
                        max_len = len(temp_one)
                    else:
                        if check_num:
                            temp_second.append(temp_one[-1])
                        break
                if count == 0:
                    if exp_list[idx] == now_cal[count]:
                        cal = ""
                        if check_num:        
                            cal += exp_list[idx-1]
                        else:
                            out = temp_one.pop()
                            cal += out
                        cal += exp_list[idx]
                        cal += exp_list[idx+1]
                        temp_one.append(str(eval(cal)))
                        check_num = False
                    elif exp_list[idx] == "+" or exp_list[idx] == "-" or exp_list[idx] == "*":
                        if check_num:
                            temp_one.append(exp_list[idx-1])
                        temp_one.append(exp_list[idx])
                        check_num = True
                else:
                    if temp_one[idx] == now_cal[count]:
                        cal = ""
                        if check_num:
                            cal += temp_one[idx-1]
                        else:
                            out = temp_second.pop()
                            cal += out
                        cal += temp_one[idx]
                        cal += temp_one[idx+1]
                        temp_second.append(str(eval(cal)))
                        check_num = False
                    elif temp_one[idx] == "+" or temp_one[idx] == "-" or temp_one[idx] == "*":
                        if check_num:
                            temp_second.append(temp_one[idx-1])
                        temp_second.append(temp_one[idx])
                        check_num = True
                idx += 1
            last = ''.join(map(str,temp_second))
            answer = max(answer,abs(eval(last)))

    return answer







#a = "100-200*300-500+20"
a = "1-2-3"
#a = "10+2-3"
#a = "50*6-3*2"
print(solution(a))