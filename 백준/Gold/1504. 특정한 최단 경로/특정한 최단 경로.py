import sys

input = sys.stdin.readline

from heapq import heappop, heappush

INF = float('inf')


def dja(start):
    dis = [INF] * (n + 1)
    dis[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        weight, now = heappop(q)
        if weight > dis[now]:
            continue
        for nxt, node in g[now]:
            cost = weight + node
            if cost > dis[nxt]:
                continue
            dis[nxt] = cost
            heappush(q, (cost, nxt))
    return dis


n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
vis = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
v1,v2 = map(int, input().split())

res1 = dja(1)
res2 = dja(v1)
res3 = dja(v2)

path1 = res1[v1] + res2[v2] + res3[n]
path2 = res1[v2] + res3[v1] + res2[n]

dap = min(path1,path2)
if dap >= INF:
    print("-1")
else:
    print(dap)

