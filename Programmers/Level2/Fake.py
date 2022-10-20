# 위장


def solution(clothes):
    answer = -1
    save_dict = dict()
    for _,kind in clothes:
        if kind in save_dict:
            save_dict[kind] += 1
        else:
            save_dict[kind] = 1
    temp = 1
    for _, val in save_dict.items():
        temp *= (val+1)
    answer += temp
    return answer

c = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
c2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(c))
print(solution(c2))