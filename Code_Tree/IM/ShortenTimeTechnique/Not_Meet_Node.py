import heapq

node_cnt = int(input())
node_check = [True for _ in range(node_cnt)]
node_in_line = set()
node_out = []
line_list = []
top = -1
temp, answer = 0,0

for idx in range(node_cnt):
    x, y = tuple(map(int, input().split()))
    heapq.heappush(line_list, (x,-1,idx))
    heapq.heappush(line_list, (y,+1,idx))
    heapq.heappush(node_out, idx)

while (line_list):
    node, val, line = heapq.heappop(line_list)
    temp += val
    if(val == +1):
        node_in_line.remove(line)
        if (temp <= 0 and node_out[0] == line):
            answer += 1
            print(node)
            print(line)
            
            heapq.heappop(node_out)
            print(node_out)
            print("------")

        else:
            node_check[line] = False
            node_out.remove(line)
            for in_node in node_in_line:
                node_check[in_node] = False
    else:
        node_in_line.add(line)

print(answer)
