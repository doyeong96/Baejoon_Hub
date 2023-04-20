import sys
input = sys.stdin.readline

from heapq import heappop, heappush

from collections import deque

INF = float('inf')


def dja(start):
    Q = []
    heappush(Q, (0, start))
    road[start] = 0
    while Q:
        node, now = heappop(Q)
        if road[now] < node:
            continue
        for next, nnode in g[now]:
            # 비용 = 현재비용 + 다음 노드로 이동하는 비용
            cost = node + nnode
            if road[next] > cost:
                road[next] = cost
                heappush(Q, (cost, next))


n, m = map(int, input().split())
st = int(input())
g = [[] for _ in range(n + 1)]
road = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    # 거리, 다음위치
    g[a].append((b, c))
    # g[b].append((a, c))
# print(g)
dja(st)
# print(road)
for i in range(1, n + 1):
    if road[i] == INF:
        print('INF')
    else:
        print(road[i])
