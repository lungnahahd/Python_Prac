# 트리 순위(하)
## 난이도 : 하

cnt_node = int(input())

# 트리 객체
class Node:
    def __init__(self):
        self.root, self.right, self.left = None, None, None

    def set_node(self, root, left, right):
        self.root = root
        self.right = right
        self.left = left

nodes = [Node() for _ in range(cnt_node)]

# 트리를 만드는 부분
for _ in range(cnt_node):
    root, left, right = input().split()
    nodes[ord(root)-65].set_node(ord(root)-65, ord(left)-65, ord(right)-65)

# 전위 순회
def pre_search(node):
    print(chr(node.root + 65), end='')
    if (node.left >= 0):
        pre_search(nodes[node.left])   
    if (node.right >= 0):
        pre_search(nodes[node.right])
    return

# 중위 순회
def mid_search(node):
    if (node.left >= 0):
        mid_search(nodes[node.left])
    print(chr(node.root+65), end='')
    if (node.right >= 0):
        mid_search(nodes[node.right])

# 후위 순회
def bak_search(node):
    if (node.left >= 0):
        bak_search(nodes[node.left])
    if (node.right >= 0):
        bak_search(nodes[node.right])
    print(chr(node.root+65), end='')

pre_search(nodes[0])
print()
mid_search(nodes[0])
print()
bak_search(nodes[0])
print()