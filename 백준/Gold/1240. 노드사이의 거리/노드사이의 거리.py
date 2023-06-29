# https://www.acmicpc.net/problem/1240
import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

from collections import deque


def bfs(s, e):
    Q = deque()
    Q.append((s, 0))
    vis[s] = 1
    while Q:
        now, co = Q.popleft()
        if now == e:
            return co
        for nxt, cos in g[now]:
            if vis[nxt] == 0:
                vis[nxt] = 1
                Q.append((nxt, co + cos))


n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
# print(g)

for _ in range(n - 1):
    a, b, cos = map(int, input().split())
    g[a].append((b, cos))
    g[b].append((a, cos))

# print(g)

for _ in range(m):
    s, e = map(int, input().split())
    vis = [0] * (n + 1)
    # C = []
    # print(dfs(s, e, 0))
    print(bfs(s, e))
    # print(C)
