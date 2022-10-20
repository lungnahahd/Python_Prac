# 문자열 압축(Level 2)
import sys
INT_MAX = sys.maxsize

def solution(s):
    answer = INT_MAX # 가장 최소의 값을 구하기 위해 초기 값은 가장 큰 숫자로 지정
    for i in range(1,len(s)): # 몇 자리를 기준으로 검사를 할지 체크하는 부분
        now = 0 # 현재 검사할 기준이 되는 시작 인덱스 
        tempCount = 0 # 현재 자리수를 기준으로 처리할 때, 중간 결과 값을 저장하는 변수
        beforeSame = False # 이전에 지금 현재의 값과 동일했는지 여부를 판별해주는 변수
        end = False # 중간에 길이가 미치지 못하는 경우 이를 판별해주는 변수
        howmany = 1 # 몇 개가 이전에 겹쳤는지 카운트 해주는 변수
        while now <= len(s)-i: # 각 자리수를 기준으로 끝까지 반복문 
            sameCheck = True # 현재 자리와 비교하는 문자열이 같은지를 판단하는 변수
            for j in range(i):
                if now+j+i >= len(s): # 배열의 길이가 더 이상 없다면 멈추기 -> outofIndex 막기
                    end = True
                    break
                if s[now+j] != s[now+j+i]: # 반복문 중간에 다른 부분이 있다면 바로 멈추기
                    sameCheck = False
                    break
            if end: # 만약 배열 길이가 걸렸다면 바로 반복문을 멈추기
                break
            if sameCheck:  # 문자열이 일치한 경우
                howmany += 1
                if not beforeSame:
                    beforeSame = True
                    tempCount += i
            else: # 문자열이 일치하지 않은 경우
                if beforeSame:
                    if howmany > 99:
                        tempCount += 3
                    elif howmany > 9:
                        tempCount += 2
                    else:
                        tempCount += 1
                    beforeSame = False
                else:
                    tempCount += i
                howmany = 1 
            now += i
        if now != len(s)-i: # 길이가 미치지 못한 경우 처리하는 부분
            if beforeSame:
                if howmany > 99:
                    tempCount += 3
                elif howmany > 9:
                    tempCount += 2
                else:
                    tempCount += 1
                tempCount += (len(s) - (now +i))
            else:
                tempCount += ( len(s)-now)
        else: # 끝까지 다 돈 경우 처리
            if beforeSame:
                if howmany > 99:
                    tempCount += 3
                elif howmany > 9:
                    tempCount += 2
                else:
                    tempCount += 1
            else:
                tempCount += i

        answer = min(answer, tempCount)
    if answer == INT_MAX: # 문자열의 자리수가 한 자리인 경우 예외 처리
        answer = 1
    return answer


#sample = "aabbaccc"
sample = "a"
#sample = "abcabcdede"
#sample = "xababcdcdababcdcd"
#sample = "acdhdh"
print(solution(sample))