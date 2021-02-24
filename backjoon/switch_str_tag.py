import sys
input = sys.stdin.readline

sentence = input().strip()
senlist= list(sentence)
count = len(senlist)
finallist = [0 for i in range(count)]
temp = [0 for i in range(count)]
wait = False
give = False
head = 0
last = 0
if count == 1:
    print(sentence)
else:
    for i in range(count):
        if wait and senlist[i] != ">":
            finallist[i] = str(senlist[i])
            continue
        if senlist[i] == "<":
            wait = True
            finallist[i] = senlist[i]
            if head != 0:
                for j in range(head - last):
                    finallist[i - j - 1] = str(temp[last + j]) 
                last = head
        elif senlist[i] == ">":
            wait = False
            finallist[i] = senlist[i]
        elif senlist[i] == " ":
            finallist[i] = senlist[i]
            for j in range(head - last):
                finallist[i -j - 1] = str(temp[last + j])
            last = head 
        else:
            temp[head] = senlist[i]
            head += 1
        if i == count - 1 and last != head:
            for j in range(head - last):
                finallist[i -j] = str(temp[last + j])
print(''.join(finallist))







