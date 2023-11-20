# 초대장과 번호표
people, group = list(map(int, input().split()))

people_content = [set() for _ in range(people+1)]
group_content = [set() for _ in range(group)]
sizes = [0 for _ in range(group)]
answer = 1

for idx in range(group):
    now_group = list(map(int, input().split()))
    sizes[idx] = now_group[0]
    group_content[idx] = set(now_group[1:])
    for member in range(1, now_group[0]+1):
        people_content[now_group[member]].add(idx)

ticket_queue = set()
ticket_queue.add(1)
chk_member = [False for _ in range(1, people + 2)]
chk_member[1] = True


while (ticket_queue):
    now_member = ticket_queue.pop()
    for next_group in people_content[now_member]:
        if(sizes[next_group] == 0):
            continue
        sizes[next_group] -= 1
        group_content[next_group].remove(now_member)
        if(sizes[next_group] == 1):
            last_member = group_content[next_group].pop()
            if not chk_member[last_member]:
                answer += 1
            chk_member[last_member] = True
            sizes[next_group] -= 1
            ticket_queue.add(last_member)
            continue
            
print(answer)
