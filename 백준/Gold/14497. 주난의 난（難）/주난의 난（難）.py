import sys
input = sys.stdin.readline
from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    vis[r][c] = 0
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == -1:
                if arr[nr][nc] == '0':
                    q.appendleft((nr, nc))
                    vis[nr][nc] = vis[r][c]
                else:
                    q.append((nr, nc))
                    vis[nr][nc] = vis[r][c] + 1


n, m = map(int, input().split())
jn, jm, bn, bm = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]
vis = [[-1] * m for _ in range(n)]

bfs(jn - 1, jm - 1)

print(vis[bn - 1][bm - 1])
