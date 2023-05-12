import sys

input = sys.stdin.readline

# sys.stdin = open('0000sample.txt')
#sys.stdin = open('0000sample.txt')
from heapq import heappop, heappush

INF = float('inf')


def dja(start):
    Q = []
    heappush(Q, (0, start))
    vis[start] = 0

    while Q:
        # 현재 비용, 현재 위치
        now_w, now = heappop(Q)
        if vis[now] < now_w:
            continue
        for nxt, nxt_w in g[now]:
            cost = nxt_w + now_w
            if vis[nxt] > cost:
                vis[nxt] = cost
                heappush(Q, (cost, nxt))


n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
dap = []
for _ in range(m):
    a = list(map(int, input().split()))
    # 선박 추가운행
    if a[0] == 1:
        g[a[1]].append((a[2], a[3]))
        g[a[2]].append((a[1], a[3]))
    # 고객의 표
    else:
        vis = [INF] * (n + 1)
        dja(a[1])
        if vis[a[2]] == INF:
            dap.append(-1)
        else:
            dap.append(vis[a[2]])
for i in dap:
    print(i)
