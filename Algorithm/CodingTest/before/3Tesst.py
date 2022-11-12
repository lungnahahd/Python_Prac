
import heapq
import sys  

INT_MAX = sys.maxsize
save = []
def solution(n, edges):
    global save
    answer = 0
    count = [0 for _ in range(n)]
    edges.sort()
    start= []
    end = []
    for i in edges:
        start.append(i[0])
        end.append(i[1])
    for i in range(n-1):
        if end[i] in start:
            if count[end[i]] == 0:
                count[end[i]] = start.count(end[i])
            answer += count[end[i]]
        if start[i] in start:
            if count[start[i]] == 0:
                count[start[i]] = start.count(start[i]) - 1
            answer += count[start[i]]        
    print(count)
    answer = answer*2


    return answer

print(solution(5,[[0,1],[0,2],[1,3],[1,4]]))
print(solution(4,[[0,1],[1,2],[2,3]]))
    # answer = 0
    # return answer