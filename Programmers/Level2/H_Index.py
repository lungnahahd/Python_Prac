# H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    cite_len = len(citations)
    before_paper = citations[0]
    for idx in range(cite_len):
        paper = citations[idx]
        blank = before_paper - paper
        if blank > 0: # 중간 논문 개수를 처리하기 위한 조건 -> 반복문으로 중간이 없으면 지나감
            for minus in range(1,blank):
                temp = before_paper - minus
                if temp <= idx:
                    answer = max(temp,answer)
        if paper <= idx+1:
            answer = max(paper,answer)
        before_paper = paper
    blank = before_paper 
    # 마지막까지 나오지 않는 경우 처리
    ## [3,3] 같은 경우
    if blank > 0:
        for minus in range(1,blank):
            temp = before_paper - minus
            if temp <= cite_len:
                answer = max(temp,answer)
    return answer