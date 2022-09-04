# 괄호 문자열의 적합성 판단

get_str = input()
make_list = list(get_str)

save = 0
for i in make_list:
    if i == "(":
        save += 1
    else:
        save -= 1
    if save < 0:
        break
if save == 0:
    print("Yes")
else:
    print("No")