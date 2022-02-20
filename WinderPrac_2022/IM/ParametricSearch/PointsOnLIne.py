# 선분 위의 점
## n개의 점과 m개의 선분이 주어질 때, 각 선분 위에 몇개의 점이 있는지 구하는 프로그램을 작성해보세요.
### 테크닉 : 이진 탐색



n, m = input().split()
pointCount = int(n)
lineCount = int(m)

pointS = list(map(int, input().split()))
pointS.sort()

for i in range(lineCount):
    start, end = input().split()
    start, end = int(start), int(end)
    startMin = pointCount
    endMax = -1
    startLeft,startRight = 0, pointCount-1
    endLeft,endRight = 0, pointCount-1

    # 주어진 점들에서 시작점보다 크거나 같은 점 중 최소를 선택하는 경우
    while startLeft <= startRight:
        mid = (startLeft + startRight) // 2
        if start <= pointS[mid]:
            startMin = min(mid, startMin)
            startRight = mid -1
        else:
            startLeft = mid + 1

    # 주어진 점들에서 도착점보다 작거나 같은 점 중 최대를 선택하는 경우
    while endLeft <= endRight:
        mid = (endLeft + endRight) // 2
        if pointS[mid] <= end:
            # if end == pointS[mid]:
            #     endMax = mid
            #     break
            endMax = max(endMax, mid)
            endLeft = mid + 1
        else:
            endRight = mid -1

    if endMax == -1 or startMin == pointCount:
        print(0)
    else:
        
        print(endMax - startMin + 1)