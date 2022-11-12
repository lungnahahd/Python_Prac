from collections import deque

sockets = [[2, 3, -1, -1, -1], [4, 0, -1, -1, 6], [5, 0, 0, 0, 0],
           [-1, 0, 0, 0, 0], [-1, -1, -1, -1, -1], [-1, -1, 0, 0, 0]]
limits = [2000, 1000, 3000, 200, 600, 500]
k = 300

start = deque()
mother = [0, 0, 0, 0, 0, 0]

for idx, socket in enumerate(sockets):
    no_mother = True
    for plug in socket:
        if plug != 0 and plug != -1:
            no_mother = False
            mother[plug-1] = idx
    if no_mother:
        mother[idx] = idx
        start.append(idx)

while start:
    now_socket = start.popleft()
    if sum(sockets[now_socket]) > limits[now_socket]:
        can_out = sockets[now_socket].count(-1)
        need_out = limits[now_socket] - sum(sockets[now_socket])


print(mother)
print(start.popleft())
