import sys

input = sys.stdin.readline

from heapq import heappop, heappush

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
# li.sort(key=lambda x: (x[0], x[1]))
li.sort()
# print(li)

Q = []
for s, e in li:
    if not Q:
        heappush(Q, e)
    else:
        if Q[0] <= s:
            heappop(Q)
            heappush(Q, e)
        else:
            heappush(Q, e)

print(len(Q))
