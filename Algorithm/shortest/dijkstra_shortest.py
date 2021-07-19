# 다익스트라 최단 경로 알고리즘
# 한 지점에서 다른 지점까지 도달하는 가장 짧은 경로를 찾는 문제
# 한 노드에서 다른 모든 노드로 가는 모든 최단 경로를 구하는 알고리즘
# 매 상황에서 가장 좋은 경로를 선택하는 그리디 알고리즘의 일종

distance ={
    'A' : 10000,
    'B' : 10000,
    'C' : 10000,
    'D' : 10000,
    'E' : 10000,
}
key = ['A','B','C','D','E']

distancelist = [10000 for i in range(5)]
distance['A'] = 0
savelist = []
savelist.append(key[0])
#savelist.append(distancelist[0])

gocheck = {
    'A' : True,
    'B' : True,
    'C' : True,
    'D' : True,
    'E' : True,
}

data_graph = {
    'A' : {'B' : 10, 'C' : 3},
    'B' : {'C' : 1, 'D' : 2},
    'C' : {'B' : 4, 'D': 8, 'E': 2},
    'D' : {'E': 7},
    'E' : {'D' : 9},
}

while len(savelist) != 0:
    check = savelist.pop()
    for keyvalue in data_graph[check]:
        #print(keyvalue)
        if distance[keyvalue] > distance[check] + data_graph[check][keyvalue]:
            distance[keyvalue] = distance[check] + data_graph[check][keyvalue]
        sorted(distance.items())
        okay = True
        count = 0
        while okay :
            if  gocheck[list(distance.keys())[count]]:
                savelist.append(list(distance.keys())[count])
                okay = False
            else:
                count += 1
        
print(distance)

#print(data_graph[key[check]][keyvalue]) # 값 출력