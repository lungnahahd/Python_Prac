# H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    cite_len = len(citations)
    for idx in range(cite_len):
        paper = citations[idx]
        if paper-1 <= idx and (cite_len-idx-1) <= paper:
            return paper