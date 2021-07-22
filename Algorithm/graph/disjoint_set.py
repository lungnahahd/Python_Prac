 서로소 집합 알고리즘
# 부모 노드를 나타내는 리스트를 생성하고 합집합 연산으로 같은 집합끼리 부모 노드를 조정해주기
# 조정된 부모 노드를 이용해서 서로 같은 집한인지 아닌지를 찾는 그래프를 이용한 서로소 집합 알고리즘
# 처음에는 노드와 선의 갯수를 입력 받고 차례대로 어떤 노드와 연결되어 있는지 입력 받기

node, line = input().split()
node = int(node)
line = int(line)

paraent = [ i for i in range(node+1)]

def FindMother(a) :
    if paraent[a] == a:
        return a
    else:
        return FindMother(paraent[a])

def SumFunc(a, b):
    if FindMother(a) == FindMother(b):
        return
    elif FindMother(a) > FindMother(b):
        paraent[a] = FindMother(b)
    elif FindMother(a) < FindMother(b):
        paraent[b] = FindMother(a)

for i in range(1, line+1):
    start,end = input().split()
    start = int(start)
    end = int(end)
    SumFunc(start,end)

finalmother = []
finalmother.append(0)

for i in range(1, len(paraent)):
    finalmother.append(FindMother(i))

# 부모를 찾는 부분
for i in range(1, len(paraent)):
    print(paraent[i], end=' ')
print('\n')
# 같은 그룹에 속하는지 확인하는 부분
for i in range(1, len(paraent)):
    print(finalmother[i],end=' ')