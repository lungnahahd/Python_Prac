num_size, space_count = list(map(int, input().split()))
num_list = list(map(int, input().split()))
num_sum = [0 for _ in range(num_size)]
num_sum[0] = num_list[0]

result = 0

for idx in range(1,num_size):
    num_sum[idx] = num_sum[idx-1] + num_list[idx]



def StackNum(stack, idx):
    global result
    
    if (len(stack) == space_count - 1):
        temp_result = 0
        before = num_size 
        while(stack):
            now = stack.pop()
            temp_result += (num_sum[before-1] - num_sum[now])
            before = now
        temp_result += (num_sum[before - 1])
        result = max(result, temp_result)
    else:
        if (idx + 2 > num_size - 2):
            return
        idx += 2
        while(idx <= num_size -2):
            stack.append(idx)
            temp_stack = stack[:]
            StackNum(temp_stack, idx)
            stack.pop()
            idx += 1

for idx in range(1, num_size -(space_count-1) * 2 + 1):
    StackNum([idx], idx)
print(result)
