# 트리 높이와 너비 (2250)
## 난이도 : 중


class Node:
    def __init__(self):
        self.root = None
        self.right = None
        self.left = None
        self.level = None
        self.width = None
    
    def set_node(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right
    
    def set_width(self, width):
        self.width = width

    def set_level(self, level):
        self.level = level
    
level_dict = dict()
cnt_node = int(input())
node_order = []
level_chk = [1 for _ in range(cnt_node)]

for _ in range(cnt_node):
    root, left, right = list(map(int, input().split()))
    now_node = Node()
    now_node.set_node(root, left, right)
    now_lvl = level_chk[root-1]
    now_node.set_level(now_lvl)
    if now_lvl in level_dict:
        level_dict[now_lvl].append(root)
    else:
        level_dict[now_lvl] = [root]

    if left != -1:
        level_chk[left-1] = now_lvl + 1
    if right != -1:
        level_chk[right-1] = now_lvl + 1
    node_order.append(now_node)

g_width = 1

def pre_order(node):
    global g_width
    if node.left != -1:
        pre_order(node_order[node.left-1])
    node_order[node.root-1].set_width(g_width)
    g_width += 1
    if node.right != -1:
        pre_order(node_order[node.right-1])

pre_order(node_order[0])

answer_level = 0
answer_val = 0
for idx in range(len(level_dict)):
    now_nodes = level_dict[idx+1]
    temp_val = 0
    if (len(now_nodes) == 1):
        temp_val = 1
    else:
        start = min(now_nodes)
        end = max(now_nodes)
        temp_val = node_order[end-1].width - node_order[start-1].width + 1
    if temp_val > answer_val:
        answer_val = temp_val
        answer_level = idx + 1
print(answer_level, end=' ')
print(answer_val)