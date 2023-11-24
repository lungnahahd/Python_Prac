import heapq

test = int(input())

for _ in range(test):
    test_size = int(input())
    num_list = list(map(int, input().split()))
    heap = []
    for idx in range(len(num_list)):
        heapq.heappush(heap,-num_list[idx])
        if (idx % 2 == 0):
            temp = []
            for _ in range(len(heap)):
                temp.append(heapq.heappop(heap))
            print(-temp[idx//2], end= ' ')
            heapq.heapify(temp)
            heap = temp
    print()
