import sys
input = sys.stdin.readline

getmoney = input().strip()
getmoney = int(getmoney)
count = 0

moneylist = [500, 100, 50, 10]

for give in moneylist:
    count += getmoney // give
    getmoney %= give

print(count)