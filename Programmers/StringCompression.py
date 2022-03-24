# 문자열 압축(Level 2)
from random import sample
import sys
INT_MAX = sys.maxsize

def solution(s):
    answer = INT_MAX
    for i in range(1,len(s)):
        now = 0
        tempCount = 0
        beforeSame = False
        end = False
        while now <= len(s)-i:
            sameCheck = True
            for j in range(i):
                if now+j+i >= len(s):
                    end = True
                    break
                if s[now+j] != s[now+j+i]:
                    sameCheck = False
                    break
            if end:
                break
            if sameCheck:
                if not beforeSame:
                    beforeSame = True
                    tempCount += i
            else:
                if beforeSame:
                    tempCount += 1
                    beforeSame = False
                else:
                    tempCount += i
            now += i
        if now != len(s)-i:
            if beforeSame:
                tempCount += (len(s) - (now +i))
            else:
                tempCount += (len(s)-now)
        else:
            #print("hi")
        #if not end:
            if beforeSame:
                tempCount += 1
            else:
                tempCount += i
        #print(tempCount)
        answer = min(answer, tempCount)

    return answer


#sample = "aabbaccc"
#sample = "abcabcdede"
#sample = "xababcdcdababcdcd"
sample = "abcd"
print(solution(sample))