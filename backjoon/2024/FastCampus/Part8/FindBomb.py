# 지뢰 찾기 (9082)
## 난이도 : 골드 4


case_cnt = int(input())

def change_count(idx):
    global bomb_cnt_list

    left, right = idx - 1, idx + 1
    if 0 <= left < map_size and not visited[left]:
        bomb_cnt_list[left] -= 1
    if 0 <= right < map_size and not visited[right]:
        bomb_cnt_list[right] -= 1

def set_bomb(idx):
    global bomb_cnt_list, now_state_list

    left, right = idx - 1, idx + 1
    if 0 <= left < map_size:
        now_state_list[left] = '*'
        bomb_cnt_list[left] -= 2
    if 0 <= right < map_size:
        now_state_list[right] = '*'
        bomb_cnt_list[right] -= 2


for _ in range(case_cnt):
    map_size = int(input())
    bomb_cnt_list = list(map(int,input()))
    now_state_list = list(input())
    visited = [False for _ in range(map_size)]
    visited_cnt = 0
    while visited_cnt < map_size:
        for location in range(map_size):
            if not visited[location]:
                if now_state_list[location] == "*":
                    bomb_cnt_list[location] -= 1
                    visited[location] = True
                    visited_cnt += 1
                    change_count(location)
                    break
                elif bomb_cnt_list[location] == 3:
                    now_state_list[location] = "*"
                    bomb_cnt_list[location] -= 3
                    visited[location] = True
                    visited_cnt += 1
                    set_bomb(location)
                    break

    print(bomb_cnt_list)