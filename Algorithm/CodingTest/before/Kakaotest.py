# villageMap = [[] for _ in range(10)]
# visited = [[False for _ in range(10)] for _ in range(10)]

# # for idx in range(10):
# #     p = list(map(str,input()))
# #     villageMap[idx] = p

# start = []
# end = []
# startLine = -1
# endLine = -1
# for x in range(10):
#     p = list(map(str,input()))
#     for y,val in enumerate(p):
#         if val == "H" or val == "M":
#             if startLine < 0:
#                 startLine = x 
#                 start.append(x)
#                 start.append(y)
#             else:
#                 endLine = x
#                 end.append(x)
#                 end.append(y)
#         villageMap[x].append(val)
# ####################################################
# from collections import deque

# goX = [1,0,0,-1]
# goY = [0,-1,1,0]

# def cutTree(graph,start,end,visited):
#     shortCount = 0
#     save = deque([(start[0],start[1],shortCount)])
#     visited[start[0]][start[1]]
#     while save:
#         bx,by,cost = save.popleft()
#         for idx in range(4):
#             x,y = bx+goX[idx], by+goY[idx]
#             if 0 <= x <10 and 0 <= y < 10 and not visited[x][y] and graph[x][y] != "R":
#                 if x == end[0] and y == end[1]:
#                     return cost
#                 visited[x][y] = True
#                 save.append((x,y,cost+1))





# print(cutTree(villageMap,start,end,visited))




