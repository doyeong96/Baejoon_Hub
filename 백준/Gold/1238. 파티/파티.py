import sys
input = sys.stdin.readline

from heapq import heappop, heappush

INF = float('inf')


def dja(money, start):
    global maxV
    dis = [INF] * (n + 1)
    dis[start] = 0
    q = []
    heappush(q, (money, start))

    while q:
        weight, now = heappop(q)
        if weight > dis[now]:
            continue
        for nxt, node in g[now]:
            cost = weight + node
            if dis[nxt] > cost:
                dis[nxt] = cost
                heappush(q, (cost, nxt))
    return dis


# n명의 학생, m 개의 단방향 도로, k번 마을에 모여서 파티를 즐김
n, m, k = map(int, input().split())
g = [[] for _ in range(n + 1)]
maxV = -INF

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
for i in range(1, n + 1):
    go = dja(0, i)
    back = dja(0, k)
    maxV = max(maxV, go[k] + back[i])
print(maxV)
