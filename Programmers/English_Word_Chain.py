# 영어 끝말 잇기

def solution(n, words):
    answer = []
    check = set() # 단어가 한 번 반복되었는지 여부를 판단하기 위한 세트
    first_word = True # 첫 단어를 체크하기 위한 변수
    people,count = 0,0
    for word in words:
        people += 1 # 사람이 지날 때마다 카운트
        if people % n == 1: # 사람의 수를 보고 현재 한 바퀴를 돌았는지 여부를 판단
            count += 1
        if first_word:
            first_word = False
        else:
            if word in check or last_word != word[0]: # 끝말잇기에서 진 경우..
                people = people % n
                if people == 0:
                    people = n
                answer.append(people)
                answer.append(count)
                break
        check.add(word)
        last_word = word[-1]
    if len(check) == len(words): # 아무도 진 사람이 없는 경우
        answer = [0,0]
    return answer