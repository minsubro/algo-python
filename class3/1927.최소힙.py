import heapq, sys
input = sys.stdin.readline
min_heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        print(0 if len(min_heap) == 0 else heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, x)