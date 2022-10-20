# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    big_word = True
    for word in s:
        if big_word and word != " ":
            if 65<=ord(word)<=90 or 97<=ord(word)<=122:
                answer += word.upper()
            else:
                answer += word
            big_word = False
            continue
        if word == " ":
            answer += " "
            big_word = True
            continue
        answer += word.lower()
    return answer