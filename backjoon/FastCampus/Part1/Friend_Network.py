# 친구 네트워크 (4195)

case = int(input())

# 최종 부모를 세팅하는 함수
def change_mother(set_child, group):
    for child in set_child:
        final_paranet = ''
        temp_group = []
        while True:
            if (group[child] == child):
                break
            else:
                temp_group.append(child)
                final_paranet = group[child]
                child = group[child]
        while temp_group:
            now = temp_group.pop()
            group[now] = final_paranet

# 각 노드의 부모를 찾는 과정 
def find_mother(child, group):
    if child not in group:
        group[child] = child
        return child
    else:
        if group[child] == child:
            return child
        else:
            return find_mother(group[child], group)


for _ in range(case):
    cnt_net = int(input())
    group = dict()
    set_child = set()
    answer = []
    for _ in range(cnt_net):
        left, right = input().split()
        left_parent = find_mother(left, group)
        right_parent = find_mother(right, group)
        set_child.add(left)
        set_child.add(right)
        group[right] = left_parent  
        change_mother(set_child, group)
        now_cnt = 0
        for key in group:
            if group[key] == find_mother(left, group):
                now_cnt += 1
        answer.append(now_cnt)
    for rst in answer:
        print(rst)