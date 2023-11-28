# 점 개수 세기

node_cnt, query_cnt = tuple(map(int, input().split()))
node_list = []

for _ in range(node_cnt):
    x, y = tuple(map(int, input().split()))
    node_list.append((x,y))

for _ in range(query_cnt):
    result = 0
    start_x, start_y, end_x, end_y = tuple(map(int, input().split()))
    move_x, move_y = (0 - start_x), (0 - start_y)
    max_x, max_y = end_x + move_x, end_y + move_y
    for node in node_list:
        x, y = node
        x, y = move_x + x, move_y + y
        if (0 <= x <= max_x and 0 <= y <= max_y):
            result += 1
    print(result)
