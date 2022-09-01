# 원형 순열에서의 인원 제거
import heapq

cnt, where = map(int,input().split())

queue = [i for i in range(cnt)]

now = 1
result = ""
while queue:
    temp = queue.pop(0)
    #print(queue)
    if now == where:
        result += str(temp+1)
        result += " "
        now = 1
    else:
        queue.append(temp)
        now += 1
print(result)