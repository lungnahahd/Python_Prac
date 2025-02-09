# 블랙잭 (2798)

card_count, want_num = tuple(map(int, input().split()))
cards = list(map(int, input().split()))

answer = 0

for first in range(card_count):
    for second in range(first+1, card_count):
        for third in range(second+1, card_count):
            temp_answer = cards[first] + cards[second] + cards[third]
            if (temp_answer <= want_num and answer < temp_answer):
                answer = temp_answer

print(answer)