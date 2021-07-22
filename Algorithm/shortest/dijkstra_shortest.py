# 다익스트라 최단 경로 알고리즘
# 한 지점에서 다른 지점까지 도달하는 가장 짧은 경로를 찾는 문제
# 한 노드에서 다른 모든 노드로 가는 모든 최단 경로를 구하는 알고리즘
# 매 상황에서 가장 좋은 경로를 선택하는 그리디 알고리즘의 일종

### 딕셔너리 처리에 조금은 어려움 -> 파이썬 타입에 대해 정확히 인지하고 정확히 사용하기!



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
        if distance[keyvalue] > distance[check] + data_graph[check][keyvalue]:
            distance[keyvalue] = distance[check] + data_graph[check][keyvalue]
        # sorted(distance.items()) # 이건 key를 기준으로 정렬 방법
        sortdistance = sorted(distance.items(),key=lambda x:x[1])
        distance = dict((x,y) for x, y in sortdistance)
        count = 0
        for key, value in distance.items():
            if gocheck[key]:
                gocheck[key] = False
                savelist.append(key)
print(distance)