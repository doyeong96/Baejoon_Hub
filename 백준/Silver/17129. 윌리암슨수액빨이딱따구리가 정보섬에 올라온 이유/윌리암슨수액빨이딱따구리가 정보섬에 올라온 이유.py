import sys


input = sys.stdin.readline
from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs(r, c):
    global first
    q = deque()
    q.append((r, c, 0))
    vis[r][c] = 1
    while q:
        r, c, cnt = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != 1 and vis[nr][nc] == 0:
                if arr[nr][nc] > 1:
                    return cnt + 1
                else:
                    q.append((nr, nc, cnt + 1))
                    vis[nr][nc] = 1
    return -1

n, m = map(int, input().split())
arr = [list(map(int, (input().strip()))) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
first = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            r, c = i, j
            break

res = bfs(r, c)
if res == -1:
    print("NIE")
else:
    print("TAK")
    print(res)
