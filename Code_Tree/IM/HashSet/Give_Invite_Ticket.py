people, group = list(map(int, input().split()))

people_content = [[] for _ in range(people+1)]
group_content = [[] for _ in range(group)]
sizes = [0 for _ in range(group)]
answer = 1

for idx in range(group):
    now_group = list(map(int, input().split()))
    sizes[idx] = now_group[0]
    group_content[idx] = now_group[1:]
    for member in range(1, now_group[0]+1):
        people_content[now_group[member]].append(idx)

ticket_queue = []
ticket_queue.append(1)

while (ticket_queue):
    now_member = ticket_queue.pop()
    for next_group in people_content[now_member]:
        if(sizes[next_group] == 0):
            continue
        sizes[next_group] -= 1
        group_content[next_group].remove(now_member)
        if(sizes[next_group] == 1):
            answer += 1
            sizes[next_group] -= 1
            ticket_queue.append(group_content[next_group].pop())
            continue
        
        

print(answer)
