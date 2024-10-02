# 퍼즐 조각 채우기
## Level 3


from collections import deque

move_row = [0,+1,0,-1]
move_col = [+1,0,-1,0]

    
def rotate(nodes):
    for idx in range(1,len(nodes)):
        row, col = nodes[idx]
        nodes[idx] = (-col, row)
    return nodes
    
def table_bfs(row, col, graph):
    temp = deque([(row,col)])
    graph[row][col] = 0
    nodes = [(0,0)]
    while temp:
        r,c  = temp.popleft()
    for m_idx in range(4):
        now_r, now_c = r + move_row[m_idx], c + move_col[m_idx]
        if 0 <= now_r < len(graph) and 0 <= now_c < len(graph):
            if graph[now_r][now_c] == 1:
                graph[now_r][now_c] = 0
                temp.append((now_r, now_c))
                nodes.append((now_r - r, now_c - c))
    
    return nodes

def make_count_board(graph):
    cnt_dict = {}
    visited_board = [[False for _ in range(len(graph))] for _ in range(len(graph))]
    for row in range(len(graph)):
        for col in range(len(graph)):
            if graph[row][col] == 0 and not visited_board[row][col]:
                visited_board[row][col] = True
                temp = deque([(row, col)])
                count = 1
                while temp:
                    r, c = temp.popleft()
                    for idx in range(4):
                        next_row, next_col = r + move_row[idx], c + move_col[idx]
                        if 0 <= next_row < len(graph) and 0 <= next_col < len(graph):
                            if graph[next_row][next_col] == 0 and not visited_board[next_row][next_col]: 
                                visited_board[next_row][next_col] = True
                                count += 1
                                temp.append((next_row, next_col))
                cnt_dict[(row,col)] = count
    return cnt_dict

def board_bfs(nodes, row, col, graph, cnt_graph):
    point = 0
    if len(nodes) != cnt_graph[(row,col)]:
        point = -1
    else:
        isEnd = True
        for idx in range(1, len(nodes)):
            now_row, now_col = row + nodes[idx][0], col + nodes[idx][1]
            if 0 <= now_row < len(graph) and 0 <= now_col < len(graph):
                if graph[now_row][now_col] != 0:
                    isEnd = False
                    break
        if isEnd:
            for idx in range(1, len(nodes)):
                now_row, now_col = row + nodes[idx][0], col + nodes[idx][1]
                if 0 <= now_row < len(graph) and 0 <= now_col < len(graph):
                    graph[now_row][now_col]  = 1
        point = cnt_graph[(row,col)]
    return point

def solution(game_board, table):
    answer = -1
    visited_table = [[False for _ in range(len(table))] for _ in range(len(table))]
    visited_board = [[False for _ in range(len(table))] for _ in range(len(table))]
    
    board_cnt = make_count_board(game_board)
    
    for table_row in range(len(table)):
        for table_col in range(len(table)):
            if table[table_row][table_col] == 1:
                now_nodes = table_bfs(table_row, table_col, table)
                for board_row in range(len(game_board)):
                    for board_col in range(len(game_board)):
                        if (board_row, board_col) in board_cnt and game_board[board_row][board_col] == 0:
                            for _ in range(4):
                                temp_end = board_bfs(now_nodes, board_row, board_col, game_board, board_cnt)
                                if temp_end == -1:
                                    break
                                elif temp_end != 0:
                                    answer += temp_end
                                else:
                                    rotate(now_nodes)
                            
    
    
    
    return answer