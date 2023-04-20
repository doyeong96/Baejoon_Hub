import sys
input = sys.stdin.readline

from heapq import heappop, heappush

from collections import deque

INF = float('inf')


def dja():
    q = []
    heappush(q, (0, s))
    dis[s] = 0

    while q:
        price, now = heappop(q)
        for next, nprice in g[now]:
            cost = price + nprice
            if dis[next] > cost:
                dis[next] = cost
                heappush(q, (cost, next))


n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
dis = [INF] * (n + 1)
for _ in range(m):
    # a -> b 는 c 의 가중치
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
s, e = map(int, input().split())

dja()
print(dis[e])