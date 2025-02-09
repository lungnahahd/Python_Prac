# 크게 만들기 (2812)
## 난이도 : 골드 3


num_cnt, out_cnt = list(map(int, input().split()))
nums = input()
final_len = num_cnt - out_cnt
result = []
result.append(nums[0])
idx = 1
# 스택을 활용해서 진행 
while out_cnt != 0 and idx < num_cnt:
    temp_num = nums[idx]
    if temp_num <= result[-1]:
        result.append(temp_num)
    else:
        size = len(result)
        for i in range(size):
            if out_cnt ==0 :
                break
            if temp_num <= result[-1]:
                break
            else:
                result.pop()
                out_cnt -= 1
        result.append(temp_num)
    idx += 1

# 지우고 값이 남으면 뒤에 추가
if idx < num_cnt-1:
    for i in range(idx, num_cnt):
        result.append(nums[i])

# 동일한 값이 뒤에 여러개 있어서 최종 결과 맞춰주기
while len(result) > final_len:
    result.pop()

print(''.join(result))