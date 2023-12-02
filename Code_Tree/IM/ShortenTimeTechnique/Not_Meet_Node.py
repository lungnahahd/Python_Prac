import heapq

node_cnt = int(input())
temp, sort_line = [], []
in_node = set()
not_finish_line = []
finish = [True for _ in range(node_cnt)]

for _ in range(node_cnt):
    x,y = tuple(map(int, input().split()))
    heapq.heappush(temp, (x,y))

sort_cnt = 0
while temp:
    x,y = heapq.heappop(temp)
    heapq.heappush(sort_line, (x,sort_cnt))
    heapq.heappush(sort_line, (y,sort_cnt))
    heapq.heappush(not_finish_line, sort_cnt)
    sort_cnt += 1

answer = 0
while sort_line:
    node, line = heapq.heappop(sort_line)
    if line not in in_node:
        in_node.add(line)
    elif line in in_node:
        if (finish[line]):
            if (not_finish_line[0] == line):
                heapq.heappop(not_finish_line)
                answer += 1
            else:
                while True:
                    now_node = heapq.heappop(not_finish_line)
                    finish[now_node] = False
                    if (now_node == line):
                        break
print(answer)
