import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify

def sol():
    global res
    if n == 1:
        return 0
    for i in range(n - 1):
        now = heappop(pq)
        daum = heappop(pq)
        res += now + daum
        heappush(pq, now + daum)
    return res


n = int(input())
pq = [int(input()) for _ in range(n)]
# pq.sort()
heapify(pq)

res = 0
print(sol())