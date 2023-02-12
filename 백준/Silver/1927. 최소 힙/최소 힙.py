import sys
input = sys.stdin.readline

from heapq import heappop, heappush

n = int(input())
heap = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(heap):
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, a)
