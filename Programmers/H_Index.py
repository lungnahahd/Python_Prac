# H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    save_many = dict()
    for idx,cite in enumerate(citations):
        save_many[cite] = idx+1
    cite_len = len(citations)
    print(save_many)
    before_paper = citations[0]
    for idx in range(cite_len):
        paper = citations[idx]
        blank = before_paper - paper
        if blank > 0:
            for minus in range(1,blank):
                temp = before_paper - minus
                if temp <= idx:
                    answer = max(temp,answer)
        if paper <= idx+1:
            answer = max(paper,answer)
        before_paper = paper
    return answer