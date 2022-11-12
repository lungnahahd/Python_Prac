p1,p2,p3 = list(map(int,input().split()))

import sys
from turtle import left
INT_MAX = sys.maxsize

minChange = 0
maxChange = 0

if p1 + p2 == p2*2:
    minChange,maxChange = 0,0
else:
    maxP1,maxP2,maxP3 = p1, p2, p3
    minP1,minP2,minP3 = p1, p2, p3
    left = False
    while maxP1+maxP3 != maxP2*2:
        maxChange += 1
        if abs(maxP2 - maxP1) >= abs(maxP3-maxP2):
            maxP2,maxP3 = maxP1 + 1, maxP2
        else:
            maxP1,maxP2 = maxP2, maxP3 -1 
    
    if minP1 + minP3 == minP2*2:
        minChange = 0
    elif abs(minP2-minP1) == 2 or abs(minP3-minP2) == 2 :
        minChange = 1
    else:
        minChange = 2
    # while minP1+minP3 != minP2*2:


    #     minChange += 1
    #     if abs(minP2-minP1) >= abs(minP3-minP2):
    #         minP2, minP3 = minP2 - 1, minP2
    #     else:
    #         minP1, minP2 = minP2, minP2 + 1

print(minChange)
print(maxChange)