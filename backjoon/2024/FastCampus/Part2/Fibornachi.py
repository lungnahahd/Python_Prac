# 피보나치 수열
## 난이도 : 하

fb_arr = [0, 1]

cnt = int(input())

for idx in range(2,cnt+1):
    fb_arr.append(fb_arr[idx-1] + fb_arr[idx-2])

print(fb_arr[cnt])
