n = int(input())
result = 0
num_list = [1,2,5]

def sum_method(sum_obj, new_num):
    global n, result

    sum_new = sum_obj + new_num
    if (sum_new == n):
        result += 1
    elif (sum_new < n):
        sum_method(sum_new, 1)
        sum_method(sum_new, 2)
        sum_method(sum_new, 5)


sum_method(0, 1)
sum_method(0, 2)
sum_method(0, 5)
print(result)
