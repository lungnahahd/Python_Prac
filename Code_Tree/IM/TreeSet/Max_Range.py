max_num, remove_cnt = input().split()
max_num, remove_cnt =  int(max_num), int(remove_cnt)
remove_nums = list(map(int,input().split()))
num_list = [[idx for idx in range(max_num+1)]]
big_range = 0

for idx in range(remove_cnt):
    now_remove = remove_nums[idx]
    size = len(num_list)
    for now in range(size):
        now_list = num_list.pop(0)
        start, end = now_list[0], now_list[-1]
        if (start > now_remove or end < now_remove):
            num_list.append(now_list)
            big_range = max(big_range, end-start+1)
        elif (start == now_remove):
            now_list.remove(start)
            big_range = max(big_range, end-start)
            if(len(now_list) != 0):
                num_list.append(now_list)
        elif (end == now_remove):
            now_list.remove(end)
            big_range = max(big_range, end-start)
            if(len(now_list) != 0):
                num_list.append(now_list)
        else:
            s_temp, e_temp = [], []
            for temp_num in now_list:
                if temp_num < now_remove:
                    s_temp.append(temp_num)
                elif temp_num > now_remove:
                    e_temp.append(temp_num)
            
            num_list.append(s_temp)
            num_list.append(e_temp)
            big_range = max(big_range, len(s_temp), len(e_temp))
    print(big_range)
    big_range = 0
