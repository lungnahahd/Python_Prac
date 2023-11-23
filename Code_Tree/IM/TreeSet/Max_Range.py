max_num, remove_cnt = input().split()
max_num, remove_cnt =  int(max_num), int(remove_cnt)
remove_nums = list(map(int,input().split()))
num_list = [(0,max_num)]
big_range = 0

for idx in range(remove_cnt):
    now_remove = remove_nums[idx]
    size = len(num_list)
    for now in range(size):
        start,end = num_list.pop(0)
        if (start > now_remove or end < now_remove):
            num_list.append((start,end))
            big_range = max(big_range, end-start+1)
        elif (start == now_remove):
            big_range = max(big_range, end-start)
            if(start != end ):
                num_list.append((start+1, end))
        elif (end == now_remove):
            big_range = max(big_range, end-start)
            if(start != end):
                num_list.append((start, end-1))
        else:
            num_list.append((start, now_remove-1))
            num_list.append((now_remove+1, end))            
            big_range = max(big_range, now_remove-start, end-now_remove)
    print(big_range)
    big_range = 0
