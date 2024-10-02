# 단어 변환
## Level 3

from collections import deque

def check_word(a_word, b_word):
    diff_cnt = 0
    for idx in range(len(a_word)):
        if a_word[idx] != b_word[idx]:
            diff_cnt += 1
            if diff_cnt > 1:
                return False
    if diff_cnt != 1:
        return False
    
    return True


def solution(begin, target, words):
    answer = 0
    
    visited = set()
    temp = deque([(begin, 0)])
    
    while temp:
        now_w, mid_cnt = temp.popleft() 
        
        for idx in range(len(words)):
            if idx not in visited:
                if check_word(now_w, words[idx]):
                    if words[idx] == target:
                        answer = mid_cnt + 1
                        break
                    temp.append((words[idx], mid_cnt+1))
                    visited.add(idx)
    
    return answer