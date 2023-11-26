# 테디의 여행 플래너

num_city, num_behavior = tuple(map(int,input().split()))
cities = input().split()
sticker = [True for idx in range(num_city)]
pin = 0

class Node:
    def __init__(self, city):
        self.city = city
        self.right = None
        self.left = None

    def get_name(self):
        print(self.city, end=' ')

    def get_right(self):
        if (self.right == None or self.right == self.left):
            print('-1', end=' ')
        else:
            self.right.get_name()
    
    def get_left(self):
        if(self.left != None and self.right != self.left):
            self.left.get_name()


pin_node = Node(cities[0])
fst_node = pin_node


for idx in range(len(cities)-1):
    right = idx + 1
    
    pin_node.right = Node(cities[right])
    pre_node = pin_node
    pin_node = pin_node.right
    pin_node.left = pre_node

lst_node = pin_node
pin_node.right = fst_node
pin_node = pin_node.right
pin_node.left = lst_node

        
for _ in range(num_behavior):
    cmd = input().split()
    if(cmd[0] == '1'):
        if(pin_node.right != None):
            pin_node = pin_node.right
    elif(cmd[0] == '2'):
        if(pin_node.left != None):
            pin_node = pin_node.left
    elif(cmd[0] == '3'):
        if(pin_node.right != None):
            pin_node.right = pin_node.right.right
            pin_node.right.left = pin_node
    elif(cmd[0] == '4'):
        temp_node = pin_node.right
        pin_node.right = Node(cmd[1])
        pin_node.right.left = pin_node
        pin_node.right.right = temp_node
        temp_node.left = pin_node.right

    pin_node.get_left()
    pin_node.get_right()
    print()


