import sys
input = sys.stdin.readline

from heapq import heappop, heappush, heapify

n, m = map(int, input().split())
li = sorted(list(map(int, input().split())), reverse=True)
q = []
cnt = 0
for e in li:
    if len(q) < m:
        heappush(q, e)
    else:
        a = heappop(q)
        heappush(q,a+e)
print(max(q))