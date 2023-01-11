from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    while Q:
        r, c, = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0 and arr[nr][nc] == 0:
                Q.append((nr, nc))
                vis[nr][nc] = 1


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
dap = 'NO'

for i in range(1):
    for j in range(m):
        if arr[i][j] == 0:
            bfs(i, j)

for i in range(n - 1, n - 2, -1):
    for j in range(m -1 , -1, -1):
        if vis[i][j] == 1:
            dap = 'YES'
print(dap)
