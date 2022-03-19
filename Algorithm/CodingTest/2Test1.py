# 1번 문제 : 정답


def solution(goods):
    answer = []
    for i in range(len(goods)):
        result = set()
        temp = goods[0]
        del goods[0]
        notIn = True
        wordCount = 0
        while notIn:
            for j in range(len(temp) - wordCount):
                val = temp[j:j+wordCount+1]
                nowIn = True
                for k in range(len(goods)):
                    if val in goods[k]:
                        nowIn = True
                        break
                    else:
                        nowIn = False
                if not nowIn:
                    result.add(val)
                    notIn = False
            wordCount += 1
            if wordCount > len(temp):
                result.add("None")
                notIn = False
        semifinal = list(result)
        final = sorted(semifinal)
        last = ""
        for m in final:
            last = last + m + " "
        answer.append(last[:-1])
        goods.append(temp)
    return answer   


goods = ["pencil","cilicon","contrabase","picturelist"]
#goods = ["abcdeabcd","cdabe","abce","bcdeab"]
print(solution(goods))