# 정수 명령 처리 6
## heapq를 활용해서 최대 우선 큐 처리 구현

import heapq
import sys

from numpy import empty


input = sys.stdin.readline

sizeNum = int(input())

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def push(self,item):
        heapq.heappush(self.queue, -item)
    
    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0 
        return not self.queue

    def size(self):
        return len(self.queue)
    
    def pop(self):
        if self.empty() == 1:
            raise Exception(" Empty Error")
        
        return -heapq.heappop(self.queue)
    
    def top(self):
        if self.empty() == 1:
            raise Exception("Empty Error")
        return -self.queue[0]


pQueue = PriorityQueue()
for i in range(sizeNum):
    case = input().split()
    if case[0] == "push":
        pQueue.push(int(case[1]))
    elif case[0] == "top":
        print(pQueue.top())
    elif case[0] == "size":
        print(pQueue.size())
    elif case[0] == "pop":
        print(pQueue.pop()) 
    elif case[0] == "empty":
        print(pQueue.empty())

    