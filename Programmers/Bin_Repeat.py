# 이진 변환 반복

def get_rid_zero(s):
    result = ""
    count = 0
    for i in s:
        if i == '1':
            result = result + "1"
        else:
            count += 1
    print(result)
    return count, result

def solution(s):
    answer = []
    how_many = 1
    count,s_temp = get_rid_zero(s)
    if s_temp == 1:
        if s == 1:
            answer.append(0)
            answer.append(0)
        else:
            answer.append(1)
            answer.append(count)
        return answer
    s_temp = len(s_temp)
    s_temp = bin(s_temp)[2:]
    print(s_temp)
    while s_temp != '1':
        if s_temp.count('0') != 0:
            temp_count,s_temp = get_rid_zero(s_temp)
            count += temp_count
        s_temp = bin(len(s_temp))[2:]
        how_many += 1
    answer.append(how_many)
    answer.append(count)
    
    return answer