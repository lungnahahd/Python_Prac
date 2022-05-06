# 메뉴 리뉴얼

def solution(orders, course):
    answer = []
    nowSize = course[0]
    nowMenu = 0
    checkWord = [[] for _ in range(26)]
    for j in range(len(orders)): # 26개의 메뉴판에 한 명씩 자신의 메뉴를 체크해서 넣어놓는 과정
        for i in range(len(orders[j])):
            temp = ord(orders[j][i]) - 65
            checkWord[temp].append(j)
        
    for i in range(26):    
        
    
    
    
    
    
    return answer