# 서로소 집합 알고리즘
# 부모 노드를 나타내는 리스트를 생성하고 합집합 연산으로 같은 집합끼리 부모 노드를 조정해주기
# 조정된 부모 노드를 이용해서 서로 같은 집한인지 아닌지를 찾는 그래프를 이용한 서로소 집합 알고리즘
# 처음에는 노드와 선의 갯수를 입력 받고 차례대로 어떤 노드와 연결되어 있는지 입력 받기

node, line = input().split()
node = int(node)
line = int(line)

paraent = [ i for i in range(node+1)]


for i in range(line):
    start, end = input().split()
    start = int(start)
    end = int(end)
    if paraent[end] > paraent[start]:
        paraent[end] = paraent[start]
    elif paraent[start] > paraent[end]:
        paraent[start] = paraent[end]

def findparant(value):
    if value == paraent[value]:
        return value
    else :
        return findparant(paraent[value])

for i in range(1, node + 1):
    paraent[i] = findparant(i)

print(paraent)