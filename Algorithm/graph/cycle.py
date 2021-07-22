# 서로소 알고리즘을 활용한 사이클 형성 여부 확인 알고리즘
# 노드와 간선을 입력해주는데, 간선 입력 중에 사이클이 확인되면 중간에 동작을 멈추는 알고리즘

node, line = input().split()
node = int(node)
line = int(line)
# 사이클 형성 여부를 확인하는 bool type 변수
cycle = False

paraent = [ i for i in range(node+1)]

def FindMother(a) :
    if paraent[a] == a:
        return a
    else:
        return FindMother(paraent[a])

def SumFunc(a, b):
    global cycle
    if FindMother(a) == FindMother(b):
        cycle = True
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
    if cycle:
        break

if cycle:
    print("사이클을 형성하고 있습니다.")
else:
    print("사이클을 형성하지 않습니다.")