# 친구 네트워크 (4195)

case_num = int(input())

answer = []
for _ in range(case_num):
    cnt = int(input())
    friend_dict = dict()
    for _ in range(cnt):
        temp_answer = 0
        left, right = input().split()
        
        
        temp_left, temp_right = set([left]), set([right])

        if left in friend_dict:
            temp_left = friend_dict[left]
        if right in friend_dict:
            temp_right = friend_dict[right]        
        
        temp_union = temp_left.union(temp_right)
        answer.append(len(temp_union))
        friend_dict[left], friend_dict[right] = temp_union, temp_union

for relation in answer:
    print(relation)