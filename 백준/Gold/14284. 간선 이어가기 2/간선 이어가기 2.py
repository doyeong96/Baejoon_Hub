import sys
input = sys.stdin.readline

from heapq import heappop, heappush
INF = float('inf')


def dja():
    q = []
    heappush(q, (0, s))
    dis[s] = 0

    while q:
        price, now = heappop(q)
        if now == e:
            return price
        for next, nprice in g[now]:
            cost = price + nprice
            if cost > dis[next]:
                continue
            if dis[next] > cost:
                dis[next] = cost
                heappush(q, (cost, next))
    return dis[e]


n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
dis = [INF] * (n + 1)
for _ in range(m):
    # a -> b 는 c 의 가중치
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
s, e = map(int, input().split())

print(dja())
# print(dis[e])