# 친구 네트워크 (4195)

case_num = int(input())

answer = []
for _ in range(case_num):
    cnt = int(input())
    friend_dict = dict()
    for _ in range(cnt):
        temp_answer = 0
        left, right = input().split()
        if left in friend_dict:
            temp = friend_dict[left]
            temp.add(right)
            friend_dict[left] = temp
        else:
            friend_dict[left] = set([right])
        #temp_answer += len(friend_dict[left])
        if right in friend_dict:
            temp = friend_dict[right]
            temp.add(left)
            friend_dict[right] = temp
        else:
            friend_dict[right] = set([left])
        temp_right,temp_left = friend_dict[right], friend_dict[left]
        temp_union = temp_right.union(temp_left)
        friend_dict[left] = temp_union
        friend_dict[right] = temp_union
        temp_answer 
        temp_answer += len(temp_union)
        answer.append(temp_answer)

for relation in answer:
    print(relation)