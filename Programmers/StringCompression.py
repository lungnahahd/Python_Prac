# 문자열 압축(Level 2)
import sys
INT_MAX = sys.maxsize

def solution(s):
    answer = INT_MAX
    for i in range(1,len(s)):
        now = 0
        tempCount = 0
        beforeSame = False
        end = False
        howmany = 1
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
                howmany += 1
                if not beforeSame:
                    beforeSame = True
                    tempCount += i
            else:
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
        if now != len(s)-i:
            if beforeSame:
                if howmany > 99:
                    tempCount += 3
                elif howmany > 9:
                    tempCount += 2
                else:
                    tempCount += 1
                tempCount += (len(s) - (now +i))
            else:
                tempCount += (len(s)-now)
        else:
            #print("hi")
        #if not end:
            if beforeSame:
                if howmany > 99:
                    tempCount += 3
                elif howmany > 9:
                    tempCount += 2
                else:
                    tempCount += 1
                #tempCount += 1
            else:
                tempCount += i
        #print(tempCount)
        answer = min(answer, tempCount)

    return answer


sample = "aabbaccc"
#sample = "abcabcdede"
#sample = "xababcdcdababcdcd"
#sample = "acdhdh"
print(solution(sample))