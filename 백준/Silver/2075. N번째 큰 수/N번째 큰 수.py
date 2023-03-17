import sys

input = sys.stdin.readline

from heapq import heappop, heappush

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

heap = []
for a in arr:
    for b in a:
        if len(heap) < n:
            heappush(heap, b)
        else:
            if heap[0] < b:
                heappop(heap)
                heappush(heap, b)
print(heap[0])
