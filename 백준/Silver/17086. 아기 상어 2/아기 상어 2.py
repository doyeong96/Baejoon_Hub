# 풀 문제 = 미로

import sys

input = sys.stdin.readline

dr = [0, 0, 1, -1, -1, -1, 1, 1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]
from heapq import heappop, heappush
from collections import deque


def bfs():
    while s:
        r, c = s.popleft()
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0 and arr[nr][nc] == 0:
                vis[nr][nc] = vis[r][c] + 1
                s.append((nr, nc))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
s = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            s.append((i, j))

bfs()
maxV = -987654321
for r in range(n):
    for c in range(m):
        if vis[r][c] > maxV:
            maxV = vis[r][c]
print(maxV)