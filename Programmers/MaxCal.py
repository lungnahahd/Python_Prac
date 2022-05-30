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
    arr_count = 0 # 연산자가 몇개 있는지 카운트하는 변수
    arr_check = [False,False,False] # 연산자가 어떤 것이 수식에 있는지 기록하는 리스트
    # 수식에서 숫자와 연산자를 구분해서 저장하는 코드
    for i in temp_list:
        if i == "+" or i == "-" or i == "*":
            exp_list.append(temp_num)
            exp_list.append(i)
            temp_num = ''
            # 주어진 수식에 연산자의 개수를 카운트
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
    if arr_count == 1: # 연산자의 개수가 하나인 경우는 단순 계산으로 빠르게 마무리
        last = ''.join(map(str,exp_list))
        answer = max(answer,abs(eval(last)))
    else: # 연산자의 개수가 두개 이상인 경우는 아래의 코드 이용(전체 반복 진행)
        for now_cal in priority_arr:
            count = 0 # 현재 몇 번째 연산자를 이용했는지를 기록할 변수
            max_len = len(exp_list) # 각 수식의 최대 길이를 저장할 변수
            temp_one = [] # 첫 번째 연산자를 이용한 뒤에 나오는 수식 저장 리스트
            temp_second = [] # 두 번째 연산자를 이용한 뒤에 나오는 수식 저장 리스트
            idx = 0 # 현재 수식에서 앞으로 나아가면서 위치를 기록하는 변수
            check_num = True # 앞에서 동일한 연산자로 계산을 했다면 해당 숫자도 바로 다음 계산에 사용되므로 이를 이용하기 위한 변수
            while True:
                if idx == max_len-1:
                    if count != 1 : # 연산자를 한 번만 사용한 경우
                        count += 1
                        idx = 0
                        if check_num:
                            temp_one.append(exp_list[-1])
                        check_num = True
                        max_len = len(temp_one)
                    else: # 연산자를 두번 사용한 경우
                        if check_num:
                            temp_second.append(temp_one[-1])
                        break
                if count == 0: # 처음 연산자 사용
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
                else: # 두 번째 연산자 사용
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